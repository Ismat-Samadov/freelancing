import requests
import pandas as pd

# Define the API endpoint URL
url = "https://api.zap-map.com/v5/chargepoints/locations/placecards?id=73786"

# Define your API key
api_key = "4Yn23Fbs2DeJkZSRMq3gm5EbXhITZ5N9"

# Define the headers with the API key
headers = {
    "X-Api-Key": api_key,
    "Content-Type": "application/json",  # You may need to adjust this based on the API's requirements
}

# Make the GET request with the headers
response = requests.get(url, headers=headers)

# Check the response
if response.status_code == 200:
    # Request was successful, you can handle the response here
    print(response.json())
else:
    # Handle errors here, e.g., print the error message
    print(f"Request failed with status code {response.status_code}: {response.text}")

# Extract relevant data from the JSON response
data = response.json()['resources']['chargepoint_locations_placecards']['data']

# Create a list to store the extracted data
charging_points = []

# Iterate through the data and extract the desired information
for item in data:
    charging_point = {
        'Name of Charging Point': item['name'],
        'Type of Charging Point': ', '.join([connector['name'] for connector in item['connector_summary']]),
        'Number of Charging Points': item['total_device_count'],
        'Location of Charging Point': item['address_info']['formatted']
    }
    charging_points.append(charging_point)

# Create a DataFrame from the extracted data
df = pd.DataFrame(charging_points)

# Save the DataFrame to an Excel file
df.to_excel('charging_points2.xlsx', index=False)