from selenium.webdriver.common.by import By


class MainPageLocators:
    """
    Локаторы для главной страницы
    """
    ORDER_BTN_HEADER = (By.XPATH, "//div[contains(@class, 'Header')]/button[text()='Заказать']")
    ORDER_BTN_FOOTER = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")
    FAQ = (By.XPATH, "//div[contains(@class, 'FAQ')]")

    @staticmethod
    def get_question_locator(question):
        return (By.XPATH, f"//div[contains(@class, 'accordion__button') and text()='{question}']")
    
    @staticmethod
    def get_answer_locator_by_question(question):
        return (By.XPATH,  f"//div[@class='accordion__button' and text()='{question}']"
            "/ancestor::div[@data-accordion-component='AccordionItem']"  # Поднимаемся до родительского AccordionItem
            "//div[@data-accordion-component='AccordionItemPanel']")  # Находим панель с ответом
