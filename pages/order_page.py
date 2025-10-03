from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from data import Url
from datetime import datetime, timedelta
from models.Order import Order


class OrderPage(BasePage):
    COLOR_CHECKBOX_GROUP_NAME = 'Цвет самоката'
    
    def load_page(self):
        self.open_page(Url.ORDER_PAGE)
        return self
    
    def click_btn_next(self):
        self._find_clickable_element(OrderPageLocators.NEXT_BTN).click()
        return self
    
    def click_btn_order_finish(self):
        self._find_clickable_element(OrderPageLocators.FINISH_ORDER_BTN).click()
        return self
    
    def click_btn_submit_order(self):
        self._find_clickable_element(OrderPageLocators.SUBMIT_ORDER_BTN).click()
        return self
    
    def fill_first_name(self, value):
        self._fill_input(OrderPageLocators.FIRST_NAME_INPUT, value)
        return self
        
    def fill_last_name(self, value):
        self._fill_input(OrderPageLocators.LAST_NAME_INPUT, value)
        return self
        
    def fill_address(self, value):
        self._fill_input(OrderPageLocators.ADDRESS_INPUT, value)
        return self
        
    def fill_phone(self, value):
        self._fill_input(OrderPageLocators.PHONE_INPUT, value)
        return self
        
    def fill_subway_station_name(self, value):
        self._fill_search(OrderPageLocators.SUBWAY_STATION_SEARCH, value)
        return self
    
    def fill_delivery_date(self, value):
        self._fill_input_date(OrderPageLocators.DELIVERY_DATE_INPUT, value)
        return self
    
    def fill_delivery_date_as_tomorrow(self):
        tomorrow = datetime.now() + timedelta(days=1)
        self.fill_delivery_date(tomorrow.strftime('%d.%m.%Y'))
        return self
    
    def fill_rent_duration(self, duration: Order.Duration):
        if (duration != None):
            self._fill_select(OrderPageLocators.RENT_DURATION_SELECT, duration.value)
        return self
    
    def fill_color(self, color: Order.Color):
        if (color != None):
            self._fill_checkbox(self.COLOR_CHECKBOX_GROUP_NAME, color.name)
        return self
    
    def fill_comment(self, value):
        self._fill_input(OrderPageLocators.COMMENT_INPUT, value)
        return self
    
    def assert_modal_order_confirmed(self):
        self._assert_modal("Заказ оформлен", ['Посмотреть статус'])
        return True