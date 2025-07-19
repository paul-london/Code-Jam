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
parks_subset = pd.read_csv('../data/raw/parks_w.csv')

states = pd.read_csv('../data/raw/states.csv')
states_master = pd.read_csv('../data/states_master.csv')

def VacationRoute(home_state):
    # Set up location data
    # Look up home state coords from state df based on user input
    home_state_coords = states_master.loc[states_master['abbreviation'] == home_state, 'coordinates'].values[0]
    # Extract fields for greedy nearest neighbor algorithm from park subset df
    parks_subset_gnn = parks_subset[['name', 'latitude', 'longitude']].reset_index(drop=True)
    # Generate new df row with the user's home state and its latitude, and longitude
    home_state_row = [home_state, home_state_coords[0], home_state_coords[1]]
    # Prepend new home state row to the park subset df
    parks_subset_gnn_with_origin = pd.concat[home_state_row, parks_subset_gnn]



    # Google Maps
    # Reformat parks_subset_gnn_with_origin for use in Google Maps (dict w/ coordinate tuple)
    origin_home = {parks_subset_gnn_with_origin['name'][0]: 
                   (parks_subset_gnn_with_origin['latitude'][0], parks_subset_gnn_with_origin['longitude'][0])}
    destinations = {parks_subset_gnn_with_origin['name'][1:]: 
                   (parks_subset_gnn_with_origin['latitude'][1:], parks_subset_gnn_with_origin['longitude'][1:])}

    
    # Google Maps function
    # Loop through all dictionary items
    def GoogleMaps(origins, destinations):
        """
        Purpose:
        Calculates travel distances and travel times between all locations in origins vs.
        all locations in destinations.
        
        Arguments:
        origins: all possible starting points 
        destinations: all possible ending points
        (Both are dictionaries with keys: location names and values: coordinate tuples (latitude, longitude))
        """
        # Initialize distance matrix
        travel_array = np.zeros((len(origins) * (len(destinations)), 4), dtype = object)
        i = 0
        for origin_name, origin_coords in origins.items():
            for dest_name, dest_coords in destinations.items():
                # Skip pairs where origin = destination (distance 0)
                if origin_name == dest_name:
                    continue
        
                # Travel data from origin to destination
                result = gmaps.distance_matrix(origins=[origin_coords], destinations=[dest_coords], mode='driving')
                element = result['rows'][0]['elements'][0]
                
                # Check for valid result
                if element['status'] == 'OK':
                    distance_meters = element['distance']['value']
                    duration_seconds = element['duration']['value']

                # Fill in matrix with travel information        
                travel_array[i, 0] = origin_name
                travel_array[i, 1] = dest_name
                travel_array[i, 2] = np.round(distance_meters / 1609.344, 2)
                travel_array[i, 3] = np.round(duration_seconds / 3600, 2)

                i += 1

                # Debug (remove)
                print(f"{origin_name} → {dest_name} = {np.round((distance_meters/1609.344),2)} mi ({np.round((duration_seconds/3600),2)} hrs)") # convert to miles and hours

                time.sleep(0.05) # Brief API pause

                return travel_array
            
    # Run GoogleMaps function to determine travel distances from home state to 9 parks
    GoogleMaps(origin_home, destinations)

    # Greedy Nearest Neighbors
    # Set up matrix
    # Extract indices from park list
    park_list = list(origin_home.keys())
    park_indices = {name: idx for idx, name in enumerate(park_list)}
    n = len(origin_home)
    gnn_matrix = np.full((n, n), np.inf)  # fill with inf travel distances to start

    # Populate matrix with travel distances in miles
    for row in travel_array:
        origin, destination, dist_mi, _ = row
        i = park_indices[origin]
        j = park_indices[destination]
        gnn_matrix[i][j] = dist_mi

    # Greedy Nearest Neighbor function
    def greedy_nearest_neighbor(gnn_matrix, start=0):
        """
        Purpose:
        Calculates fastest route between a set of points, minimizing travel distance.
        
        Arguments:
        gnn_matrix: matrix containing origins, destinations, and travel distances 
        start (default=0): starting index of the matrix
        """
        n = gnn_matrix.shape[0]
        visited = [False] * n
        route = [start] # State-specific coordinate
        visited[start] = True

        current = start
        for _ in range(n-1):
            # Find nearest unvisited park
            distances = gnn_matrix[current]
            nearest = None
            nearest_dist = float('inf')
            for i in range(n):
                if not visited[i] and distances[i] < nearest_dist:
                    nearest = i
                    nearest_dist = distances[i]

            route.append(nearest)
            visited[nearest] = True
            current = nearest

        if len(route) == 2:
            return route
        else: route.append(route)
    
    # Run greedy nearest neighbor algorithm with start=0 (home state)
    greedy_nearest_neighbor(gnn_matrix, start=0)

    # Load pre-processed park-to-park travel data from Google Maps
    travel_array_w = np.load('path/to/travel_array_w.npy', allow_pickle=True)

    # Append array generated from home to parks to array for parks to parks (previously generated)


    # Run greedy nearest neighbor algorithm with start as the first visited park (home state)
    greedy_nearest_neighbor(gnn_matrix, start=route[1])

    return route
