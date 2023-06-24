from PageAnalysis import PageAnalysis
from Scraping import Scraping

def main():
    url = input("WebSite? ")
    product = input("ProductName? ")
    scraping_obj = Scraping(url,product)
    scraping_obj.start()
    analysis_obj = PageAnalysis(scraping_obj.html)
    analysis_obj.analysis()  
    analysis_obj.tocsv("{}.csv".format(product))  




if __name__ == '__main__':
    main()

