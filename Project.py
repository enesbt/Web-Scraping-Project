from PageAnalysis import PageAnalysis
from Scraping import Scraping

def main():
    url = input("Link? ")
    scraping_obj = Scraping(url)
    scraping_obj.start()
    analysis_obj = PageAnalysis(scraping_obj.html)
    analysis_obj.analysis()  
    analysis_obj.tocsv("product2.csv")  




if __name__ == '__main__':
    main()

