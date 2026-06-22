from scraper import get_price
from utils import update_price


def clean_price(str_price):
    return int(str_price
               .replace(",", "")
               .replace("،", "")
               .replace("تومان", "")
               .strip()
               )


product_name = "iphone_17_pro_max_256_12_CH"

product_url = (
    "https://www.digikala.com/product/dkp-20481189/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84"
    "-%D8%A7%D9%BE%D9%84-%D9%85%D8%AF%D9%84-iphone-17-pro-max-ch-%D8%AF%D9%88-%D8%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8"
    "%B1%D8%AA-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-256-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%88-%D8%B1"
    "%D9%85-12-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D9%86%D8%A7%D8%AA-%D8%A7%DA%A9%D8%AA%DB%8C%D9%88/")

raw_price = get_price(product_url)

try:
    if raw_price:
        price = clean_price(raw_price)
        print(product_name)
        print(f"Current Price: {price}")

        update_price(product_name, product_url, price)
    else:
        print("Price not find")
except Exception as e:
    print("Error: ", e)
