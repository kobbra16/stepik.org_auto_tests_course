import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("--language")

    # Настройка опций для браузера с указанным языком
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    # Запуск браузера
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Choose language for testing")