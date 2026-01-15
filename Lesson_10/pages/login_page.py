from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    """Страница авторизации"""

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def open(self) -> None:
        """Открывает страницу логина"""
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username: str, password: str) -> None:
        """
        Выполняет авторизацию.

        :param username: Логин
        :param password: Пароль
        """
        self.find(self.USERNAME).send_keys(username)
        self.find(self.PASSWORD).send_keys(password)
        self.find(self.LOGIN_BUTTON).click()