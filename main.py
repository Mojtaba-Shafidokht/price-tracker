import json
from scraper import get_product_info
from utils import update_price, extract_id, load_data as load_products_info
from notifier import send_unavailable, send_not_found


def load_products():
    try:
        with open("products.json", "r") as f:
            return json.load(f)
    except:
        return {}


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

        if title is not None and raw_price is not None:
            price = clean_price(raw_price)
            title = title.strip()

            info = update_price(title, product_url, price)

            print(f"Product_title: {title}")
            print(f"Current Price: {price}")
            print(f"Minimum Price: {info['minimum_price']}")
            print(f"Last Updated: {info['last_updated']}")

        else:
            product_id = extract_id(product_url)
            products_info = load_products_info()

            if product_id and product_id in products_info:
                info = products_info[product_id]
                title, current_price, min_price, date = (
                    info['title'], info['current_price'], info['minimum_price'], info['last_updated'])

                print(f"Product_title: {info['title']}")
                print(f"⚠️ Unavailable - Last Price: {info['current_price']}")
                print(f"Minimum Price: {info['minimum_price']}"),
                print(f"Last Updated: {info['last_updated']}")

                send_unavailable(title, current_price, min_price, date)

            else:
                print(f"❌ Product not found! - ⚠️ Check it manually to make sure!\nProduct url: {product_url}")

                send_not_found(product_url)

    except Exception as e:
        print("Error: ", e)
