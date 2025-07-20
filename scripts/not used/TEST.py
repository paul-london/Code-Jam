import pandas as pd
import numpy as np
import time
import googlemaps
import ast

# Initialize Google Maps API client
api_key_g = 'AIzaSyBsZE5PsKrO7cQP1vUILx4j9HMCdPK3x_g'
gmaps = googlemaps.Client(key=api_key_g)

# Load your data
parks_subset = pd.read_csv('../data/parks_w.csv')
states_master = pd.read_csv('../data/states_master.csv')

def VacationRoute(home_state):
    # Get coordinates for home state
    home_coords = ast.literal_eval(
    states_master.loc[states_master['abbreviation'] == home_state, 'coordinates'].values[0]
    
    # Create new dataframe with home state as the first row
    parks_gnn = parks_subset[['name', 'latitude', 'longitude']].copy()
    home_row = pd.DataFrame([[home_state, home_coords[0], home_coords[1]]], columns=parks_gnn.columns)
    parks_gnn = pd.concat([home_row, parks_gnn], ignore_index=True)
    
    # Create dictionary of name to coordinate tuples
    names = parks_gnn['name'].tolist()
    coords = list(zip(parks_gnn['latitude'], parks_gnn['longitude']))
    coords_dict = dict(zip(names, coords))

    # Initialize distance matrix
    n = len(names)
    gnn_matrix = np.full((n, n), np.inf)

    # Populate matrix using Google Maps API
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            origin = coords[i]
            destination = coords[j]
            result = gmaps.distance_matrix([origin], [destination], mode='driving')
            element = result['rows'][0]['elements'][0]
            if element['status'] == 'OK':
                gnn_matrix[i][j] = element['distance']['value'] / 1609.344  # convert to miles
            time.sleep(0.1)  # Pause to avoid API limits

    # Greedy Nearest Neighbor algorithm
    def greedy_nearest_neighbor(matrix, start=0):
        visited = [False] * n
        route = [start]
        visited[start] = True
        current = start

        for _ in range(n - 1):
            next_city = np.argmin([matrix[current][j] if not visited[j] else np.inf for j in range(n)])
            route.append(next_city)
            visited[next_city] = True
            current = next_city

        return route

    # Get optimal visiting order of indices and corresponding names
    route_indices = greedy_nearest_neighbor(gnn_matrix, start=0)
    route_names = [names[i] for i in route_indices]
    return route_names