import folium
import os

def generate_blank_us_map(output_file='blank_us_map.html'):
    """
    Purpose:
    Generates a blank Folium map centered on the United States and saves it to an HTML file.

    Parameters:
    - output_file: Filename to save the HTML map
    """
    # Get directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct path to ../maps/ from the script's location
    maps_dir = os.path.abspath(os.path.join(script_dir, '..', 'maps'))
    os.makedirs(maps_dir, exist_ok=True)  # Ensure the directory exists

    # Centered on the geographic center of the continental US
    m = folium.Map(location=[39.8283, -98.5795], zoom_start=4)

    # Save map
    output_path = os.path.join(maps_dir, output_file)
    m.save(output_path)
    print(f"Blank US map saved to: {output_path}")

# Call the function
if __name__ == '__main__':
    generate_blank_us_map()
