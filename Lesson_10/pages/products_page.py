from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProductsPage(BasePage):
    """Главная страница магазина"""

    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")

    PRODUCTS = {
        "Sauce Labs Backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
        "Sauce Labs Bolt T-Shirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
        "Sauce Labs Onesie": (By.ID, "add-to-cart-sauce-labs-onesie"),
    }

    def add_product(self, product_name: str) -> None:
        """
        Добавляет товар в корзину.

        :param product_name: Название товара
        """
        self.find(self.PRODUCTS[product_name]).click()

    def open_cart(self) -> None:
        """Переход в корзину"""
        self.find(self.CART_BUTTON).click()