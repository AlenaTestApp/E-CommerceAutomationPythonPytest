"""Home Page Locators"""
from selenium.webdriver.common.by import By


class HomeLocators:
    LOGOUT = (By.XPATH, "//a[normalize-space()='Logout']")
