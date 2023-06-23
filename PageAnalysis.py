from bs4  import BeautifulSoup
from Scraping import Scraping
import re
import pandas as pd


class PageAnalysis:
    def __init__(self,html) -> None:
        self.soup = BeautifulSoup(html,"html.parser")
        self.product_Data = []

    def starcount(self,star_control): #star count calculate with regex
        total =0
        for star_divs in star_control.find_all("div",attrs={"class":"full"}):
            styles = star_divs.get("style")
            match = re.search(r"width:\s*([\d.]+)(?:px|%)", styles)        
            total+=float(match.group(1))
        return total/100


    def analysis(self):
        item_list = self.soup.find_all("div",attrs={"class":"p-card-chldrn-cntnr card-border"})
        for item in item_list:
            product_link = item.a.get("href")
            product_brand = item.find("span",attrs={"class":"prdct-desc-cntnr-ttl"}).text.strip() #marka
            corgo_control = item.find("div",attrs={"class":"product-stamp-container freeCargo"})
            product_freecargo = 1 if corgo_control is not None else 0  # freecargo 0 = no 1 =yes
            product_image= item.find("img",attrs={"class":"p-card-img"}).get("src") #image
            product_title = item.find("span",attrs={"class":"prdct-desc-cntnr-name"}).get("title") #title
            text_count =item.find("span",attrs={"class":"ratingCount"})
            if text_count is not None:
                text_count = text_count.text
                product_rating_count= ''.join(filter(str.isdigit, text_count)) #comment count
            else:
                product_rating_count = 0
            
            star_control= item.find("div",attrs={"class":"ratings"})
            product_rating_star = 0
            if star_control is not None:        
                product_rating_star =self.starcount(star_control) #star count
                
            control_text_dis = item.find("div",attrs={"class":"low-price-in-last-month"})
            product_discount_text=None
            if control_text_dis is not None:
                product_discount_text = control_text_dis.find("span").text    #discount text
            product_original_price=None
            control_org_price = item.find("div",attrs={"class":"prc-box-orgnl"})    
            if control_org_price is not None:
                product_original_price = control_org_price.text #original price
            
            product_discount_price=None
            control_dis_price = item.find("div",attrs={"class":"prc-box-dscntd"})    
            if control_dis_price is not None:
                product_discount_price = control_dis_price.text  #discount price
            
        
            Product={
                "ProductLink":product_link,
                "ProductBrand":product_brand,
                "ProductFreeCargo":product_freecargo,
                "ProductImage":product_image,
                "ProductTitle":product_title,
                "ProductComment":product_rating_count,
                "ProductRating": product_rating_star,
                "ProductDiscountText":product_discount_text,
                "ProductOriginalPrice":product_original_price,
                "ProducDiscountPrice":product_discount_price
            }
            self.product_Data.append(Product)

    def tocsv(self,file_name):            
        df = pd.DataFrame(self.product_Data)
        df.to_csv(file_name)
