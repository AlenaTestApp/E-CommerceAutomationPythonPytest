"""Class Login page"""
from pages.base_page import BasePage
import time

from locators.login_locators import LoginLocators
from test_data.data import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def login(self, user_name, user_password):
        self.click(LoginLocators.LOGIN_SIGNUP)
        self.type(LoginLocators.USERNAME, user_name)
        self.type(LoginLocators.PASSWORD, user_password)
        self.click(LoginLocators.LOGIN_BTN)

    def get_greeting_text(self):
        login_confirmation = self.wait_visible(LoginLocators.LOGIN_CONFIRMATION)
        return login_confirmation.text


