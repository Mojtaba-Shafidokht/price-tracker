from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


def get_product_info(url):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0")

    try:
        driver = webdriver.Chrome(
            service=Service("./chromedriver.exe"),
            options=options
        )
    except:
        driver = webdriver.Chrome()

    driver.get(url)

    wait = WebDriverWait(driver, 10)

    try:
        title_element = wait.until(
            ec.presence_of_element_located(
                (By.CSS_SELECTOR, "[class='text-h4 text-neutral-900 mb-2 pointer-events-none']")
            )
        )
        title = title_element.text

        price_element = wait.until(
            ec.presence_of_element_located(
                (By.CSS_SELECTOR, "[class='ml-1 text-neutral-800']")
            )
        )
        price = price_element.text

        return title, price

    except TimeoutException:
        return None, None

    except Exception as e:
        return None, None

    finally:
        driver.quit()
