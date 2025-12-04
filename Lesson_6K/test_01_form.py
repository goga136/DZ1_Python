import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)

@pytest.fixture()
def driver():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_form_validation(driver):

    first_name = driver.find_element(By.CSS_SELECTOR, "[name = 'first-name']")
    first_name.send_keys("Иван")
    first_name.click()

    last_name = driver.find_element(By.CSS_SELECTOR, "[name = 'last-name']")
    last_name.send_keys("Петров")
    last_name.click()

    address_input = driver.find_element(By.CSS_SELECTOR, "[name = 'address']")
    address_input.send_keys("Ленина, 55-3")
    address_input.click()

    city_name = driver.find_element(By.CSS_SELECTOR, "[name = 'city']")
    city_name.send_keys("Москва")
    city_name.click()

    country_name = driver.find_element(By.CSS_SELECTOR, "[name = 'country']")
    country_name.send_keys("Россия")
    country_name.click()

    e_mail = driver.find_element(By.CSS_SELECTOR, "[name = 'e-mail']")
    e_mail.send_keys("test@skypro.com")
    e_mail.click()

    phone_number = driver.find_element(By.CSS_SELECTOR, "[name = 'phone']")
    phone_number.send_keys("+7985899998787")
    phone_number.click()

    job_position = driver.find_element(By.CSS_SELECTOR, "[name = 'job-position']")
    job_position.send_keys("QA")
    job_position.click()

    company_name = driver.find_element(By.CSS_SELECTOR, "[name = 'company']")
    company_name.send_keys("SkyPro")
    company_name.click()

    submit_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3")
    submit_button.click()

    field = driver.find_element(By.CSS_SELECTOR,"[name = 'zip-code']").element.value_of_css_property('background-color')
    assert field == '#f8d7da'

    for field in fields:
        fields = ['first-name', 'last-name', 'address', 'city', 'country', 'e-mail', 'phone', 'job-position', 'company']
        taps = driver.find_elements(By.CSS_SELECTOR, "form-label").element.value_of_css_property('background-color')
        assert taps == '#d1e7dd'


    driver.quit()
