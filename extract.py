from lxml import html
from utils import read_htmlFile, load_xpaths
from db_config import create_table, insert_into_db


# html file path
base_path = r'C:\Users\hemanshu.marwadi\Desktop\Himanshu Marwadi\x-path\bk_store\bk_store.html'
json_file_path = r'C:\Users\hemanshu.marwadi\Desktop\Himanshu Marwadi\x-path\bk_store\xpaths.json'
TABLE_NAME = 'burger_king_stores'


def parsel(html_data, xpaths):
    burger_king = []
    tree = html.fromstring(html_data)

    store_info = tree.xpath(xpaths["store_info"])

    for information in store_info:
        bk_stores = {}

        onclick = information.xpath(xpaths["onclick"])
        bk_stores['store_id'] = onclick.split(",")[-1].replace("'", "").replace(")", "").strip() if onclick else None

        bk_stores['brand_name'] = information.xpath(xpaths["brand_name"])
        bk_stores['address'] = information.xpath(xpaths["address"])
        bk_stores['locality'] = information.xpath(xpaths["locality"])
        bk_stores['city'] = information.xpath(xpaths["city"])
        bk_stores['pincode'] = information.xpath(xpaths["pincode"])
        bk_stores['phone_number'] = information.xpath(xpaths["phone_number"])
        bk_stores['timing'] = information.xpath(xpaths["timing"])
        bk_stores['store_url'] = information.xpath(xpaths["store_url"])
        bk_stores['map_url'] = information.xpath(xpaths["map_url"])

        burger_king.append(bk_stores)

    return burger_king


def main():
    create_table(table_name=TABLE_NAME)
    raw = read_htmlFile(base_path)
    xpaths = load_xpaths(json_file_path)
    pars_data = parsel(raw, xpaths)

    for row in pars_data:
        insert_into_db(table_name=TABLE_NAME, data=row)


if __name__ == '__main__':
    main()