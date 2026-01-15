from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
import re

class CheckoutPage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    def fill_form(self, first_name, last_name, zip_code):
        # блокируем любые JS alert/confirm, которые мешают
        self.driver.execute_script("window.alert = function() {};")
        self.driver.execute_script("window.confirm = function() {return true;};")

        # заполняем форму
        self.find(self.FIRST_NAME).send_keys(first_name)
        self.find(self.LAST_NAME).send_keys(last_name)
        self.find(self.POSTAL_CODE).send_keys(zip_code)

        # ждём кнопку Continue и кликаем через JS
        button = self.wait.until(
            EC.presence_of_element_located(self.CONTINUE_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", button)

        # ждём реальный переход на step-two
        self.wait.until(EC.url_contains("checkout-step-two"))

    def get_total(self) -> float:
        text = self.find(self.TOTAL).text
        return float(re.search(r"\$(\d+\.\d+)", text).group(1))
