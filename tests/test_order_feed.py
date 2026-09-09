import allure

from pages.feed_page import FeedPage
from pages.main_page import MainPage
from urls import BASE_URL, FEED_URL


@allure.feature('Лента заказов')
class TestOrderFeed:

    @allure.title(
        'При создании заказа увеличивается счётчик '
        'Выполнено за всё время'
    )
    def test_total_orders_counter_increases(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        feed_page = FeedPage(authorized_driver)

        feed_page.open(FEED_URL)
        counter_before = feed_page.get_total_count()

        main_page.open(BASE_URL)
        main_page.create_order()
        main_page.close_order_modal()

        feed_page.open(FEED_URL)
        feed_page.wait_total_count_increased(counter_before)

        assert feed_page.get_total_count() > counter_before

    @allure.title(
        'При создании заказа увеличивается счётчик '
        'Выполнено за сегодня'
    )
    def test_today_orders_counter_increases(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        feed_page = FeedPage(authorized_driver)

        feed_page.open(FEED_URL)
        counter_before = feed_page.get_today_count()

        main_page.open(BASE_URL)
        main_page.create_order()
        main_page.close_order_modal()

        feed_page.open(FEED_URL)
        feed_page.wait_today_count_increased(counter_before)

        assert feed_page.get_today_count() > counter_before

    @allure.title('Номер нового заказа появляется в разделе В работе')
    def test_created_order_appears_in_progress(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        feed_page = FeedPage(authorized_driver)

        main_page.open(BASE_URL)

        order_number = main_page.create_order()
        main_page.close_order_modal()

        feed_page.open(FEED_URL)

        assert feed_page.wait_order_in_progress(order_number)