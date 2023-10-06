import json
import requests
import pandas as pd

# Define the API URL and your authorization token
url = 'https://platform.cloud.coveo.com/rest/search/v2?organizationId=americanspeechlanguagehearingassociationproductionh0xeoc4i'
authorization_token = 'Bearer xxee022e66-e168-47e9-8f83-d77df9a3cae0'

# Define the headers
headers = {
    'Authorization': authorization_token,
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,ru;q=0.7,az;q=0.6',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Dnt': '1',
    'Origin': 'https://find.asha.org',
    'Referer': 'https://find.asha.org/',
    'Sec-Ch-Ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

# Initialize variables for pagination
page_number = 1  # Start with the first page
results_per_page = 10  # Adjust the number of results per page as needed
total_results = []  # To store all results

while True:
    # Define query parameters for pagination
    query_params = {
        'firstResult': (page_number - 1) * results_per_page,
        'numberOfResults': results_per_page,
        # Add other query parameters as needed
    }

    # Make an HTTP GET request to the API with pagination parameters
    response = requests.get(url, headers=headers, params=query_params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Extract the results part from the JSON response
        results = data.get("results", [])

        # Add the results from this page to the total results
        total_results.extend(results)

        # Check if there are more pages to retrieve
        if len(results) < results_per_page:
            break  # No more results to fetch
        else:
            page_number += 1  # Move to the next page
    else:
        print(f"Failed to retrieve data for page {page_number}. Status Code: {response.status_code}")
        break

# Create a DataFrame from the total results
df = pd.DataFrame(total_results)

# Define the path where you want to save the Excel file
excel_file_path = 'asha_professionals.xlsx'

# Export the DataFrame to an Excel file
df.to_excel(excel_file_path, index=False)

print(f"Data exported to {excel_file_path}")
