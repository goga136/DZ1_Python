from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


def run_test():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    try:
        driver.get("http://the-internet.herokuapp.com/inputs")
        input_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='number']")))

        input_field.send_keys("Sky")
        input_field.clear()
        input_field.send_keys("Pro")
    finally:
        driver.quit()


run_test()
