import json
from scraper import get_price
from utils import update_price


def load_products():
    with open("products.json", "r") as f:
        return json.load(f)


def clean_price(str_price):
    return int(str_price
               .replace(",", "")
               .replace("،", "")
               .replace("تومان", "")
               .strip()
               )


products = load_products()

for product_name, product_url in products.items():
    print(f"\nChecking: {product_name}")

    raw_price = get_price(product_url)

    try:
        if raw_price:
            price = clean_price(raw_price)
            print(f"Current Price: {price}")

            update_price(product_name, product_url, price)
        else:
            print("Price not find")
    except Exception as e:
        print("Error: ", e)
