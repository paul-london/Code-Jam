# Import required libraries
import pandas as pd
import numpy as np
import folium as fl
import time
import googlemaps

# Neatly display dataframes
from tabulate import tabulate

# Display all fields with pandas
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Ignore warnings
import warnings
warnings.filterwarnings('ignore')

# Initialize Google Maps API client
api_key_g = 'AIzaSyBsZE5PsKrO7cQP1vUILx4j9HMCdPK3x_g'
gmaps = googlemaps.Client(key=api_key_g)

# Define dataframes used in the function
parks = pd.read_csv('../data/raw/parks.csv')
parks_master = pd.read_csv('../data/parks_master.csv')
parks_subset = pd.read_csv('../data/parks_w.csv')

states = pd.read_csv('../data/raw/states.csv')
states_master = pd.read_csv('../data/states_master.csv')

route = []

def VacationRoute(home_state):
    import ast
    
    # Force coordinates column to be proper tuples of floats
    def force_tuple_floats(coord):
        if isinstance(coord, str):
            try:
                coord = ast.literal_eval(coord)
            except Exception as e:
                print(f"Error parsing coord string {coord}: {e}")
                raise
        if not (isinstance(coord, (tuple, list)) and len(coord) == 2):
            raise ValueError(f"Bad coord structure: {coord}")
        return tuple(map(float, coord))
    
    # Make sure states_master coordinates are clean tuples of floats
    if 'coordinates' not in states_master.columns:
        states_master['coordinates'] = list(zip(states_master['latitude'], states_master['longitude']))
    states_master['coordinates'] = states_master['coordinates'].apply(force_tuple_floats)
    
    # Get coordinates for home state
    home_state_coords = states_master.loc[states_master['abbreviation'] == home_state, 'coordinates'].values[0]
    print(f"Home state: {home_state} coordinates: {home_state_coords} type: {type(home_state_coords)}")
    
    parks_subset_gnn = parks_subset[['name', 'latitude', 'longitude']].reset_index(drop=True)
    # Rebuild origin row with floats
    home_state_row = [home_state, float(home_state_coords[0]), float(home_state_coords[1])]
    home_state_df = pd.DataFrame([home_state_row], columns=['name', 'latitude', 'longitude'])
    parks_subset_gnn_with_origin = pd.concat([home_state_df, parks_subset_gnn], ignore_index=True)

    # Build origin and destination dicts
    origin_home = {
        parks_subset_gnn_with_origin.loc[0, 'name']: 
        (float(parks_subset_gnn_with_origin.loc[0, 'latitude']), float(parks_subset_gnn_with_origin.loc[0, 'longitude']))
    }
    destinations = {
        parks_subset_gnn_with_origin.loc[i, 'name']: 
        (float(parks_subset_gnn_with_origin.loc[i, 'latitude']), float(parks_subset_gnn_with_origin.loc[i, 'longitude']))
        for i in range(1, len(parks_subset_gnn_with_origin))
    }
    
    print(f"Origin_home sample: {list(origin_home.items())[0]}")
    print(f"Destination sample: {list(destinations.items())[0]}")
    
    # Google Maps function
    def GoogleMaps(origins, destinations):
        travel_array = np.zeros((len(origins) * len(destinations), 4), dtype=object)
        i = 0
        
        for origin_name, origin_coords in origins.items():
            for dest_name, dest_coords in destinations.items():
                if origin_name == dest_name:
                    continue
                
                # Debug prints for coords before API call
                print(f"\nCalling gmaps.distance_matrix with:")
                print(f"  origin_name: {origin_name}")
                print(f"  origin_coords: {origin_coords} type: {type(origin_coords)}")
                print(f"  origin_coords elements types: {[type(x) for x in origin_coords]}")
                print(f"  dest_name: {dest_name}")
                print(f"  dest_coords: {dest_coords} type: {type(dest_coords)}")
                print(f"  dest_coords elements types: {[type(x) for x in dest_coords]}")
                
                # Ensure coords are tuples of floats
                def ensure_tuple(coord):
                    if isinstance(coord, str):
                        import ast
                        try:
                            coord = ast.literal_eval(coord)
                        except Exception as e:
                            print(f"Error parsing coord string {coord}: {e}")
                            raise
                    if not (isinstance(coord, (tuple, list)) and len(coord) == 2):
                        raise ValueError(f"Bad coord structure: {coord}")
                    return tuple(map(float, coord))
                
                origin_coords = ensure_tuple(origin_coords)
                dest_coords = ensure_tuple(dest_coords)
                
                # Extra debug after ensuring tuples
                print(f"  After ensure_tuple:")
                print(f"    origin_coords: {origin_coords} type: {type(origin_coords)}")
                print(f"    dest_coords: {dest_coords} type: {type(dest_coords)}")
                print(f"    origin_coords elements types: {[type(x) for x in origin_coords]}")
                print(f"    dest_coords elements types: {[type(x) for x in dest_coords]}")

                # Call Google Maps Distance Matrix API
                result = gmaps.distance_matrix(
                    origins=[origin_coords], 
                    destinations=[dest_coords], 
                    mode='driving'
                )
                element = result['rows'][0]['elements'][0]

                if element['status'] == 'OK':
                    distance_meters = element['distance']['value']
                    duration_seconds = element['duration']['value']

                    travel_array[i, 0] = origin_name
                    travel_array[i, 1] = dest_name
                    travel_array[i, 2] = np.round(distance_meters / 1609.344, 2)  # miles
                    travel_array[i, 3] = np.round(duration_seconds / 3600, 2)     # hours

                    print(f"{origin_name} → {dest_name} = {travel_array[i, 2]} mi ({travel_array[i, 3]} hrs)")
                    i += 1

                time.sleep(0.05)

        return travel_array[:i]  # Trim unused rows

    # Call GoogleMaps with debug
    travel_array = GoogleMaps(origin_home, destinations)

    # Create park index mapping
    all_parks = list(origin_home.keys()) + list(destinations.keys())
    park_indices = {name: idx for idx, name in enumerate(all_parks)}
    n = len(all_parks)

    # Initialize distance matrix
    gnn_matrix = np.full((n, n), np.inf)

    for row in travel_array:
        origin, destination, dist_mi, _ = row
        i = park_indices[origin]
        j = park_indices[destination]
        gnn_matrix[i][j] = dist_mi

    # Greedy Nearest Neighbor function
    def greedy_nearest_neighbor(gnn_matrix, start=0):
        n = gnn_matrix.shape[0]
        visited = [False] * n
        route = [start]
        visited[start] = True

        current = start
        for _ in range(n - 1):
            distances = gnn_matrix[current]
            nearest = None
            nearest_dist = float('inf')
            for i in range(n):
                if not visited[i] and distances[i] < nearest_dist:
                    nearest = i
                    nearest_dist = distances[i]

            if nearest is None:
                break

            route.append(nearest)
            visited[nearest] = True
            current = nearest

        return route

    # Run the algorithm
    route_indices = greedy_nearest_neighbor(gnn_matrix, start=0)
    route_names = [all_parks[i] for i in route_indices]

    return route_names

