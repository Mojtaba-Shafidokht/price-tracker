import json
import re
from datetime import datetime

FILE_NAME = "prices.json"


def extract_id(url):
    match = re.search(r'dkp-(\d+)', url)
    return match.group(1) if match else None


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
    product_id = extract_id(url)

    if not product_id:
        print(f"⚠️ Could not extract product ID from URL: {url}")
        return None

    if product_id not in data:
        print("🆕 New product added")

        data[product_id] = {
            "title": product_name,
            "url": url,
            "current_price": new_price,
            "minimum_price": new_price,
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M")
        }

        save_data(data)
        result = data[product_id].copy()
        result["price_changed"] = None
        return result

    last_price = data[product_id]["current_price"]
    min_price = data[product_id].get("minimum_price", new_price)
    date = data[product_id]["last_updated"]

    if new_price < min_price:
        min_price = new_price

    price_changed = None
    if new_price > last_price:
        print("📈 Price increased")
        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        price_changed = "increased"
    elif new_price < last_price:
        print("📉 Price decreased")
        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        price_changed = "decreased"
    else:
        print("➖ No change")

    data[product_id] = {
        "title": product_name,
        "url": url,
        "current_price": new_price,
        "minimum_price": min_price,
        "last_updated": date
    }

    save_data(data)
    result = data[product_id].copy()
    result["price_changed"] = price_changed
    return result
