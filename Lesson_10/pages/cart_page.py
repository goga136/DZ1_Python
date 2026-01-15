from selenium.webdriver.common.by import By
from .base_page import BasePage


class CartPage(BasePage):
    """Страница корзины"""

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def checkout(self) -> None:
        """Нажатие кнопки Checkout"""
        self.find(self.CHECKOUT_BUTTON).click()