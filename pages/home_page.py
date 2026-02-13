"""Class Home page"""
from pages.base_page import BasePage

from locators.home_locators import HomeLocators


class HomePage(BasePage):

    def confirm_home_page(self):
        assert self.wait_visible(HomeLocators.LOGOUT).is_displayed()

