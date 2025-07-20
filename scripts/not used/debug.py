import ast
# Import required libraries
import pandas as pd
import numpy as np
import folium as fl
import time
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
# Assume states_master and parks_subset are already loaded as DataFrames

home_state = 'CA'

# Force coordinates column to tuples of floats
def force_tuple_floats(coord):
    if isinstance(coord, str):
        try:
            coord = ast.literal_eval(coord)
        except Exception as e:
            print(f"Error parsing coord string {coord}: {e}")
            raise
    if not (isinstance(coord, (tuple, list)) and len(coord) == 2):
        raise ValueError(f"Bad coord structure: {coord}")
    return tuple(map(float, coord))

states_master['coordinates'] = states_master['coordinates'].apply(force_tuple_floats)

home_state_coords = states_master.loc[states_master['abbreviation'] == home_state, 'coordinates'].values[0]
print(f"Home state coords: {home_state_coords} (type: {type(home_state_coords)})")

parks_subset_gnn = parks_subset[['name', 'latitude', 'longitude']].reset_index(drop=True)
home_state_row = [home_state, float(home_state_coords[0]), float(home_state_coords[1])]
home_state_df = pd.DataFrame([home_state_row], columns=['name', 'latitude', 'longitude'])
parks_subset_gnn_with_origin = pd.concat([home_state_df, parks_subset_gnn], ignore_index=True)

origin_home = {
    parks_subset_gnn_with_origin.loc[0, 'name']: 
    (float(parks_subset_gnn_with_origin.loc[0, 'latitude']), float(parks_subset_gnn_with_origin.loc[0, 'longitude']))
}

destinations = {
    parks_subset_gnn_with_origin.loc[i, 'name']: 
    (float(parks_subset_gnn_with_origin.loc[i, 'latitude']), float(parks_subset_gnn_with_origin.loc[i, 'longitude']))
    for i in range(1, len(parks_subset_gnn_with_origin))
}

print(f"Origin home sample: {origin_home}")
print(f"Destinations sample: {list(destinations.items())[:3]}")

# Now, try a single API call with first origin and first destination to isolate error
origin_coords = list(origin_home.values())[0]
dest_coords = list(destinations.values())[0]
print(f"Calling gmaps.distance_matrix with origin: {origin_coords}, destination: {dest_coords}")

result = gmaps.distance_matrix(
    origins=[origin_coords],
    destinations=[dest_coords],
    mode='driving'
)
print("API call success. Result snippet:")
print(result['rows'][0]['elements'][0])
