import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_not_found(url):
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    message = (
        f"❌ Product not found! - ⚠️ Check it manually to make sure!\n\n"
        f"🔗 {url}\n"
        f"🕐 {date}"
    )

    url_api = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url_api, data={"chat_id": CHAT_ID, "text": message})


def send_unavailable(product_name, last_price):
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    message = (
        "⚠️ Product unavailable\n\n"
        f"🛍 {product_name}\n\n"
        f"Last price: {last_price:,} Toman\n"
        f"🕐 {date}"
    )

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})


def send_notification(product_name, old_price, new_price):
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    if new_price > old_price:
        emoji = "📈"
        status = "Price increased"
    elif new_price < old_price:
        emoji = "📉"
        status = "Price decreased"
    else:
        emoji = "➖"
        status = "No change"

    message = (
        f"{emoji} {status}\n\n"
        f"🛍 {product_name}\n\n"
        f"Last price: {old_price:,} Toman\n"
        f"New price: {new_price:,} Toman\n"
        f"🕐 {date}"
    )

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})
