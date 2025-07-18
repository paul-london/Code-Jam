# Available fields for each park
"""
id
url
*fullName
*parkCode (only needed for amenities)
name
*description
*designation
*latitude
*longitude
latLong (combined "lat:..., long:...")
*activities (array of objects with id and name)
*amenities
topics
*states
contacts (e.g., phone, email)
entranceFees (array)
entrancePasses
fees
directionsInfo
directionsUrl
operatingHours
addresses
images (photos array)
weatherInfo
"""

# Import requests for JSON and pandas
import requests
import pandas as pd
import time

api_key = "fpyJ9NycrgZX5mK8f0n90c4qXGPcYAsBPwt4BLJk"
url = "https://developer.nps.gov/api/v1/parks"

def fetch_all_parks(api_key):
    """
    Gets information from NPS about National Parks.
    """
    all_parks = []
    start = 0
    limit = 50

    while True:
        params = {
            "limit": limit,
            "start": start,
            "api_key": api_key,
        }

        response = requests.get(url, params=params)
        response.raise_for_status()  # raise error for bad response
        data = response.json().get("data", [])

        if not data:
            break  # no more data

        all_parks.extend(data)
        start += limit  # go to next page

    return all_parks

# Fetch data
parks_raw = fetch_all_parks(api_key)

# Convert to DataFrame
records = []
for park in parks_raw:
    activity_list = park.get('activities', [])
    activity_names = [a.get('name', '') for a in activity_list]
    
    records.append({
        'name': park.get('fullName', ''),
        'latitude': park.get('latitude', ''),
        'longitude': park.get('longitude', ''),
        'designation': park.get('designation', ''),
        'states': park.get('states', ''),
        'description': park.get('description', ''),
        'activities': ', '.join(activity_names),
        'parkCode': park.get('parkCode', '')
    })

parks = pd.DataFrame(records)

# Get park amenities by park code
def get_amenities_by_park(park_code, api_key):
    """
    Gets list of amenity names for a specific park by its parkCode.
    """
    url = "https://developer.nps.gov/api/v1/amenities/parksplaces"
    params = {
        "parkCode": park_code,
        "api_key": api_key
    }
    try:
        res = requests.get(url, params=params)
        res.raise_for_status()
        data = res.json().get("data", [])
        print(f"Raw data for {park_code}: {data}")  # Debug
        if data and isinstance(data[0], list):
            amenities_list = data[0]
        else:
            amenities_list = []
        print(f"Amenities list: {amenities_list}")  # Debug
        amenity_names = [amenity['name'] for amenity in amenities_list]
        return ', '.join(amenity_names)
    except Exception as e:
        print(f"Error for park {park_code}: {e}")
        return ""

# Add amenities to dataframe
parks['amenities'] = parks['parkCode'].apply(lambda code: (time.sleep(0.5), get_amenities_by_park(code, api_key))[1])

# Drop parkCode column
parks.drop(columns=['parkCode'], inplace=True)

# Save as CSV
parks.to_csv("../data/parks.csv", index=False)