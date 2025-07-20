import pandas as pd
import numpy as np
import googlemaps
import time
import os

def precompute_park_distances(parks_df, gmaps, dist_file='park_distance_matrix.npy', dur_file='park_duration_matrix.npy', names_file='park_names.npy'):
    """
    Precompute and save park-to-park distance and duration matrices if not already saved.
    """
    if os.path.exists(dist_file) and os.path.exists(dur_file) and os.path.exists(names_file):
        print("Loading precomputed park-to-park distance matrices...")
        distance_matrix = np.load(dist_file)
        duration_matrix = np.load(dur_file)
        park_names = np.load(names_file).tolist()
        return distance_matrix, duration_matrix, park_names

    print("Precomputing park-to-park distances (this may take several minutes)...")
    parks = parks_df['name'].tolist()
    coords = parks_df['coordinates'].tolist()
    n = len(parks)

    distance_matrix = np.zeros((n, n))
    duration_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if i == j:
                distance_matrix[i, j] = 0
                duration_matrix[i, j] = 0
            else:
                result = gmaps.distance_matrix(
                    origins=[coords[i]],
                    destinations=[coords[j]],
                    mode='driving',
                    units='imperial'
                )
                element = result['rows'][0]['elements'][0]
                if element['status'] == 'OK':
                    distance_matrix[i, j] = element['distance']['value'] / 1609.34  # meters to miles
                    duration_matrix[i, j] = element['duration']['value'] / 3600     # seconds to hours
                else:
                    distance_matrix[i, j] = np.inf
                    duration_matrix[i, j] = np.inf
                time.sleep(1)  # API rate limit safety

    np.save(dist_file, distance_matrix)
    np.save(dur_file, duration_matrix)
    np.save(names_file, np.array(parks))
    print("Precomputation done and saved.")
    return distance_matrix, duration_matrix, parks

def compute_home_to_parks(home_coord, parks_coords, gmaps):
    """
    Compute distances and durations from home to each park.
    """
    distances = []
    durations = []
    for dest in parks_coords:
        result = gmaps.distance_matrix(
            origins=[home_coord],
            destinations=[dest],
            mode='driving',
            units='imperial'
        )
        element = result['rows'][0]['elements'][0]
        if element['status'] == 'OK':
            distances.append(element['distance']['value'] / 1609.34)
            durations.append(element['duration']['value'] / 3600)
        else:
            distances.append(np.inf)
            durations.append(np.inf)
        time.sleep(1)  # API rate limit safety
    return distances, durations

def VacationRoute(home_state, states_file, parks_file, api_key):
    # Load data
    states_master = pd.read_csv(states_file)
    parks_w = pd.read_csv(parks_file)

    # Build coordinates tuples
    states_master['coordinates'] = list(zip(states_master['latitude'], states_master['longitude']))
    parks_w['coordinates'] = list(zip(parks_w['latitude'], parks_w['longitude']))

    # Find home coordinates
    home_coord = states_master.loc[states_master['abbreviation'] == home_state, 'coordinates'].values[0]

    # Initialize Google Maps client
    gmaps = googlemaps.Client(key=api_key)

    # Precompute or load park-to-park distance/duration matrices
    distance_matrix, duration_matrix, parks = precompute_park_distances(parks_w, gmaps)

    # Compute home → parks distances and durations
    home_to_parks_dist, home_to_parks_dur = compute_home_to_parks(home_coord, parks_w['coordinates'].tolist(), gmaps)

    visited = set()
    route_indices = []
    current_index = -1  # -1 means current location is home

    print(f"Starting from {home_state}.\nLeg-by-Leg Route with Distance and Time:\n")

    while len(visited) < len(parks):
        min_distance = float('inf')
        next_index = None
        next_duration = None

        for i in range(len(parks)):
            if i in visited:
                continue
            if current_index == -1:
                dist = home_to_parks_dist[i]
                dur = home_to_parks_dur[i]
            else:
                dist = distance_matrix[current_index, i]
                dur = duration_matrix[current_index, i]

            if dist < min_distance:
                min_distance = dist
                next_index = i
                next_duration = dur

        if next_index is None:
            print("No more reachable parks.")
            break

        # Print leg info
        from_loc = home_state if current_index == -1 else parks[current_index]
        to_loc = parks[next_index]
        print(f"{from_loc} → {to_loc} = {min_distance:.2f} mi ({next_duration:.2f} hrs)")

        visited.add(next_index)
        route_indices.append(next_index)
        current_index = next_index

    print("\nOptimal Roadtrip Route:")
    print("1.", home_state)
    for idx, park_i in enumerate(route_indices, start=2):
        print(f"{idx}. {parks[park_i]}")

    return [home_state] + [parks[i] for i in route_indices]

# === Example usage ===
# route = VacationRoute(
#     home_state='PA',
#     states_file='/path/to/states_master.csv',
#     parks_file='/path/to/parks_w.csv',
#     api_key='YOUR_REAL_API_KEY'
# )
# Define paths to your CSV files (update these paths to where your files actually are)
states_file = '/Users/priti/Documents/GitHub/Code-Jam/data/states_master.csv'
parks_file = '/Users/priti/Documents/GitHub/Code-Jam/data/parks_w.csv'

# Your Google Maps API key
api_key = 'AIzaSyBsZE5PsKrO7cQP1vUILx4j9HMCdPK3x_g'  # <-- Replace this with your actual Google API key

# Call the function with your chosen home state abbreviation, e.g. 'PA'
route = VacationRoute(
    home_state='PA',
    states_file=states_file,
    parks_file=parks_file,
    api_key=api_key
)

print("\nFinal route list:")
print(route)