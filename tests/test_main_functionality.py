import allure

from pages.main_page import MainPage
from pages.feed_page import FeedPage
from urls import BASE_URL, FEED_URL


@allure.feature('Основная функциональность')
class TestMainFunctionality:

    @allure.title('Переход по клику на Конструктор')
    def test_click_constructor_opens_constructor(self, driver):
        feed_page = FeedPage(driver)
        main_page = MainPage(driver)

        feed_page.open(FEED_URL)
        main_page.click_constructor()

        main_page.wait_for_url(f'{BASE_URL}/')

        assert main_page.is_main_title_visible()

    @allure.title('Переход по клику на Ленту заказов')
    def test_click_order_feed_opens_feed(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.open(BASE_URL)
        main_page.click_order_feed()

        feed_page.wait_for_url(FEED_URL)

        assert feed_page.is_feed_title_visible()


    @allure.title('Открытие окна с деталями ингредиента')
    def test_click_ingredient_opens_details_modal(self, driver):
        main_page = MainPage(driver)

        main_page.open(BASE_URL)
        main_page.click_ingredient()

        assert main_page.is_ingredient_modal_visible()

    @allure.title('Закрытие окна с деталями ингредиента по крестику')
    def test_close_ingredient_details_modal(self, driver):
        main_page = MainPage(driver)

        main_page.open(BASE_URL)
        main_page.click_ingredient()

        assert main_page.is_ingredient_modal_visible()

        main_page.close_ingredient_modal()
        main_page.wait_ingredient_modal_closed()

        assert 'ingredients/' not in main_page.get_current_url()

    @allure.title('Счётчик ингредиента увеличивается после добавления')
    def test_ingredient_counter_increases_after_adding(self, driver):
        main_page = MainPage(driver)

        main_page.open(BASE_URL)

        counter_before = main_page.get_ingredient_counter_value()

        main_page.add_ingredient_to_order()
        main_page.wait_counter_increased(counter_before)

        counter_after = main_page.get_ingredient_counter_value()

        assert counter_after > counter_before