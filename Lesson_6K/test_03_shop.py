from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


def test_shop():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    try:
        driver.get("https://www.saucedemo.com/")

        user_name = driver.find_element(By.CSS_SELECTOR, "#user-name")
        user_name.send_keys("standard_user")
        password = driver.find_element(By.CSS_SELECTOR, "#password")
        password.send_keys(By.CSS_SELECTOR, "#secret_sauce")

        driver.find_element(By.ID, "login-button").click()

        backpack = WebDriverWait(driver, 10).until(
            EC.element_to_by_clickable((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")))
        backpack = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
        backpack.click()

        shirt = WebDriverWait(driver, 10).until(
            EC.element_to_by_clickable((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")))
        shirt = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
        shirt.click()



    finally:
        driver.quit()

