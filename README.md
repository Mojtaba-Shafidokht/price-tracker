# 📊 Price Tracker (Digikala Scraper)

A Python-based price tracking tool that monitors product prices from Digikala using Selenium.
This project automatically scrapes product prices, stores them, and detects any changes over time.

---

## 🚀 Features

* 🔍 Scrape product prices from Digikala
* 🧹 Clean and convert price data into numeric format
* 💾 Store prices locally using JSON
* 📈 Detect price changes (increase, decrease, no change)
* 🧱 Modular and scalable project structure
* 📬 Telegram notifications for price changes and unavailable products

---

## 🛠️ Technologies Used

* Python 3
* Selenium
* JSON (for data storage)
* python-dotenv (for environment variables)
* Telegram Bot API (for notifications)

---

## 📂 Project Structure

```
price-tracker/
│
├── main.py            # Entry point of the application
├── scraper.py         # Handles web scraping logic
├── utils.py           # Data storage and comparison logic
├── notifier.py        # Sends batched Telegram notifications
├── .env.example       # Template for environment variables
├── products.example.json  # Template for product URLs
├── requirements.txt   # Project dependencies
├── README.md          # Project documentation
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/price-tracker.git
cd price-tracker
```

2. Create and activate virtual environment:

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🧾 Configuration

Before running the project, you need to create a `products.json` file.

You can use the provided example file:

```bash
cp products.example.json products.json
```

Then edit `products.json` and add your desired product URLs.

```json
{
    "samsung_s26": "https://www.digikala.com/product/dkp-20481189/",
    "ps5_slim": "https://www.digikala.com/product/dkp-11223344/"
}
```

---

## 📬 Telegram Notifications

1. Create a bot via `@BotFather` and get your token
2. Send a message to your bot and get your Chat ID:
`https://api.telegram.org/bot<YOUR_TOKEN_HERE>/getUpdates`
3. Rename `.env.example` to `.env`:
```bash
mv .env.example .env
```
4. Open `.env` and fill in your credentials:
```
TELEGRAM_TOKEN=your_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
TELEGRAM_PROXY=
```   

> ⚠️ **Note:** Local proxy URL (e.g. `http://127.0.0.1:10808`) — only needed if `api.telegram.org` is blocked in your region. See "Notes for Users Behind Internet Filtering" below.

---

## Notes for Users Behind Internet Filtering

If Telegram is blocked in your country, you may see SSL/timeout errors
when sending notifications, even with a system-wide VPN enabled — this
often happens because scraping Digikala (an Iranian server) becomes
noticeably slower when all traffic is routed through a VPN tunnel.

**Recommended approach:** instead of enabling a full VPN, run a local
proxy (e.g. via V2Ray/Xray) and set `TELEGRAM_PROXY` in your `.env` file
to point to it (e.g. `http://127.0.0.1:10808`). This way, only the
Telegram API request goes through the tunnel, while scraping stays
fast and direct.

---

## Notifications

All price changes, out-of-stock alerts, and errors detected during a
single run are collected and sent as **one combined Telegram message**
at the end of execution, instead of sending a separate message per
product. If nothing has changed, no message is sent.

---

## ⚠️ ChromeDriver Requirement

This project uses Selenium to automate browser interactions.
To run the project successfully, you need to have a compatible version of **Google Chrome** and **ChromeDriver** installed.

### 🔧 Setup Instructions

1. Check your Chrome version:

```
chrome://version
```

2. Download the matching ChromeDriver:
   https://googlechromelabs.github.io/chrome-for-testing/

3. Place `chromedriver` in the project directory:

```
price-tracker/
├── chromedriver.exe
```

---

### ❗ Important Notes

* ChromeDriver version **must match** your installed Chrome version
* This project currently supports **Google Chrome only**
* Other browsers like Firefox are not supported by default

---

### 🌍 Network Limitation

In some regions, automatic driver download may be blocked.
For this reason, the project uses a **local ChromeDriver** instead of downloading it dynamically.

---

## ▶️ Usage

Run the program:

```bash
python main.py
```

---

## 🧠 How It Works

1. The scraper fetches the product page using Selenium
2. Extracts the product title and price
3. Cleans and converts the price into an integer
4. Stores the price in a JSON file
5. Compares it with the previous price
6. Displays whether the price has increased, decreased, or stayed the same
7. Collects all changes and sends a single batched Telegram notification at the end

---

## 📌 Example Output

```
Checking product...
📈 Price increased
🛍 Product: Samsung Galaxy S26 Ultra - 512 Gb
📊 Current Price: 500000000
⬇️ Minimum Price: 386995000
🕐 Last Updated: 2026-02-09 20:27
```

---

## Data Storage

Product prices are stored in `prices.json`, keyed by the stable
Digikala product ID (extracted from the URL, e.g. `dkp-20481189`)
rather than the product title — titles can change slightly between
scrapes (e.g. due to invisible ZWNJ characters), so IDs are used to
avoid mismatches.

```json
{
    "20481189": {
        "title": "...",
        "url": "...",
        "current_price": 409990000,
        "minimum_price": 405000000,
        "last_updated": "2026-07-01"
    }
}
```

---

## ⚠️ Notes

* This project is for educational purposes
* Websites may change their structure, which can break the scraper
* Headless mode may not always work due to anti-bot protections

---

## 🔮 Future Improvements

* Export data to Excel
* Scheduling (run periodically)

---

## 👨‍💻 Author

Mojtaba Shafidokht

---

## ⭐️ Show Your Support

If you found this project useful, consider giving it a star ⭐ on GitHub!
