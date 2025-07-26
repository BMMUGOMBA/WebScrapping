import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
import os

# Headers to mimic a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

# File setup
script_dir = os.path.dirname(os.path.abspath(__file__))
image_links_file = os.path.join(script_dir, "image_links.txt")

# Clear image links file
with open(image_links_file, 'w') as f:
    pass

# Dictionary to store listing data
List_dict = {
    'name': [],
    'category': [],
    'address': []
}

Url_Dict = {
    'Url':[]
}

# Start scraping from page 1
page_no = 1

while page_no < 3:
    print(f'📄 Scraping page {page_no}...')
    page_url = f'https://www.zimbabweyp.com/category/retail_services/{page_no}.html'
    response = requests.get(page_url, headers=headers)

    if response.status_code != 200:
        print("❌ Page not found or error loading page.")
        break

    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all company blocks
    companies = soup.find_all('div', class_='company with_img g_0')
    #print(companies)

    for company in companies:
        try:
            # Extract company name
            name_tag = company.find('h3')
            name = name_tag.get_text(strip=True) if name_tag else 'N/A'

            # Extract address
            address_tag = company.find('div', class_='address')
            address = address_tag.get_text(separator=' ', strip=True) if address_tag else 'N/A'

            print(f"🏢 Name: {name}")
            print(f"📍 Address: {address}")
            print('---')

            # Extract path: '/category/retail_services/1.html'
            path = (page_url)

            # Get category (i.e., second element in split path)
            category = path.split('/')[2]  # index 0: '', 1: 'category', 2: 'retail_services'

            # Append to dictionary
            List_dict['name'].append(name)
            List_dict['address'].append(address)
            List_dict['category'].append(category)

        except Exception as e:
            print(f"⚠️ Error extracting data: {e}")
            continue
    # Go to the next page
    page_no += 1
    if page_no > 50:
        break

# Save to Excel
df = pd.DataFrame(List_dict)
df.to_excel('List.xlsx', index=False)
print("📘 Scraped data saved to 'Listk.xlsx'")