import scrapy
import json
import pandas as pd

class AshaSpider(scrapy.Spider):
    name = 'main'
    start_urls = ['https://platform.cloud.coveo.com/rest/search/v2?organizationId=americanspeechlanguagehearingassociationproductionh0xeoc4i']
    
    def parse(self, response):
        # Define the authorization token
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
            yield scrapy.Request(
                url=self.start_urls[0],
                headers=headers,
                method='GET',
                callback=self.parse_results,
                meta={'query_params': query_params, 'total_results': total_results.copy()}
            )
            page_number += 1  # Move to the next page

    def parse_results(self, response):
        query_params = response.meta['query_params']
        total_results = response.meta['total_results']

        # Check if the request was successful
        if response.status == 200:
            data = json.loads(response.text)

            # Extract the results part from the JSON response
            results = data.get("results", [])

            # Add the results from this page to the total results
            total_results.extend(results)

            # Check if there are more pages to retrieve
            if len(results) < query_params['numberOfResults']:
                df = pd.DataFrame(total_results)
                df.to_excel('asha_professionals.xlsx', index=False)
                self.log(f'Data exported to asha_professionals.xlsx')
            else:
                # Continue to the next page
                yield scrapy.Request(
                    url=self.start_urls[0],
                    headers=response.request.headers,
                    method='GET',
                    callback=self.parse_results,
                    meta={'query_params': query_params, 'total_results': total_results}
                )
        else:
            self.log(f'Failed to retrieve data. Status Code: {response.status}')

