import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.calculator_page import CalculatorPage

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

class TestSlowCalculator:
    def test_slow_calculator(self, driver):
        # Создаем объект страницы
        calculator_page = CalculatorPage(driver)

        # Открываем страницу калькулятора
        calculator_page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Устанавливаем задержку
        calculator_page.set_delay(45)

        # Выполняем вычисление 7 + 8
        calculator_page.click_button("7")
        calculator_page.click_button("+")
        calculator_page.click_button("8")
        calculator_page.click_button("=")

        # Ожидаем результат и проверяем
        assert calculator_page.wait_for_result("15"), "Результат не появился за отведенное время"
        result = calculator_page.get_screen_text()

        assert result == "15", f"Ожидался результат 15, получено {result}"
