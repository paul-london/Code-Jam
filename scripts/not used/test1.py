import pandas as pd
import numpy as np
import time
import googlemaps
import ast
import warnings

warnings.filterwarnings('ignore')

# Load data
parks_subset = pd.read_csv('/Users/priti/Documents/GitHub/Code-Jam/data/parks_w.csv')  # path to your 9 parks
states_master = pd.read_csv('//Users/priti/Documents/GitHub/Code-Jam/data/states_master.csv')  # should have 'abbreviation' and 'coordinates'

# Google Maps API key
api_key_g = 'AIzaSyBsZE5PsKrO7cQP1vUILx4j9HMCdPK3x_g'
gmaps = googlemaps.Client(key=api_key_g)

def VacationRoute(home_state):
    # 1. Get coordinates from string to tuple
    coords_str = states_master.loc[
        states_master['abbreviation'] == home_state, 'coordinates'
    ].values[0]
    home_state_coords = ast.literal_eval(coords_str)  # now a real tuple (lat, lon)

    # 2. Prepare dataframe with home state at top
    parks_subset_gnn = parks_subset[['name', 'latitude', 'longitude']].reset_index(drop=True)
    home_state_row = pd.DataFrame(
        [[home_state, home_state_coords[0], home_state_coords[1]]],
        columns=['name', 'latitude', 'longitude']
    )
    parks_with_home = pd.concat((home_state_row, parks_subset_gnn), ignore_index=True)

    # 3. Set up origin and destination dictionaries
    origin_home = {
        parks_with_home['name'][0]: (parks_with_home['latitude'][0], parks_with_home['longitude'][0])
    }
    destinations = {
        name: (lat, lon)
        for name, lat, lon in zip(
            parks_with_home['name'][1:], 
            parks_with_home['latitude'][1:], 
            parks_with_home['longitude'][1:]
        )
    }

    # 4. Call Google Maps API for travel distances
    def GoogleMaps(origins, destinations):
        travel_array = np.zeros((len(origins) * len(destinations), 4), dtype=object)
        i = 0
        for origin_name, origin_coords in origins.items():
            for dest_name, dest_coords in destinations.items():
                if origin_name == dest_name:
                    continue
                try:
                    result = gmaps.distance_matrix(
                        origins=[origin_coords],
                        destinations=[dest_coords],
                        mode='driving'
                    )
                    element = result['rows'][0]['elements'][0]
                    if element['status'] == 'OK':
                        distance_meters = element['distance']['value']
                        duration_seconds = element['duration']['value']
                        travel_array[i] = [
                            origin_name,
                            dest_name,
                            np.round(distance_meters / 1609.344, 2),  # miles
                            np.round(duration_seconds / 3600, 2)      # hours
                        ]
                        print(f"{origin_name} → {dest_name} = {travel_array[i][2]} mi ({travel_array[i][3]} hrs)")
                        i += 1
                        time.sleep(0.05)
                except Exception as e:
                    print(f"Error fetching distance from {origin_name} to {dest_name}: {e}")
        return travel_array

    travel_array = GoogleMaps(origin_home, destinations)

    # 5. Build distance matrix for GNN
    park_list = list(parks_with_home['name'])  # includes home state
    park_indices = {name: idx for idx, name in enumerate(park_list)}
    n = len(park_list)
    gnn_matrix = np.full((n, n), np.inf)

    for row in travel_array:
        origin, destination, dist_mi, _ = row
        i = park_indices[origin]
        j = park_indices[destination]
        gnn_matrix[i][j] = dist_mi

    # 6. Greedy Nearest Neighbor algorithm
    def greedy_nearest_neighbor(matrix, start=0):
        n = matrix.shape[0]
        visited = [False] * n
        route = [start]
        visited[start] = True
        current = start

        for _ in range(n - 1):
            nearest = None
            nearest_dist = float('inf')
            for i in range(n):
                if not visited[i] and matrix[current][i] < nearest_dist:
                    nearest = i
                    nearest_dist = matrix[current][i]
            if nearest is not None:
                route.append(nearest)
                visited[nearest] = True
                current = nearest
        return route

    # 7. Get the optimal route (indices → names)
    route_indices = greedy_nearest_neighbor(gnn_matrix, start=0)
    optimal_route = [park_list[i] for i in route_indices]

    return optimal_route

route = VacationRoute("PA")
print("\nOptimal Roadtrip Route:")
for i, stop in enumerate(route):
    print(f"{i+1}. {stop}")
