import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step('Открыть страницу {url}')
    def open(self, url):
        self.driver.get(url)

    @allure.step('Кликнуть по элементу')
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step('Дождаться видимости элемента')
    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Дождаться URL {url}')
    def wait_for_url(self, url):
        self.wait.until(EC.url_to_be(url))

    def get_text(self, locator):
        return self.wait_for_visible(locator).text

    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Дождаться исчезновения элемента')
    def wait_for_invisible(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step('Перетащить элемент')
    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait.until(EC.visibility_of_element_located(source_locator))
        target = self.wait.until(EC.visibility_of_element_located(target_locator))

        browser_name = self.driver.capabilities.get('browserName', '').lower()

        if browser_name == 'firefox':
            self.driver.execute_script(
                """
                const source = arguments[0];
                const target = arguments[1];

                const dataTransfer = new DataTransfer();

                source.dispatchEvent(
                    new DragEvent('dragstart', {bubbles: true, cancelable: true, dataTransfer: dataTransfer})
                );

                target.dispatchEvent(
                    new DragEvent('dragenter', {bubbles: true, cancelable: true, dataTransfer: dataTransfer})
                );

                target.dispatchEvent(
                    new DragEvent('dragover', {bubbles: true, cancelable: true, dataTransfer: dataTransfer})
                );

                target.dispatchEvent(
                    new DragEvent('drop', {bubbles: true, cancelable: true, dataTransfer: dataTransfer})
                );

                source.dispatchEvent(
                    new DragEvent('dragend', {bubbles: true, cancelable: true, dataTransfer: dataTransfer})
                );
                """,
                source,
                target
            )
        else:
            ActionChains(self.driver).drag_and_drop(source, target).perform()

    @allure.step('Ввести текст')
    def input_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def wait_until(self, condition):
        return self.wait.until(condition)

    @allure.step('Кликнуть по элементу с прокруткой')
    def click_with_scroll(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

        element = self.wait.until(EC.element_to_be_clickable(locator))

        try:
            element.click()
        except ElementClickInterceptedException:
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Закрыть модальное окно, если оно открыто')
    def close_modal_if_visible(self, overlay_locator, close_locator):
        overlays = self.driver.find_elements(*overlay_locator)

        if not overlays:
            return

        if not overlays[0].is_displayed():
            return

        close_button = self.wait.until(EC.presence_of_element_located(close_locator))

        self.driver.execute_script("arguments[0].click();", close_button)

        self.wait.until(EC.invisibility_of_element_located(overlay_locator))