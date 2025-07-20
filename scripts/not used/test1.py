import pandas as pd
import numpy as np
import googlemaps
import time
import os

def precompute_park_distances(parks_df, gmaps, dist_file='park_distance_matrix.npy', dur_file='park_duration_matrix.npy', names_file='park_names.npy'):
    if os.path.exists(dist_file) and os.path.exists(dur_file) and os.path.exists(names_file):
        print("Loading precomputed park-to-park distance matrices...")
        distance_matrix = np.load(dist_file)
        duration_matrix = np.load(dur_file)
        park_names = np.load(names_file, allow_pickle=True).tolist()
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
                    distance_matrix[i, j] = element['distance']['value'] / 1609.34
                    duration_matrix[i, j] = element['duration']['value'] / 3600
                else:
                    distance_matrix[i, j] = np.inf
                    duration_matrix[i, j] = np.inf
                time.sleep(1)

    np.save(dist_file, distance_matrix)
    np.save(dur_file, duration_matrix)
    np.save(names_file, np.array(parks))
    print("Precomputation done and saved.")
    return distance_matrix, duration_matrix, parks

def compute_home_to_parks(home_coord, parks_coords, gmaps):
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
        time.sleep(1)
    return np.array(distances), np.array(durations)

def VacationRouteWithSavedMatrix(home_state):
    # --- Hardcoded paths and API key ---
    states_file = '/Users/priti/Documents/GitHub/Code-Jam/data/states_master.csv'
    parks_file = '/Users/priti/Documents/GitHub/Code-Jam/data/parks_w.csv'
    api_key = 'YOUR_API_KEY_HERE'  # Replace with your actual key

    # --- Load and prepare data ---
    states_master = pd.read_csv(states_file)
    parks_w = pd.read_csv(parks_file)

    states_master['coordinates'] = list(zip(states_master['latitude'], states_master['longitude']))
    parks_w['coordinates'] = list(zip(parks_w['latitude'], parks_w['longitude']))

    home_coord = states_master.loc[states_master['abbreviation'] == home_state, 'coordinates'].values[0]

    gmaps = googlemaps.Client(key=api_key)

    # --- Load or compute park-to-park matrices ---
    distance_matrix, duration_matrix, parks = precompute_park_distances(parks_w, gmaps)

    # --- Compute home to all parks ---
    home_to_parks_dist, home_to_parks_dur = compute_home_to_parks(home_coord, parks_w['coordinates'].tolist(), gmaps)

    visited = set()
    route_indices = []
    current_index = -1  # Start from home

    legs_info = []

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

        from_loc = home_state if current_index == -1 else parks[current_index]
        to_loc = parks[next_index]
        print(f"{from_loc} → {to_loc} = {min_distance:.2f} mi ({next_duration:.2f} hrs)")

        legs_info.append({
            'source': from_loc,
            'destination': to_loc,
            'distance_miles': round(min_distance, 2),
            'duration_hours': round(next_duration, 2)
        })

        visited.add(next_index)
        route_indices.append(next_index)
        current_index = next_index

    print("\nOptimal Roadtrip Route:")
    print("1.", home_state)
    for idx, park_i in enumerate(route_indices, start=2):
        print(f"{idx}. {parks[park_i]}")

    # Return both the route legs and home-to-parks distances for plotting
    legs_df = pd.DataFrame(legs_info)
    home_distance_array = np.vstack((home_to_parks_dist, home_to_parks_dur)).T

    return legs_df, home_distance_array

# Example usage
legs_df, home_distance_array = VacationRouteWithSavedMatrix('PA')
print(legs_df)
