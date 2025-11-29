from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/textinput")

input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input_field.clear()
input_field.send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

updated_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button_text = updated_button.text

print(button_text)

driver.quit()
