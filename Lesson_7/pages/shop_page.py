from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        return self

    def login(self, username, password):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#user-name")))
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        return ProductPage(self.driver)


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack_to_cart(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")))
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        return self

    def add_bolt_t_shirt_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        return self

    def add_onesie_to_cart(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        return self

    def go_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
        return CartPage(self.driver)


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def checkout(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        self.driver.find_element(By.ID, "checkout").click()
        return CheckoutPage(self.driver)


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_customer_info(self, first_name, last_name, postal_code):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#first-name")))
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(postal_code)
        return self

    def continue_to_overview(self):
        self.driver.find_element(By.ID, "continue").click()
        return self

    def get_total_amount(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.summary_total_label")))
        return self.driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text