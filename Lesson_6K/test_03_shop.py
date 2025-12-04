from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_shop():
    driver = webdriver.Firefox()

    try:
        driver.get("https://www.saucedemo.com/")

        user_name = driver.find_element(By.CSS_SELECTOR, "#user-name")
        user_name.send_keys("standard_user")
        password = driver.find_element(By.CSS_SELECTOR, "#password")
        password.send_keys("secret_sauce")

        driver.find_element(By.ID, "login-button").click()

        (WebDriverWait(driver, 10).
         until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"))))
        backpack = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
        backpack.click()
        shirt = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
        shirt.click()
        onesie = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
        onesie.click()

        cart = driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link")
        cart.click()

        check = driver.find_element(By.ID, "checkout")
        check.click()

        name = driver.find_element(By.CSS_SELECTOR,
                                   "#first-name.input_error.form_input")
        name.send_keys("Игорь")

        last_name = driver.find_element(By.CSS_SELECTOR,
                                        "#last-name.input_error.form_input")
        last_name.send_keys("Шевченко")

        postal = driver.find_element(By.CSS_SELECTOR,
                                     "#postal-code.input_error.form_input")
        postal.send_keys("195256")

        next = driver.find_element(By.ID, "continue")
        next.click()

        total = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label")
        assert total.text == "Total: $58.29"


    finally:
        driver.quit()
