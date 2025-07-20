import os
import folium
import pandas as pd
import numpy as np
import googlemaps

# Get absolute path to the repo root (assuming script is in /scripts/)
script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.abspath(os.path.join(script_dir, '..'))

# Build paths to CSVs and .npy file
states_file = os.path.join(repo_root, 'data', 'states_master.csv')
parks_file = os.path.join(repo_root, 'data', 'parks_w.csv')
arrays_file = os.path.join(repo_root, 'data', 'arrays', 'travel_array_w.npy')

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
            distances.append(element['distance']['value'] / 1609.34)  # meters to miles
            durations.append(element['duration']['value'] / 3600)     # seconds to hours
        else:
            distances.append(np.inf)
            durations.append(np.inf)
    return distances, durations

def VacationRoute(home_state, states_file, parks_file, api_key):
    states_master = pd.read_csv(states_file)
    parks_w = pd.read_csv(parks_file)

    states_master['coordinates'] = list(zip(states_master['latitude'], states_master['longitude']))
    parks_w['coordinates'] = list(zip(parks_w['latitude'], parks_w['longitude']))

    home_coord = states_master.loc[states_master['abbreviation'] == home_state, 'coordinates'].values[0]

    gmaps = googlemaps.Client(key=api_key)

    # Load precomputed distance and duration matrix
    travel_array_w = np.load(arrays_file, allow_pickle=True)
    
    all_parks = list(set(travel_array_w[:, 0]) | set(travel_array_w[:, 1]))
    all_parks.sort()

    park_indices = {park: idx for idx, park in enumerate(all_parks)}
    parks = all_parks

    n = len(parks)
    distance_matrix = np.full((n, n), np.inf)
    duration_matrix = np.full((n, n), np.inf)

    for row in travel_array_w:
        origin, dest, dist, dur = row
        i = park_indices[origin]
        j = park_indices[dest]
        distance_matrix[i, j] = float(dist)
        duration_matrix[i, j] = float(dur)

    park_coords_ordered = [
        parks_w.loc[parks_w['name'] == park, 'coordinates'].values[0] for park in parks
    ]
    home_to_parks_dist, home_to_parks_dur = compute_home_to_parks(
        home_coord, park_coords_ordered, gmaps
    )

    visited = set()
    route_indices = []
    current_index = -1

    print(f"Starting from {home_state}.\nLeg-by-Leg Route with Distance and Time:\n")
    legs_info = []

    while len(visited) < len(parks):
        min_distance = float('inf')
        next_index = None
        next_duration = None

        for i in range(len(parks)):
            if i in visited:
                continue
            dist = home_to_parks_dist[i] if current_index == -1 else distance_matrix[current_index, i]
            dur = home_to_parks_dur[i] if current_index == -1 else duration_matrix[current_index, i]

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

    legs_df = pd.DataFrame(legs_info)
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

    folium.Marker(
        location=home_coord,
        popup=f"Start: {home_state}",
        icon=folium.Icon(color='green', icon='home')
    ).add_to(route_map)

    for i, (idx, row) in enumerate(legs_df.iterrows()):
        if row['source'] == home_state:
            source_coord = states_df.loc[
                states_df['abbreviation'] == home_state, ['latitude', 'longitude']
            ].values[0].tolist()
        else:
            source_coord = parks_df.loc[
                parks_df['name'] == row['source'], ['latitude', 'longitude']
            ].values[0].tolist()

        dest_coord = parks_df.loc[
            parks_df['name'] == row['destination'], ['latitude', 'longitude']
        ].values[0].tolist()

        park_info = parks_df[parks_df['name'] == row['destination']].iloc[0]
        img_url = park_info['image_url']
        description = park_info['description']

        html = f"""
        <div style="width:220px">
        <h3 style="font-size:16px; margin-bottom:5px;">{row['destination']}</h3>
        <img src="{img_url}" width="200"><br>
        <em>{description}</em><br>
        </div>
        """

        folium.PolyLine(
            locations=[source_coord, dest_coord],
            color='blue',
            weight=3,
            opacity=0.7,
            tooltip=f"{row['distance_miles']:.1f} mi ({row['duration_hours']:.1f} hrs)"
        ).add_to(route_map)

        icon = folium.Icon(color='red', icon='flag') if i == len(legs_df) - 1 else folium.Icon(color='blue', icon='info-sign')
        folium.Marker(
            location=dest_coord,
            popup=folium.Popup(html, max_width=250),
            icon=icon,
            tooltip=f"{row['destination']}"
        ).add_to(route_map)

    return route_map

if __name__ == "__main__":
    home_state = 'NY'  # You can change this to any US state abbreviation
    api_key = 'AIzaSyBsZE5PsKrO7cQP1vUILx4j9HMCdPK3x_g'

    route_map = plot_route_on_map(parks_file, states_file, home_state, api_key)
    route_map.save("usa_roadtrip_map.html")
    print("✅ Map saved as 'usa_roadtrip_map.html'. Open it in your browser.")
