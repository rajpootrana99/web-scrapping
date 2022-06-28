import string
from time import sleep, time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from socket import timeout

driver = webdriver.Chrome()

names=[] #List to store name of the agent
phones1=[] #List to store number of the agent
phones2=[]
for x in range(2):
    if x == 0: continue
    url = "https://www.zameen.com/Plots/Islamabad_DHA_Defence-3188-" + str(x) + ".html"
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")
    for a in soup.findAll('li', attrs={'class':'ef447dde'}):
        link=a.find('a', attrs={'class':'_7ac32433'}).get("href")
        driver.get("https://www.zameen.com/"+link)
        # call_btn = driver.find_element(By.CLASS_NAME, "_5b77d672")
        call_btn = driver.find_element(By.XPATH, "//button[@class='_5b77d672 da62f2ae _8a1d083b']")
        # driver.find_element(By.XPATH, "//button[text()='Call']").click()
        # print(call_btn)
        # //button[@class='_5b77d672 da62f2ae _8a1d083b']
        # button[class='_5b77d672 da62f2ae _8a1d083b']
        # call_btn = driver.find_element_by_css_selector("button._8a1d083b")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(call_btn))
        # driver.execute_script("return arguments[0].scrollIntoView(true);", call_btn)
        # driver.implicitly_wait(10)
        ActionChains(driver).move_to_element(call_btn).click().perform()
        # sleep(10)
        # print(call_btn)
        name=a.find('span', attrs={'class':'f2186d94'})
        print(name)
        break
        # phone1=a.find('a', attrs={'class':'_3bb2d41a'}).get("href")
        # phone2=a.find('a', attrs={'class':'_3bb2d41a'}).get("href")
        # names.append("" if name is None else name.text)
        # phones1.append("" if phone1 is None else phone1)
        # phones2.append("" if phone2 is None else phone2)
        # price=a.find('p', attrs={'class':'phone'})
        # products.append("" if name is None else name.text)
        # prices.append("" if price is None else price.text)
# url = "https://www.listing.com.pk/listing/page/8"
# print(names)
# print(phones1)
# print(phones2)
# driver.get(url)
# content = driver.page_source
# soup = BeautifulSoup(content, features="lxml")
# for a in soup.findAll('div', attrs={'class':'post'}):
#     name=a.find('h2', attrs={'class':'entry-title'})
#     price=a.find('p', attrs={'class':'phone'})
#     products.append(name.text)
#     prices.append("" if price is None else price.text)

# df = pd.DataFrame({'Product Name':products,'Price':prices}) 
# df.to_csv('products.csv', index=False, encoding='utf-8')

driver.quit()