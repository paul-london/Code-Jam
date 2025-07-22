import os
import folium
import pandas as pd
import numpy as np
import googlemaps

# Get absolute path to the repo root (assuming script is in /scripts/)
script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.abspath(os.path.join(script_dir, '..'))

# Build paths to CSVs in /data/ folder in the repo
states_file = os.path.join(repo_root, 'data', 'states_master.csv')
parks_file = os.path.join(repo_root, 'data', 'parks_subset.csv')

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
        #time.sleep(1)  # API rate limit safety
    return distances, durations

def VacationRoute(home_state, states_file, parks_file, api_key):
    states_master = pd.read_csv(states_file)
    parks_subset = pd.read_csv(parks_file)

    states_master['coordinates'] = list(zip(states_master['latitude'], states_master['longitude']))
    parks_subset['coordinates'] = list(zip(parks_subset['latitude'], parks_subset['longitude']))

    home_coord = states_master.loc[states_master['abbreviation'] == home_state, 'coordinates'].values[0]

    gmaps = googlemaps.Client(key=api_key)

    # distance_matrix, duration_matrix, parks = precompute_park_distances(parks_subset, gmaps)
    # Manual define from pre-calculcations
    travel_array_subset = np.load(os.path.join(repo_root, 'data', 'arrays', 'travel_array_subset.npy'), allow_pickle=True)
    distance_matrix = travel_array_subset[:, 2:3]
    duration_matrix = travel_array_subset[:, 3:4]
    
    # Get all unique parks (origins and destinations)
    all_parks = list(set(travel_array_subset[:, 0]) | set(travel_array_subset[:, 1]))
    all_parks.sort()  # keep consistent order

    # Map park names to indices
    park_indices = {park: idx for idx, park in enumerate(all_parks)}
    parks = all_parks

    n = len(all_parks)
    distance_matrix = np.full((n, n), np.inf)
    duration_matrix = np.full((n, n), np.inf)

    for row in travel_array_subset:
        origin, dest, dist, dur = row
        i = park_indices[origin]
        j = park_indices[dest]
        distance_matrix[i, j] = float(dist)
        duration_matrix[i, j] = float(dur)

    # Make sure order matches 'parks = all_parks'
    # Manually fixed coordinated from notebook
    park_coords_manual = {
    "Everglades National Park": (25.4686, -80.4776),
    "Fire Island National Seashore": (40.7551, -72.9878),
    "Zion National Park": (37.2594, -112.9507),
    }
    park_coords_ordered = []
    for park in parks:
        if park in park_coords_manual:
            park_coords_ordered.append(park_coords_manual[park])
        else:
            coord = parks_subset.loc[parks_subset['name'] == park, 'coordinates'].values[0]
            park_coords_ordered.append(coord)
            
    home_to_parks_dist, home_to_parks_dur = compute_home_to_parks(
        home_coord, park_coords_ordered, gmaps
        )

    visited = set()
    route_indices = []
    current_index = -1  # -1 means current location is home

    print(f"Starting from {home_state}.\nLeg-by-Leg Route with Distance and Time:\n")

    # Prepare list to collect route legs info for dataframe
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

        # Save leg info
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

    # Convert legs info to dataframe and return
    legs_df = pd.DataFrame(legs_info)
    print(legs_df)
    # Create JSON of parks_subset for SE
    legs_df.to_json((os.path.join(repo_root, 'db.json', 'legs_df.json')), orient='records', indent=2)
    return legs_df

def plot_route_on_map(parks_file, states_file, home_state, api_key='NA'):
    legs_df = VacationRoute(
        home_state=home_state,
        states_file=states_file,
        parks_file=parks_file,
        api_key=api_key
    )

    parks_df = pd.read_csv(parks_file)
    states_df = pd.read_csv(states_file)

    parks_df['coordinates'] = list(zip(parks_df['latitude'], parks_df['longitude']))
    states_df['coordinates'] = list(zip(states_df['latitude'], states_df['longitude']))

    home_coord = states_df.loc[
        states_df['abbreviation'] == home_state, ['latitude', 'longitude']
    ].values[0].tolist()

    route_map = folium.Map(location=home_coord, zoom_start=5)

    # Add home marker
    folium.Marker(
        location=home_coord,
        popup=f"Start: {home_state}",
        icon=folium.Icon(color='green', icon='home')
    ).add_to(route_map)

    # Draw routes and markers
    for i, (idx, row) in enumerate(legs_df.iterrows()):
        # Get source coordinates (from state or park)
        if row['source'] == home_state:
            source_coord = states_df.loc[
                states_df['abbreviation'] == home_state, ['latitude', 'longitude']
            ].values[0].tolist()
        else:
            source_coord = parks_df.loc[
                parks_df['name'] == row['source'], ['latitude', 'longitude']
            ].values[0].tolist()

        # Get destination coordinates
        dest_coord = parks_df.loc[
            parks_df['name'] == row['destination'], ['latitude', 'longitude']
        ].values[0].tolist()

        # Get description and image
        park_info = parks_df[parks_df['name'] == row['destination']].iloc[0]
        img_url = park_info['image_url']
        description = park_info['description']

        # Generate HTML for popup
        html = f"""
        <div style="width:220px">
        <h3 style="font-size:16px; margin-bottom:5px;">{row['destination']}</h3>
        <img src="{img_url}" width="200"><br><br>
        <em>{description}</em><br>
        </div>
        """

        # Add polyline for leg
        folium.PolyLine(
            locations=[source_coord, dest_coord],
            color='blue',
            weight=3,
            opacity=0.7,
            tooltip=f"{row['distance_miles']:.1f} mi ({row['duration_hours']:.1f} hrs)"
        ).add_to(route_map)

        # Add marker with flag if last stop
        icon = folium.Icon(color='red', icon='flag') if i == len(legs_df) - 1 else folium.Icon(color='blue', icon='info-sign')
        folium.Marker(
            location=dest_coord,
            popup=folium.Popup(html, max_width=250),
            icon=icon,
            tooltip=f"{row['destination']}"
        ).add_to(route_map)

    return route_map

if __name__ == "__main__":
    states_file = os.path.join(repo_root, 'data', 'states_master.csv')
    parks_file = os.path.join(repo_root, 'data', 'parks_subset.csv')
    home_state = 'PA'
    api_key = 'AIzaSyBsZE5PsKrO7cQP1vUILx4j9HMCdPK3x_g'


    route_map = plot_route_on_map(parks_file, states_file, home_state, api_key)
    route_map.save(os.path.join(repo_root, 'maps', 'usa_roadtrip_map.html'))
    print("✅ Map saved as 'usa_roadtrip_map.html'. Open it in your browser.")
