import allure

from locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):

    def is_feed_title_visible(self):
        return self.wait_for_visible(FeedPageLocators.FEED_TITLE).is_displayed()

    def get_total_count(self):
        return int(self.get_text(FeedPageLocators.TOTAL_COUNT))

    def get_today_count(self):
        return int(self.get_text(FeedPageLocators.TODAY_COUNT))

    @allure.step('Дождаться увеличения общего счётчика')
    def wait_total_count_increased(self, previous_value):
        self.wait_until(lambda driver:
            self.get_total_count() > previous_value)

    @allure.step('Дождаться увеличения счётчика за сегодня')
    def wait_today_count_increased(self, previous_value):
        self.wait_until(lambda driver:
            self.get_today_count() > previous_value)

    def get_in_progress_orders(self):
        elements = self.driver.find_elements(*FeedPageLocators.IN_PROGRESS_ORDERS)

        return [
            element.text.strip()
            for element in elements
        ]

    @staticmethod
    def normalize_order_number(number):
        number = number.strip().lstrip('#').lstrip('0')

        return number or '0'

    @allure.step('Дождаться появления заказа в разделе В работе')
    def wait_order_in_progress(self, order_number):
        expected = self.normalize_order_number(order_number)

        def order_is_present(driver):
            orders = self.get_in_progress_orders()

            return any(
                self.normalize_order_number(order) == expected
                for order in orders
            )

        self.wait_until(order_is_present)

        return True