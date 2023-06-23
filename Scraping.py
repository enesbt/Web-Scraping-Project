from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

import time


class Scraping:
    def __init__(self,url) -> None:
        self.url = url
        self.html=''

    def start(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        driver.maximize_window()
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
       

    