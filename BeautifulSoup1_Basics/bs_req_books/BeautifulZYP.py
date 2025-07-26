import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
import os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, "image_links.txt")

with open('image_links.txt', 'w') as f:
    pass

List_dict = {
    'name': [],
    'category': [],
     'location': [],
    'address': []
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}

number_dict = {'One': '1', 'Two': '2', 'Three': '3', 'Four': '4', 'Five': '5'}

url = 'https://www.zimbabweyp.com/'
response = requests.get(url, headers=headers)
page_html = response.text
soup = BeautifulSoup(page_html, 'html.parser')

#page_count_string = soup.find('li', class_='current').text
#page_count = int(page_count_string.strip().split(' ')[-1])

#for page_no in range(1, page_count + 1):
page_no = 1
while True:
    print(f'page--> {page_no}')
    page_url = f'https://www.zimbabweyp.com/category/retail_services{page_no}.html'
    response = requests.get(page_url, headers=headers)
    page_html = response.text
    soup = BeautifulSoup(page_html,'html.parser')
    Listings = soup.find_all('div', class_='listings')

    for List in Listings:
        #book_url = 'https://books.toscrape.com/catalogue/' + book.find('a')['href']
        List_url = 'https://www.zimbabweyp.com/category/retail_services' + List.find('a')['href']
        response = requests.get(List_url, headers=headers)
        response.encoding = 'utf-8'

        soup = BeautifulSoup(response.text, 'html.parser')

        name = soup.find('div', class_='tp scroller').h1.text
        List_dict['name'].append(name)

        address = soup.find('div', class_='text location').text
        List_dict['address'].append(name)

        #category = soup.find('div', class_='product_main').p.text
        #book_dict['price'].append(price)

        ul_container = soup.find('ul', itemtype='https://schema.org/BreadcrumbList')
        li_items = ul_container.find_all('li')
        category = li_items[2].a.text
        List_dict['location'].append(category)

        ul_container = soup.find('ul', itemtype='https://schema.org/BreadcrumbList')
        li_items = ul_container.find_all('li')
        category = li_items[3].a.text
        List_dict['category'].append(category)


df = pd.DataFrame(List_dict)
df.to_excel('Listings.xlsx')

