import json

FILE_NAME = "prices.json"


def load_data():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except Exception as e:
        print("Error: ", e)
        return {}


def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


def update_price(product_name, url, new_price):
    data = load_data()

    if product_name in data:
        old_price = data[product_name]["price"]

        if new_price > old_price:
            print("📈 Price increased")
        elif new_price < old_price:
            print("📉 Price decreased")
        else:
            print("➖ No change")

    else:
        print("🆕 New product added")

    data[product_name] = {
        "url": url,
        "price": new_price
    }

    save_data(data)
