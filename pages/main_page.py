from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import Url
import allure


class MainPage(BasePage):
    @allure.step('Нажимаем на кнопку заказать в заголовке')
    def click_order_btn_header(self):
        """
        Нажать на кнопку заказать в заголовке
        """
        self._find_clickable_element(MainPageLocators.ORDER_BTN_HEADER).click()
        return self
    
    @allure.step('Нажимаем на кнопку заказать в футере')
    def click_order_btn_footer(self):
        """
        Нажать на кнопку заказать внизу страницы
        """
        self._scroll_to_element(MainPageLocators.ORDER_BTN_FOOTER).click()
        return self
    
    @allure.step('Открываем главную страницу')
    def load_page(self):
        self.open_page(Url.MAIN_PAGE)
        return self
    
    @allure.step('Переходим на страницу заказа в зависимости от типа кнопки')
    def open_order_page(self, is_header_button):
        if is_header_button:
            self.click_order_btn_header()
        else:
            self.click_order_btn_footer()
            
    @allure.step('Проверяем что при клике на вопрос открылся ожидаемый ответ')
    def assert_question(self, question_text, answer_text):
        self._scroll_to_element(MainPageLocators.FAQ)
        question = self._find_clickable_element(MainPageLocators.get_question_locator(question_text))
        assert question.get_attribute("aria-expanded") == "false"
        answer = self._find_element(MainPageLocators.get_answer_locator_by_question(question_text))
        assert answer.get_attribute("hidden") == "true"
        question.click()
        assert question.get_attribute("aria-expanded") == "true"
        assert answer.get_attribute("hidden") == None
        assert answer.text == answer_text

