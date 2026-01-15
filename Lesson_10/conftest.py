import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()

    # 🚫 Отключаем уведомления, инфобары и сохранение паролей
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-extensions")
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")

    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        },
    )

    driver = webdriver.Chrome(options=options)

    # маленькая подстраховка для ожиданий
    driver.implicitly_wait(0.5)

    yield driver
    driver.quit()
