import allure

from locators import LoginPageLocators
from pages.base_page import BasePage
from urls import LOGIN_URL
from locators import LoginPageLocators, CommonLocators 


class LoginPage(BasePage):

    @allure.step('Войти в аккаунт') 
    def login(self, email, password):
        self.open(LOGIN_URL)

        self.input_text(LoginPageLocators.EMAIL_INPUT, email)

        self.input_text(LoginPageLocators.PASSWORD_INPUT, password)

        self.click_with_scroll(LoginPageLocators.LOGIN_BUTTON)

        self.wait_until(lambda driver: '/login' not in driver.current_url)