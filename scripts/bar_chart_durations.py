import os
import matplotlib.pyplot as plt
from map import VacationRoute  # Make sure test4.py is accessible or rename appropriately

# Get absolute path to the repo root (assuming script is in /scripts/)
script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.abspath(os.path.join(script_dir, '..'))

# Build paths to CSVs in /data/ folder in the repo
states_file = os.path.join(repo_root, 'data', 'states_master.csv')
parks_file = os.path.join(repo_root, 'data', 'parks_w.csv')

def plot_duration_barchart(legs_df):
    # Create route label for each leg
    legs_df['route'] = legs_df['source'] + " → " + legs_df['destination']

    # Create horizontal bar chart with log-scaled x-axis
    plt.figure(figsize=(12, 8))
    plt.barh(legs_df['route'], legs_df['duration_hours'], color='skyblue')
    plt.xscale('linear')
    plt.xlabel('Duration (hours)')
    plt.title('Travel Durations Between Route Legs')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    legs_df = VacationRoute(
        home_state='CA',
        states_file = os.path.join(repo_root, 'data', 'states_master.csv'),
        parks_file = os.path.join(repo_root, 'data', 'parks_w.csv'),
        api_key='AIzaSyBsZE5PsKrO7cQP1vUILx4j9HMCdPK3x_g'
    )

    plot_duration_barchart(legs_df)
    print(legs_df[['source', 'destination', 'duration_hours']])