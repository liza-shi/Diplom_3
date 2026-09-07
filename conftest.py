import pytest
import requests

from selenium import webdriver

from helpers import generate_user_data
from pages.login_page import LoginPage
from urls import (BASE_URL, REGISTER_USER_URL, DELETE_USER_URL)


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()

    browser.set_window_size(1440, 1000)
    browser.get(BASE_URL)

    yield browser

    browser.quit()


@pytest.fixture
def registered_user():
    user_data = generate_user_data()

    response = requests.post(REGISTER_USER_URL, json=user_data)

    assert response.status_code == 200

    response_data = response.json()
    access_token = response_data['accessToken']

    yield user_data

    requests.delete(
        DELETE_USER_URL,
        headers={'Authorization': access_token})


@pytest.fixture
def authorized_driver(driver, registered_user):
    login_page = LoginPage(driver)

    login_page.login(registered_user['email'], registered_user['password'])

    return driver