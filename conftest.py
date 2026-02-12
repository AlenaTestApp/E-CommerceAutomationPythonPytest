"""PyTest Fixures for Driver setup"""

import pytest
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")

from utils.driver import create_driver
from config.configs import BASE_URL
from pages.login_page import LoginPage


class App:
    def __init__(self, driver):
        self.login_page = LoginPage(driver)


@pytest.fixture()
def driver():
    driver = create_driver()
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture()
def app(driver):
    return App(driver)
