from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_product_info(url):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get(url)

    wait = WebDriverWait(driver, 10)

    try:
        title_element = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[class='text-h4 text-neutral-900 mb-2 pointer-events-none']")
            )
        )
        title = title_element.text

        price_element = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[class='ml-1 text-neutral-800']")
            )
        )
        price = price_element.text

        return title, price

    except Exception as e:
        print("Error: ", e)
        return None, None

    finally:
        driver.quit()
