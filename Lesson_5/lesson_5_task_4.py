from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


def run_test():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    try:
        driver.get("http://the-internet.herokuapp.com/login")
        input_login = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "username")))

        input_login.send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, ".fa").click()

        wait = WebDriverWait(driver, 10)
        message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#flash")))
        print(message.text.strip())
    finally:
        driver.quit()


run_test()
