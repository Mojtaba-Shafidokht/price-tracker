import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

PROXY = os.getenv("TELEGRAM_PROXY")


def _get_proxies():
    if PROXY:
        return {"http": PROXY, "https": PROXY}
    return None


def send_notification(message):
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    header = f"📊 Price Tracker Report\n🕐 {date}\n\n"
    final_message = header + message

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try:
        requests.post(
            url,
            data={"chat_id": CHAT_ID, "text": final_message},
            proxies=_get_proxies(),
            timeout=20
        )

    except Exception as e:
        print(f"⚠️ Failed to send Telegram notification: {e}")
