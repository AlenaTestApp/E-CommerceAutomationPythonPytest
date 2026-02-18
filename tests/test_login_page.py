"""Login Page Test suite"""
from test_data.data import *
import pytest


@pytest.mark.smoke
def test_login_valid_credentials(app):
    # Test Login with valid User's credentials
    app.login_page.login(USER_NAME, USER_PASSWORD)
    assert NAME in app.login_page.get_greeting_text()


def test_login_invalid_credentials(app):
    # Validate error message when User logs in with invalid credentials
    error_message = "Your email or password is incorrect!"
    app.login_page.login(USER_NAME, INVALID_PASSWORD)
    assert error_message in app.login_page.invalid_login_error()


def test_logout(app):
    # Validate User successfully logged out and redirected to Login page
    app.login_page.login(USER_NAME, USER_PASSWORD)
    app.login_page.logout()


