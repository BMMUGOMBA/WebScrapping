#Creating Driver and opening driver
from selenium import webdriver

url = 'https://quotes.toscrape.com/js/'

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option( name='detach',value=True)
options.add_experimental_option( name='detach',value=True)

driver = webdriver.Chrome(options=options)
driver.get(url)