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
    'location': [],
    'address': []
}

Url_Dict = {
    'Url':[]
}

# Start scraping from page 1
page_no = 1

while True:
    print(f'📄 Scraping page {page_no}...')
    page_url = f'https://www.zimbabweyp.com/category/retail_services/{page_no}.html'
    response = requests.get(page_url, headers=headers)

    if response.status_code != 200:
        print("❌ Page not found or error loading page.")
        break

    soup = BeautifulSoup(response.text, 'html.parser')
    Listings = soup.find_all('div', id='listings')


    # Stop if no listings found (end of results)
    if not Listings:
        print("✅ No more listings found. Ending scrape.")
        break

    for List in Listings:
        try:
            List_url = 'https://www.zimbabweyp.com/category/retail_services' + List.find('a')['href']
            response2 = requests.get(List_url, headers=headers)
            response2.encoding = 'utf-8'

            if response2.status_code != 200:
                print("❌ Page not found or error loading page.")
                break

            newsoup = BeautifulSoup(response2.text, 'html.parser')

            # Extract Name
            name = newsoup.find('section').h1.text.strip()
            List_dict['name'].append(name)
 

            print(name)
            print(List_url)
            print("Fetched URL:", response2.url)
            Url_Dict['Url'].append(List_url)
 
            #print(newsoup)

        except Exception as e:
            print(f"⚠️ Error on listing: {e}")
            continue

    # Go to the next page
    page_no += 1
    if page_no > 50:
        break

# Save to Excel
df = pd.DataFrame(Url_Dict)
df.to_excel('List.xlsx', index=False)
print("📘 Scraped data saved to 'Listk.xlsx'")
