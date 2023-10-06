import scrapy
import json

class AshaSpider(scrapy.Spider):
    name = 'asha_spider'
    start_urls = ['https://platform.cloud.coveo.com/rest/search/v2?organizationId=americanspeechlanguagehearingassociationproductionh0xeoc4i']
    
    def parse(self, response):
        # Define the headers and other settings as before
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
        page_number = 1
        results_per_page = 10

        while True:
            query_params = {
                'firstResult': (page_number - 1) * results_per_page,
                'numberOfResults': results_per_page,
            }

            yield scrapy.Request(
                url=self.start_urls[0],
                headers=headers,
                method='GET',
                callback=self.parse_results,
                meta={'query_params': query_params}
            )
            page_number += 1

    def parse_results(self, response):
        query_params = response.meta['query_params']

        if response.status == 200:
            data = json.loads(response.text)
            results = data.get("results", [])

            for result in results:
                click_uri = result.get("ClickUri")
                yield {
                    'ClickUri': click_uri
                }

            if len(results) < query_params['numberOfResults']:
                self.log('Data extraction completed.')
            else:
                yield scrapy.Request(
                    url=self.start_urls[0],
                    headers=response.request.headers,
                    method='GET',
                    callback=self.parse_results,
                    meta={'query_params': query_params}
                )
        else:
            self.log(f'Failed to retrieve data. Status Code: {response.status}')
