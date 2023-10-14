import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send an HTTP GET request to the website you want to scrape
url = "https://imageproperty.com.au/about-us/meet-the-team"
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the elements representing individual seller profiles
    seller_profiles = soup.find_all('div', class_='agent-profile-card')

    # Initialize a list to store seller data
    all_sellers_data = []

    for seller_profile in seller_profiles:
        # Extract agent details for each seller
        agent_name = seller_profile.find('h3', class_='mb-0').text
        agent_role = seller_profile.find('p', class_='mb-0').text

        phone_link = seller_profile.find('a', href=lambda x: x and x.startswith('tel:'))
        phone_number = phone_link.text if phone_link else None
        phone_href = phone_link['href'] if phone_link else None

        email_link = seller_profile.find('a', href=lambda x: x and x.startswith('mailto:'))
        email = email_link.text if email_link else None
        email_href = email_link['href'] if email_link else None

        # Extract the "VIEW PROFILE" link if it exists
        view_profile_link = seller_profile.find('a', class_='btn btn-sm d-block mt-3 btn-primary')
        view_profile_href = view_profile_link['href'] if view_profile_link else None

        # Append the seller data to the list
        seller_data = {
            'Agent Name': agent_name,
            'Agent Role': agent_role,
            'Phone Number': phone_number,
            'Phone Href': phone_href,
            'Email': email,
            'Email Href': email_href,
            'View Profile Link': view_profile_href
        }
        all_sellers_data.append(seller_data)

    # Create a DataFrame from the list of seller data
    sellers_df = pd.DataFrame(all_sellers_data)

    # Print the DataFrame
    print(sellers_df)

    # Save the DataFrame to a CSV file
    sellers_df.to_csv('all_sellers_data.csv', index=False)
    sellers_df.to_excel('all_sellers_data.xlsx', index=False)


else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
