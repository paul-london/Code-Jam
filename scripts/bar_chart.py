import matplotlib.pyplot as plt
from test4 import VacationRoute

def plot_distance_barchart(legs_df):
    legs_df['route'] = legs_df['source'] + " → " + legs_df['destination']

    plt.figure(figsize=(12, 8))
    plt.barh(legs_df['route'], legs_df['distance_miles'], color='skyblue')
    plt.xscale('log')
    plt.xlabel('Distance (miles) [Log Scale]')
    plt.title('Distances Between Route Legs')
    plt.tight_layout()
    plt.show()
    legs_df['route'] = legs_df['source'] + " → " + legs_df['destination']
'''
    plt.figure(figsize=(12, 6))
    plt.bar(legs_df['route'], legs_df['distance_miles'], color='skyblue')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Distance (miles)')
    plt.title('Distances Between Each Route Leg')
    plt.tight_layout()
    plt.show()
    

legs_df['route'] = legs_df['source'] + " → " + legs_df['destination']

plt.figure(figsize=(12, 8))
plt.barh(legs_df['route'], legs_df['distance_miles'], color='skyblue')
plt.xscale('log')
plt.xlabel('Distance (miles) [Log Scale]')
plt.title('Distances Between Route Legs')
plt.tight_layout()
plt.show()

'''
if __name__ == "__main__":
    # Call VacationRoute to get the legs dataframe
    legs_df = VacationRoute(
        home_state='PA',
        states_file='/Users/priti/Documents/GitHub/Code-Jam/data/states_master.csv',
        parks_file='/Users/priti/Documents/GitHub/Code-Jam/data/parks_w.csv',
        api_key='AIzaSyBsZE5PsKrO7cQP1vUILx4j9HMCdPK3x_g'
    )

    plot_distance_barchart(legs_df)
