import requests
from bs4 import BeautifulSoup

# Your Scraper API key
API_KEY = 'aa2ac9ebbc1f94b34aeed2c479937499'

def get_product_links(url):
    product_links = []  # Create an empty list to store the product URLs

    # Construct the Scraper API URL
    scraper_api_url = f'https://api.scraperapi.com?api_key={API_KEY}&url={url}'

    # Send an HTTP GET request to the Scraper API URL
    response = requests.get(scraper_api_url)

    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all 'a' elements within the specified class
        product_links = [a['href'] for a in soup.select('li.product a.woocommerce-LoopProduct-link')]
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

    return product_links

# Example usage of the function
url = "https://www.amtcomposites.co.za/product-category/tooling-modelling-board/"
product_links = get_product_links(url)

# Print the extracted product URLs
for link in product_links:
    print(link)
