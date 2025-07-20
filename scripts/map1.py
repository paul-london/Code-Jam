import folium
import pandas as pd
from test4 import VacationRoute

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

    for _, row in legs_df.iterrows():
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

        folium.PolyLine(
            locations=[source_coord, dest_coord],
            color='blue',
            weight=3,
            opacity=0.7
        ).add_to(route_map)

        folium.Marker(
            location=dest_coord,
            popup=folium.Popup(
                f"{row['destination']}<br>{row['distance_miles']:.1f} mi, {row['duration_hours']:.1f} hrs",
                max_width=250
            ),
            icon=folium.Icon(color='red', icon='flag')
        ).add_to(route_map)

    return route_map

if __name__ == "__main__":
    parks_file = '../data/parks_w.csv'
    states_file = '../data/states_master.csv'
    home_state = 'PA'
    api_key ='AIzaSyBsZE5PsKrO7cQP1vUILx4j9HMCdPK3x_g'


    route_map = plot_route_on_map(parks_file, states_file, home_state, api_key)
    route_map.save("usa_roadtrip_map.html")
    print("✅ Map saved as 'usa_roadtrip_map.html'. Open it in your browser.")
