from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

from bs4  import BeautifulSoup
import re
import time

#url = "https://www.trendyol.com/oyuncu-dizustu-bilgisayari-x-c106084"
url="https://www.trendyol.com/sr?wc=101512&wb=108128&tag=sari_kampanya_urunu"
driver = webdriver.Chrome()



driver.get(url)
driver.maximize_window()
    


time.sleep(2)        
a = 0
b=200
while True:
        
    driver.execute_script("window.scrollTo({}, {})".format(a,b))     

    
    current_height = driver.execute_script("return document.body.scrollHeight")
    
    if b>= current_height:
        break
    a = b
    b += 200
        
    time.sleep(1)
       

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")


def starcount(star_control):
    for star_divs in star_control.find_all("div",attrs={"class":"full"}):
        #star_divs = star_control.find_all("div", class_="full")
        styles = star_divs.get("style")
        width_values = []
        
        match = re.search(r'width:\s*(\d+)%?;', styles)
        if match:
            width_value = int(match.group(1))
            width_values.append(width_value)
    print(width_values)
           
        

    




product_data =[]
item_list = soup.find_all("div",attrs={"class":"p-card-chldrn-cntnr card-border"})

for item in item_list:
    product_brand = item.find("span",attrs={"class":"prdct-desc-cntnr-ttl"}).text.strip() #marka
    corgo_control = item.find("div",attrs={"class":"product-stamp-container freeCargo"})
    product_freecargo = 1 if corgo_control is not None else 0
    product_image= item.find("img",attrs={"class":"p-card-img"}).get("src")
    product_title = item.find("span",attrs={"class":"prdct-desc-cntnr-name"}).get("title")
    text_count =item.find("span",attrs={"class":"ratingCount"})
    if text_count is not None:
        text_count = text_count.text
        product_rating_count= ''.join(filter(str.isdigit, text_count))
    else:
        product_rating_count = 0
    
    star_control= item.find("div",attrs={"class":"ratings"})
    
    if star_control is not None:        
            starcount(star_control)
            #for x in star_control.find_all("div",attrs={"class":"full"}):
             #   print(x.get("style"))
    else:
        product_rating_star = 0 
    product_discount_text=0
    product_original_price=0
    product_discount_price=0
  #  print(product_rating_count)
   # print(product_title)
    

    





time.sleep(2)
driver.close()