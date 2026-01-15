import allure
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка итоговой стоимости заказа")
@allure.description(
    "Авторизация, добавление товаров в корзину и проверка итоговой суммы заказа"
)
def test_shop_total_price(driver):

    login = LoginPage(driver)
    products = ProductsPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    with allure.step("Открыть сайт магазина"):
        login.open()

    with allure.step("Авторизоваться пользователем standard_user"):
        login.login("standard_user", "secret_sauce")

    with allure.step("Добавить товары в корзину"):
        products.add_product("Sauce Labs Backpack")
        products.add_product("Sauce Labs Bolt T-Shirt")
        products.add_product("Sauce Labs Onesie")

    with allure.step("Перейти в корзину"):
        products.open_cart()

    with allure.step("Нажать Checkout"):
        cart.checkout()

    with allure.step("Заполнить данные для оформления заказа"):
        checkout.fill_form("Ivan", "Ivanov", "12345")

    with allure.step("Проверить, на какой странице мы находимся"):
        print(driver.current_url)

    with allure.step("Получить итоговую стоимость"):
        total = checkout.get_total()

    with allure.step("Проверить, что итоговая сумма равна $58.29"):
        assert total == 58.29
