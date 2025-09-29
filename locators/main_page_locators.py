from selenium.webdriver.common.by import By


class MainPageLocators:
    """
    Локаторы для главной страницы
    """
    ORDER_BTN_HEADER = (By.XPATH, "//div[contains(@class, 'Header')]/button[text()='Заказать']")
    ORDER_BTN_FOOTER = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")
