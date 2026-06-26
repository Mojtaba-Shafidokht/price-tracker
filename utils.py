import json
from notifier import send_notification

FILE_NAME = "prices.json"


def get_last_price(product_url):
    data = load_data()

    for product_name, product_info in data.items():
        if product_info["url"] == product_url:
            return product_name, product_info["price"]

    return None, None


def load_data():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print("Error: ", e)
        return {}


def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def update_price(product_name, url, new_price):
    data = load_data()

    if product_name in data:
        old_price = data[product_name]["price"]

        if new_price > old_price:
            print("📈 Price increased")
            send_notification(product_name, old_price, new_price)
        elif new_price < old_price:
            print("📉 Price decreased")
            send_notification(product_name, old_price, new_price)
        else:
            print("➖ No change")
            send_notification(product_name, old_price, new_price)

    else:
        print("🆕 New product added")

    data[product_name] = {
        "url": url,
        "price": new_price
    }

    save_data(data)
