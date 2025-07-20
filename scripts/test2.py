import pandas as pd
import googlemaps
import time

# === Load data ===
states_master = pd.read_csv('/Users/priti/Documents/GitHub/Code-Jam/data/states_master.csv')
parks_w = pd.read_csv('/Users/priti/Documents/GitHub/Code-Jam/data/parks_w.csv')

# Create coordinate tuples for states and parks
states_master['coordinates'] = list(zip(states_master['latitude'], states_master['longitude']))
parks_w['coordinates'] = list(zip(parks_w['latitude'], parks_w['longitude']))

# Define start state abbreviation
start_state = 'PA'

# Get home coordinates for start state
origin_home = states_master.loc[states_master['abbreviation'] == start_state, 'coordinates'].values[0]

# Initialize Google Maps client — replace with your real API key
gmaps = googlemaps.Client(key='AIzaSyBsZE5PsKrO7cQP1vUILx4j9HMCdPK3x_g')

visited = set()
route = []
current_location = origin_home

print("Leg-by-Leg Route with Distance and Time:\n")

while len(visited) < len(parks_w):
    min_distance = float('inf')
    nearest_park = None
    nearest_info = None

    for idx, row in parks_w.iterrows():
        park_name = row['name']
        if park_name in visited:
            continue

        dest_coords = row['coordinates']

        try:
            result = gmaps.distance_matrix(
                origins=[current_location],
                destinations=[dest_coords],
                mode="driving",
                units="imperial"
            )
            element = result['rows'][0]['elements'][0]
            if element['status'] != 'OK':
                continue

            distance_mi = element['distance']['value'] / 1609.34
            duration_hr = element['duration']['value'] / 3600

            if distance_mi < min_distance:
                min_distance = distance_mi
                nearest_park = park_name
                nearest_info = (distance_mi, duration_hr, dest_coords)

        except Exception as e:
            print(f"Skipping {park_name} due to error: {e}")
            continue

        time.sleep(1)  # To avoid Google API rate limit

    if nearest_park is None:
        print("No more reachable parks.")
        break

    prev_location = route[-1] if route else start_state
    print(f"{prev_location} → {nearest_park} = {nearest_info[0]:.2f} mi ({nearest_info[1]:.2f} hrs)")

    visited.add(nearest_park)
    route.append(nearest_park)
    current_location = nearest_info[2]

print("\nOptimal Roadtrip Route:")
print("1.", start_state)
for i, park in enumerate(route, start=2):
    print(f"{i}. {park}")
