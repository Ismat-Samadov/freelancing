import requests
from bs4 import BeautifulSoup

def scrape_product_data(urls):
    all_product_data = []  # List to store data for all URLs
    
    for url in urls:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the product title element with the specified class
            product_title = soup.find('h1', class_='product_title')

            # Find the price element with the specified class
            price_element = soup.find('p', class_='price')

            # Find the availability element
            availability_element = soup.find('p', class_='ast-stock-detail')
            
            if availability_element:
                availability_text = availability_element.find('span', class_='stock').get_text()
            else:
                availability_text = "Out of stock"  # Assume out of stock if availability element not found

            # Extract the product title and price text
            if product_title and price_element:
                product_title_text = product_title.get_text()
                price_text = price_element.find('bdi').get_text()
            else:
                product_title_text = "Product title not found"
                price_text = "Price not found"

            # Create a list containing the extracted data for this URL
            data = [url,product_title_text, price_text, availability_text]
            
            all_product_data.append(data)
        else:
            all_product_data.append(["Failed to retrieve the webpage. Status code: " + str(response.status_code)])

    return all_product_data

# Example usage:
urls = [
    "https://www.amtcomposites.co.za/product/necuron-651-50mm-1500mm-x-500mm/",
    "https://www.amtcomposites.co.za/product/necuron-651-25mm-1500mm-x-500mm/",
    "https://www.amtcomposites.co.za/product/necuron-540-50mm-1500mm-x-500mm/"
]

product_data = scrape_product_data(urls)
for data in product_data:
    print(data)
