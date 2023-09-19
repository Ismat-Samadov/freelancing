import aiohttp
import asyncio
import pandas as pd

# Define your range of location IDs
start_location_id = 100000
end_location_id = 500000

# Define your API key
api_key = "4Yn23Fbs2DeJkZSRMq3gm5EbXhITZ5N9"

# Define the headers with the API key
headers = {
    "X-Api-Key": api_key,
    "Content-Type": "application/json",  # You may need to adjust this based on the API's requirements
}

# Create an empty list to store all charging point data
all_charging_points = []

# Maximum number of retries
max_retries = 3


async def fetch_data(session, location_id):
    url = f"https://api.zap-map.com/v5/chargepoints/locations/placecards?id={location_id}"

    # Set a longer timeout for the request (e.g., 60 seconds)
    timeout = aiohttp.ClientTimeout(total=60)

    for retry_count in range(max_retries):
        try:
            async with session.get(url, headers=headers, timeout=timeout) as response:
                if response.status == 200:
                    data = await response.json()
                    charging_points = []
                    for item in data['resources']['chargepoint_locations_placecards']['data']:
                        charging_point = {
                            'Location ID': location_id,
                            'Name of Charging Point': item['name'],
                            'Type of Charging Point': ', '.join(
                                [connector['name'] for connector in item['connector_summary']]),
                            'Number of Charging Points': item['total_device_count'],
                            'Location of Charging Point': item['address_info']['formatted']
                        }
                        charging_points.append(charging_point)

                    all_charging_points.extend(charging_points)
                else:
                    print(f"Request failed for location ID {location_id} with status code {response.status}")
        except asyncio.TimeoutError:
            print(f"Request timed out for location ID {location_id}. Retrying ({retry_count + 1}/{max_retries})...")
            continue
        else:
            break


async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for location_id in range(start_location_id, end_location_id + 1):
            task = asyncio.ensure_future(fetch_data(session, location_id))
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    # Create a DataFrame from all the extracted data
    df = pd.DataFrame(all_charging_points)

    # Save the DataFrame to an Excel file
    df.to_excel('charging_points_large_range_async_with_retry.xlsx', index=False)
