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

---

## 🛠️ Technologies Used

* Python 3
* Selenium
* JSON (for data storage)

---

## 📂 Project Structure

```
price-tracker/
│
├── main.py          # Entry point of the application
├── scraper.py       # Handles web scraping logic
├── utils.py         # Data storage and comparison logic
├── requirements.txt # Project dependencies
├── README.md        # Project documentation
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

---

## 📌 Example Output

```
Checking product...

Product: Apple iPhone 17 Pro Max CH Dual SIM
Current Price: 450000000
📈 Price increased
```

---

## ⚠️ Notes

* This project is for educational purposes
* Websites may change their structure, which can break the scraper
* Headless mode may not always work due to anti-bot protections

---

## 🔮 Future Improvements

* Email/Telegram notifications on price changes
* Export data to Excel
* Scheduling (run periodically)

---

## 👨‍💻 Author

Mojtaba Shafidokht

---

## ⭐️ Show Your Support

If you found this project useful, consider giving it a star ⭐ on GitHub!
