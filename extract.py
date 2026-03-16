from lxml import html
from utils import read_htmlFile
from db_config import create_table , insert_into_db

#html file path
base_path = r'C:\Users\hemanshu.marwadi\Desktop\Himanshu Marwadi\x-path\bk_store\bk_store.html'
TABLE_NAME = 'burger_king_stores' #table name from store data in database

def parsel(html_data):
    burger_king = []
    tree = html.fromstring(html_data) #html data convert a fromstring ( tree format )
    store_info = tree.xpath('//div[@class = "store-info-box"]')
    for information in store_info:
        bk_stores = {}
        bk_stores['brand_name'] = information.xpath('normalize-space(string(.//li[@class = "outlet-name"]//a))')
        bk_stores['address'] = information.xpath('normalize-space(string(.//li[@class = "outlet-address"]//span/text()))')
        bk_stores['locality'] = information.xpath('normalize-space(string(.//div[@class="info-text"]//span[2]))')
        bk_stores['city'] = information.xpath('normalize-space(string(.//span[@class="merge-in-next"]/span[1]))')
        bk_stores['pincode'] = information.xpath('normalize-space(.//span[@class="merge-in-next"]//span[3])')
        bk_stores['phone_number'] = information.xpath('normalize-space(.//li[@class = "outlet-phone"]//a)')
        bk_stores['timing'] = information.xpath('normalize-space(.//li[@class = "outlet-timings"]//div[@class = "info-text"]//span)')
        bk_stores['store_url'] = information.xpath('normalize-space(.//a[@class = "btn btn-website"]//@href)')
        bk_stores['map_url'] = information.xpath('normalize-space(.//a[@class = "btn btn-map"]//@href)')
        burger_king.append(bk_stores)
    
    return burger_king
        
    

def main():
    create_table(table_name=TABLE_NAME) #table create
    raw = read_htmlFile(base_path) #read raw data
    pars_data = parsel(raw) # Extract data from raw formate
    for row in pars_data:
        insert_into_db(table_name=TABLE_NAME, data=row) #insert data in database
    
    
if __name__ == '__main__':
    main()