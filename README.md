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

2. Run the program:

```bash
python main.py
```

---

## 🧠 How It Works

1. The scraper fetches the product page using Selenium
2. Extracts the product price
3. Cleans and converts the price into an integer
4. Stores the price in a JSON file
5. Compares it with the previous price
6. Displays whether the price has increased, decreased, or stayed the same

---

## 📌 Example Output

```
iphone_17_pro_max_256_12_CH
Current Price: 445000000
➖ No change
```

---

## ⚠️ Notes

* This project is for educational purposes
* Websites may change their structure, which can break the scraper
* Headless mode may not always work due to anti-bot protections

---

## 🔮 Future Improvements

* Automatic product name extraction
* Email/Telegram notifications on price changes
* Export data to Excel
* Scheduling (run periodically)

---

## 👨‍💻 Author

Mojtaba Shafidokht

---

## ⭐️ Show Your Support

If you found this project useful, consider giving it a star ⭐ on GitHub!
