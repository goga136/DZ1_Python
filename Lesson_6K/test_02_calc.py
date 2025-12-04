import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def test_slow_calculator():

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 60)

    delay_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
    delay_input.clear()
    delay_input.send_keys("45")

    driver.find_element(By.CSS_SELECTOR,"//span[text()='7']").click()
    driver.find_element(By.CSS_SELECTOR, "//span[text()='+']").click()
    driver.find_element(By.CSS_SELECTOR, "//span[text()='8']").click()
    driver.find_element(By.CSS_SELECTOR, "//span[text()='=']").click()

    wait = WebDriverWait(driver, 60)
    wait.until(
        EC.text_to_be_presence_in_element(By.ID, "screen"),'15')
    result = driver.find_element(By.ID, "screen").text
    wait_input.clear()
    print(result)
    assert result == "15"


    driver.quit()
