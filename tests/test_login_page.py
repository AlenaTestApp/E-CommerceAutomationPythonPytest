"""Login Page Test suite"""
from test_data.data import *


def test_title(app):
    app.login_page.login(USER_NAME, USER_PASSWORD)
    assert NAME in app.login_page.get_greeting_text()
