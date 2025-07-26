import requests
from  bs4 import BeautifulSoup

number_dict = {'One':1,'Two':1,'Three':3,'Four':4,'Five':5}

book_url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

response = requests.get(book_url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text,'html.parser')

#price, category, stars, upc, availability, in_stock, image_link

name = soup.find('div', class_ ='product_main').h1.text
print(name)

price = soup.find('div', class_ = 'product_main').p.text
print(price)
