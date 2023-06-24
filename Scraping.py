from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

import time


class Scraping:
    def __init__(self,url,product) -> None:
        self.url = url
        self.html=''
        self.product = product

    def start(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        driver.maximize_window()
        searchbar=driver.find_element(By.XPATH,"//*[@id='sfx-discovery-search-suggestions']/div/div/input")
        time.sleep(1)
        searchbar.click()
        searchbar.send_keys(self.product)
        time.sleep(1)
        searchbar.send_keys(Keys.ENTER)
        time.sleep(2)
        a = 0   #scroll size
        b = 200
        while True:        
            driver.execute_script("window.scrollTo({}, {})".format(a,b))        
            current_height = driver.execute_script("return document.body.scrollHeight")    
            if b>= current_height:   #page end
                break
            a = b
            b += 200        
            time.sleep(1)
        self.html = driver.page_source
        driver.close()
       

    