import json
from scraper import get_product_info
from utils import update_price, extract_id, load_data as load_products_info
from notifier import send_notification


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
messages = []

for product_url in products.values():
    print("\nChecking product...")

    try:
        title, raw_price = get_product_info(product_url)

        if title is not None and raw_price is not None:
            price = clean_price(raw_price)
            title = title.strip()

            info = update_price(title, product_url, price)

            print(f"🛍 Product: {title}")
            print(f"📊 Current Price: {price}")
            print(f"⬇️ Minimum Price: {info['minimum_price']}")
            print(f"🕐 Last Updated: {info['last_updated']}")

            if info.get("price_changed"):
                emoji = "📈" if info["price_changed"]=="increased" else "📉"
                status = "Price increased" if info["price_changed"] == "increased" else "Price decreased"

                messages.append(
                    f"{emoji} {status}\n"
                    f"🛍 Product: {title}\n"
                    f"📊 Current price: {price}\n"
                    f"⬇️ Minimum price: {info['minimum_price']}\n"
                    f"🕐 Last updated: {info['last_updated']}\n"
                )

        else:
            product_id = extract_id(product_url)
            products_info = load_products_info()

            if product_id and product_id in products_info:
                info = products_info[product_id]
                title, current_price, min_price, date = (
                    info['title'], info['current_price'], info['minimum_price'], info['last_updated'])

                log1 = (
                    f"⚠️ Unavailable - Last Price: {current_price}\n"
                    f"🛍 Product: {title}\n"
                    f"⬇️ Minimum Price: {min_price}\n"
                    f"🕐 Last Updated: {date}"
                )

                print(log1)
                messages.append(log1)

            else:
                log2 = f"❌ Product out of stack! - ⚠️ Check it manually to make sure!\n🔗 Product url: {product_url}"

                print(log2)
                messages.append(log2)

    except Exception as e:
        print("Error: ", e)

if messages:
    final_message = "\n\n".join(messages)
    send_notification(final_message)
else:
    print("No changes for sending notifications!")
