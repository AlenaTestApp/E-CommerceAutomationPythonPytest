"""Class Login page"""
from pages.base_page import BasePage
import time

from locators.login_locators import LoginLocators
from locators.home_locators import HomeLocators
from pages.home_page import HomePage


class LoginPage(BasePage):
    def login(self, user_name, user_password):
        self.click(LoginLocators.LOGIN_SIGNUP)
        self.type(LoginLocators.USERNAME, user_name)
        self.type(LoginLocators.PASSWORD, user_password)
        self.click(LoginLocators.LOGIN_BTN)

    def get_greeting_text(self):
        login_confirmation = self.wait_visible(LoginLocators.LOGIN_CONFIRMATION)
        return login_confirmation.text

    def invalid_login_error(self):
        login_error = self.wait_visible(LoginLocators.LOGIN_ERROR)
        return login_error.text

    def logout(self):
        # function confirms that User is on Home page and clicks Logout btn
        # after logout verifies user is redirected to Login page and Login button is visible
        home_page = HomePage(self.driver)
        home_page.confirm_home_page()
        self.click(HomeLocators.LOGOUT)
        assert "/login" in self.driver.current_url
        assert self.wait_visible(LoginLocators.LOGIN_BTN).is_displayed()





