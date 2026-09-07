from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_LINK = (By.XPATH, "//a[.//*[contains(normalize-space(), 'Конструктор')]]")

    ORDER_FEED_LINK = (By.XPATH,
        "//a[.//*[contains(normalize-space(), 'Лента') "
        "and contains(normalize-space(), 'заказ')]]")

    MAIN_TITLE = (By.XPATH, "//*[contains(normalize-space(), 'Соберите бургер')]")

    BUN_INGREDIENT = (By.XPATH, "//p[normalize-space()='Флюоресцентная булка R2-D3']")

    INGREDIENT_DETAILS_MODAL = (By.XPATH, "//h2[normalize-space()='Детали ингредиента']")

    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'close')]")

    INGREDIENT_COUNTER = (By.XPATH,
        "//p[normalize-space()='Флюоресцентная булка R2-D3']"
        "/ancestor::a[1]//p[contains(@class, 'num')]")

    ORDER_BASKET = (By.XPATH,
        "//span[contains(@class, 'constructor-element__text') "
        "and contains(normalize-space(), 'Перетяните булочку сюда')]")
    
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[normalize-space()='Оформить заказ']")

    ORDER_IDENTIFIER_LABEL = (By.XPATH, "//*[normalize-space()='идентификатор заказа']")

    ORDER_ID = (By.XPATH,
        "//*[normalize-space()='идентификатор заказа']"
        "/preceding-sibling::*[1]")


class FeedPageLocators:
    FEED_TITLE = (By.XPATH, "//h1[contains(normalize-space(), 'Лента заказов')]")


    TOTAL_COUNT = (By.XPATH,
        "//*[contains(normalize-space(), 'Выполнено за') "
        "and contains(normalize-space(), 'время')]"
        "/following-sibling::*[1]")

    TODAY_COUNT = (By.XPATH,
        "//*[contains(normalize-space(), 'Выполнено за сегодня')]"
        "/following-sibling::*[1]")

    IN_PROGRESS_ORDERS = (By.XPATH,
        "//*[contains(normalize-space(), 'В работе')]"
        "/following-sibling::ul[1]//li")



class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[normalize-space()='Email']/following::input[1]")

    PASSWORD_INPUT = (By.XPATH, "//label[normalize-space()='Пароль']/following::input[1]")

    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")


class CommonLocators:
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")

    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'close')]")