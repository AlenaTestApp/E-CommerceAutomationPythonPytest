"""WebDriver setup and browser StartUp TearDown logic"""

from selenium import webdriver


def create_driver():
    # driver creation and browser startup
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

