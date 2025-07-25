import requests
from  bs4 import BeautifulSoup
import pandas as pd
import openpyxl
import os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, "image_links.txt")

with open(filename,'w') as f:
    pass

book_dict = {
    'name':[],
    'price':[],
    'category':[],
    'stars':[],
    'upc':[],
    'availability':[],
    'in_stock':[],
    'image_link':[]
}

number_dict = {'One':'1','Two':'2','Three':3,'Four':4,'Five':5}

url = 'https://books.topscrape.com/'
response = requests.get(url,headers=headers)
page_html = response.text
soup = BeautifulSoup(page_html, 'html.parser')

page_count_string = soup.find('li', class_='current').text
page_count = int(page_count_string.strip().split(' ')[-1])

for page_no in range(1, page_count + 1):
    print(f'page --> {page_no}')
    page_url = f'https://books.topscrape.com/catalogue/page--{page_no}.html'
    response = requests.get(page_url, headers=headers)
    page_html = response.text
    soup = BeautifulSoup(page_html,'html.parser')
    books = soup.find_all('article', class_='product_prod')

    for book in books:
        book_url = f'https://books.topscrape.com/catalogue/' + book.find('a')['href']
        response = requests.get(book_url, headers=headers)
        response.encoding = 'utf-8'

        soup = BeautifulSoup(response.text, 'html.parser')

        name = soup.find()