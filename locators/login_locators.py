"""Login Page Locators"""
from selenium.webdriver.common.by import By


class LoginLocators:
    # Login Page Locators
    LOGIN_SIGNUP = (By.XPATH, "//a[contains(text(), 'Login')]")
    USERNAME = (By.XPATH, "//input[@name = 'email']")
    PASSWORD = (By.XPATH, "//input[@name = 'password']")
    LOGIN_BTN = (By.XPATH, "//button[contains(text(), 'Login')]")
    LOGIN_CONFIRMATION = (By.XPATH, "//*[normalize-space(text())='Logged in as']")
    LOGIN_ERROR = (By.XPATH, "//form[@action='/login']//p[contains(.,'incorrect')]")
