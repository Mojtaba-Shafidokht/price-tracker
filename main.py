import json
from scraper import get_product_info
from utils import update_price, get_last_price
from notifier import send_unavailable, send_not_found


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

    try:
        title, raw_price = get_product_info(product_url)

        if title and raw_price:
            price = clean_price(raw_price)

            print(f"Product: {title}")
            print(f"Current Price: {price}")

            update_price(title, product_url, price)

        else:
            last_name, last_price = get_last_price(product_url)

            if last_name:
                print(f"Product: {last_name}")
                print(f"⚠️ Unavailable - Last Price: {last_price}")
                send_unavailable(last_name, last_price)
            else:
                print(f"❌ Product not found! - ⚠️ Check it manually to make sure!\nProduct url: {product_url}")
                send_not_found(product_url)

    except Exception as e:
        print("Error: ", e)
