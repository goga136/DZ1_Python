from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.shop_page import LoginPage, ProductPage, CartPage, CheckoutPage


def test_shop():
    # Создание драйвера
    driver = webdriver.Firefox()

    # Создание объекта страницы авторизации и выполнение авторизации
    login_page = LoginPage(driver)
    inventory_page = login_page.open().login("standard_user", "secret_sauce")

    # Добавление товаров в корзину на главной странице
    inventory_page \
        .add_backpack_to_cart() \
        .add_bolt_t_shirt_to_cart() \
        .add_onesie_to_cart()

    # Переход в корзину
    cart_page = inventory_page.go_to_cart()

    # Начало оформления заказа
    checkout_page = cart_page.checkout()

    # Заполнение формы данными
    checkout_page \
        .fill_customer_info("Игорь", "Шевченко", "195256") \
        .continue_to_overview()

    # Получение итоговой суммы
    total_text = checkout_page.get_total_amount()

    assert total_text == "Total: $58.29"
    print(f"Тест пройден успешно! Итоговая сумма: {total_text}")

    driver.quit()
