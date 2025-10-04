from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from data import Url
from datetime import datetime, timedelta
from models.Order import Order
import allure

class OrderPage(BasePage):
    COLOR_CHECKBOX_GROUP_NAME = 'Цвет самоката'
    
    @allure.step('Открываем страницу заказа')
    def load_page(self):
        self.open_page(Url.ORDER_PAGE)
        return self
    
    @allure.step('Нажимаем на кнопку Далее')
    def click_btn_next(self):
        self._find_clickable_element(OrderPageLocators.NEXT_BTN).click()
        return self
    
    @allure.step('Нажимаем на кнопку Заказать')
    def click_btn_order_finish(self):
        self._find_clickable_element(OrderPageLocators.FINISH_ORDER_BTN).click()
        return self
    
    @allure.step('Нажимаем на кнопку Да при вопросе Хотите оформить заказ?')
    def click_btn_submit_order(self):
        self._find_clickable_element(OrderPageLocators.SUBMIT_ORDER_BTN).click()
        return self
    
    @allure.step('Заполняем Имя')
    def fill_first_name(self, value):
        self._fill_input(OrderPageLocators.FIRST_NAME_INPUT, value)
        return self
    
    @allure.step('Заполняем Фамилия')    
    def fill_last_name(self, value):
        self._fill_input(OrderPageLocators.LAST_NAME_INPUT, value)
        return self
    
    @allure.step('Заполняем Адрес: куда привезсти заказ')
    def fill_address(self, value):
        self._fill_input(OrderPageLocators.ADDRESS_INPUT, value)
        return self
    
    @allure.step('Заполняем Телефон')
    def fill_phone(self, value):
        self._fill_input(OrderPageLocators.PHONE_INPUT, value)
        return self
     
    @allure.step('Заполняем Станция метро')
    def fill_subway_station_name(self, value):
        self._fill_search(OrderPageLocators.SUBWAY_STATION_SEARCH, value)
        return self
    
    @allure.step('Заполняем Дату доставки')
    def fill_delivery_date(self, value):
        self._fill_input_date(OrderPageLocators.DELIVERY_DATE_INPUT, value)
        return self
    
    @allure.step('Заполняем Дату доставки завтрашним днем')
    def fill_delivery_date_as_tomorrow(self):
        tomorrow = datetime.now() + timedelta(days=1)
        self.fill_delivery_date(tomorrow.strftime('%d.%m.%Y'))
        return self
    
    @allure.step('Заполняем Срок аренды')
    def fill_rent_duration(self, duration: Order.Duration):
        if (duration != None):
            self._fill_select(OrderPageLocators.RENT_DURATION_SELECT, duration.value)
        return self
    
    @allure.step('Заполняем Цвет')
    def fill_color(self, color: Order.Color):
        if (color != None):
            self._fill_checkbox(self.COLOR_CHECKBOX_GROUP_NAME, color.name)
        return self
    
    @allure.step('Заполняем Комментарий')
    def fill_comment(self, value):
        self._fill_input(OrderPageLocators.COMMENT_INPUT, value)
        return self
    
    @allure.step('Проверяем что появилось окно Заказ оформлен')
    def assert_modal_order_confirmed(self):
        self._assert_modal("Заказ оформлен", ['Посмотреть статус'])
        return True
    
    @allure.step('Проверяем клик на лого скутера')
    def assert_navigation_logo_scooter(self):
        self._find_clickable_element(OrderPageLocators.LOGO_SCOOTER).click()
        self.assert_current_page_url(Url.MAIN_PAGE)
        return True
    
    @allure.step('Проверяем клик на лого яндекса')        
    def assert_navigation_logo_yandex(self):
        self._find_clickable_element(OrderPageLocators.LOGO_YANDEX).click()
        self.switch_to_tab(-1)
        self.assert_current_page_url(Url.DZEN)
        return True
