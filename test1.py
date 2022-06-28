from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

products=[] #List to store name of the product
prices=[] #List to store price of the product

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.listing.com.pk/listing/")
driver.implicitly_wait(10)
# driver.find_element(By.XPATH, "//input[contains(@id,'search')]").send_keys("Samsung Phones")
# driver.find_element(By.XPATH, "//span[text()='Samsung']").click()
phonenames = driver.find_elements(By.XPATH, "//h2[contains(@class,' entry-title')]")
rates = driver.find_elements(By.XPATH, "//p[contains(@class,'phone')]")

for phone in phonenames:
    products.append(phone.text)

print("*"*58)

for rate in rates:
    prices.append(rate.text)

a = {'Product Name':products,'Price':prices}
df = pd.DataFrame.from_dict(a, orient='index')
df.to_csv('products.csv', index=False, encoding='utf-8')

# df = pd.DataFrame({'Product Name':phonenames,'Price':prices}) 
# df.to_csv('products.csv', index=False, encoding='utf-8')

driver.quit()