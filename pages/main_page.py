import allure

from locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Перейти в Конструктор')
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_LINK)

    @allure.step('Перейти в Ленту заказов')
    def click_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_LINK)

    def is_main_title_visible(self):
        return self.wait_for_visible(MainPageLocators.MAIN_TITLE).is_displayed()


    @allure.step('Открыть детали ингредиента')
    def click_ingredient(self):
        self.click(MainPageLocators.BUN_INGREDIENT)

    def is_ingredient_modal_visible(self):
        return self.wait_for_visible(MainPageLocators.INGREDIENT_DETAILS_MODAL).is_displayed()

    @allure.step('Закрыть окно деталей ингредиента')
    def close_ingredient_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)

    def wait_ingredient_modal_closed(self):
        return self.wait_for_invisible(MainPageLocators.INGREDIENT_DETAILS_MODAL)

    def get_ingredient_counter_value(self):
        elements = self.driver.find_elements(*MainPageLocators.INGREDIENT_COUNTER)

        if not elements:
            return 0
        return int(elements[0].text)

    @allure.step('Добавить ингредиент в заказ')
    def add_ingredient_to_order(self):
        self.drag_and_drop(MainPageLocators.BUN_INGREDIENT, MainPageLocators.ORDER_BASKET)

    def wait_counter_increased(self, previous_value):
        self.wait.until(lambda driver:
            self.get_ingredient_counter_value() > previous_value)

    @allure.step('Оформить заказ')
    def click_create_order(self):
        self.click_with_scroll(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Получить номер созданного заказа')
    def get_created_order_number(self):
        self.wait_for_visible(MainPageLocators.ORDER_IDENTIFIER_LABEL)

        def order_number_loaded(driver):
            text = driver.find_element(*MainPageLocators.ORDER_ID).text.strip()

            if text.isdigit() and text != '9999':
                return text

            return False

        return self.wait_until(order_number_loaded)

    @allure.step('Закрыть окно созданного заказа')
    def close_order_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step('Создать заказ')
    def create_order(self):
        self.add_ingredient_to_order()
        self.click_create_order()

        return self.get_created_order_number()