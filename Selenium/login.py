#Creating Driver and opening driver
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://quotes.toscrape.com/js/'

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

options.add_experimental_option( name='detach',value=True)

driver = webdriver.Chrome(options=options)
driver.get(url)

login_button = driver.find_element(By.XPATH, value='//a[text()="Login"]')
login_button.click()

username_input = driver.find_element(By.ID, value='username')
username_input.send_keys('myusername')

password_input = driver.find_element(By.ID, value='password')
password_input.send_keys('123456')

log_me_in = driver.find_element(By.CSS_SELECTOR, value = 'input[value = "Login"]')
log_me_in.click()
