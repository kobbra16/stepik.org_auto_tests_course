import time
import pytest


def test_add_to_cart_button(browser):
    # Открываем страницу товара
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")

    # Ждем загрузки страницы и проверяем наличие кнопки "Добавить в корзину"
    time.sleep(2)  # Можно заменить на WebDriverWait для более надежного ожидания

    add_to_cart_button = browser.find_element("css selector", ".btn-add-to-basket")

    assert add_to_cart_button.is_displayed(), "Кнопка 'Добавить в корзину' не найдена на странице."