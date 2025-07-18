# Available fields for each park
"""
id
url
*fullName
parkCode
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

API_KEY = "fpyJ9NycrgZX5mK8f0n90c4qXGPcYAsBPwt4BLJk"
url = "https://developer.nps.gov/api/v1/parks"

def fetch_all_parks(api_key):
    all_parks = []
    start = 0
    limit = 50

    while True:
        params = {
            "limit": limit,
            "start": start,
            "api_key": api_key,
            "fields": "amenities"
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
parks_raw = fetch_all_parks(API_KEY)

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
        'amenities': park.get('amenities', ''),
        'activities': ', '.join(activity_names)
    })

parks = pd.DataFrame(records)

# Save as CSV
parks.to_csv("../data/nps_parks_with_activities.csv", index=False)