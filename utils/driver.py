"""WebDriver setup and browser StartUp TearDown logic"""

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver():
    # driver creation and browser startup
    options = Options()

    # CI (Continuous Integration) environment on GitHub runner
    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")           # headless
        options.add_argument("--no-sandbox")             # no-sandbox  for CI
        options.add_argument("--disable-dev-shm-usage")  # disable-dev-shm-usage, use /tmp
        options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    # maximize_window in Local environment
    if os.getenv("CI") != "true":
        driver.maximize_window()

    return driver
