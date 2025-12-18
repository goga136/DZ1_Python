from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    # Локаторы
    delay_input = (By.CSS_SELECTOR, "#delay")
    screen = (By.CLASS_NAME, "screen")

    # Методы для получения локаторов кнопок (можно вынести в отдельный словарь)
    @staticmethod
    def _get_button_locator(text):
        return (By.XPATH, f"//span[text()='{text}']")

    # Методы взаимодействия с элементами
    def open(self, url):
        self.driver.get(url)

    def set_delay(self, delay):
        delay_input = self.wait.until(
            EC.presence_of_element_located(self.delay_input)
        )
        delay_input.clear()
        delay_input.send_keys(str(delay))

    def click_button(self, button_text):
        button_locator = self._get_button_locator(button_text)
        button = self.wait.until(
            EC.element_to_be_clickable(button_locator)
        )
        button.click()

    def get_screen_text(self):
        screen = self.wait.until(
            EC.presence_of_element_located(self.screen)
        )
        return screen.text

    def wait_for_result(self, expected_result, timeout=60):
        try:
            self.wait.until(
                EC.text_to_be_present_in_element(self.screen, expected_result)
            )
            return True
        except:
            return False
