# Import required libraries
import pandas as pd
import json
import numpy as np
import folium as fl
import time
from tabulate import tabulate
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
    # Set up location data
    home_state_coords = states_master.loc[
        states_master['abbreviation'] == home_state, 'coordinates'
    ].values[0]
    
    parks_subset_gnn = parks_subset[['name', 'latitude', 'longitude']].reset_index(drop=True)
    home_state_row = [home_state, home_state_coords[0], home_state_coords[1]]
    home_state_df = pd.DataFrame([home_state_row], columns=['name', 'latitude', 'longitude'])
    parks_subset_gnn_with_origin = pd.concat([home_state_df, parks_subset_gnn], ignore_index=True)

    # Build origin and destination dictionaries for Google Maps
    origin_home = {
        parks_subset_gnn_with_origin.loc[0, 'name']: 
        (parks_subset_gnn_with_origin.loc[0, 'latitude'], parks_subset_gnn_with_origin.loc[0, 'longitude'])
    }
    
    destinations = {
        parks_subset_gnn_with_origin.loc[i, 'name']: 
        (parks_subset_gnn_with_origin.loc[i, 'latitude'], parks_subset_gnn_with_origin.loc[i, 'longitude'])
        for i in range(1, len(parks_subset_gnn_with_origin))
    }

    # Google Maps function
    def GoogleMaps(origins, destinations):
        travel_array = np.zeros((len(origins) * len(destinations), 4), dtype=object)
        i = 0
        for origin_name, origin_coords in origins.items():
            for dest_name, dest_coords in destinations.items():
                if origin_name == dest_name:
                    continue
                
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

        return travel_array[:i]  # Trim any unused rows

    # Get distance data
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
