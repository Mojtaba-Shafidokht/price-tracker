import json
from scraper import get_product_info
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

for product_url in products.values():
    print("\nChecking product...")

    title, raw_price = get_product_info(product_url)

    try:
        if title and raw_price:
            price = clean_price(raw_price)

            print(f"Product: {title}")
            print(f"Current Price: {price}")

            update_price(title, product_url, price)

        else:
            print("Price not find and failed to fetch data")

    except Exception as e:
        print("Error: ", e)
