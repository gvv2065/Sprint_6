import pytest
import allure
from ..pages.main_page import MainPage
from ..data import Url


@allure.feature("Login")
class TestMain:
    
    @pytest.fixture
    def main_page(self, driver):
        """Фикстура для создания объекта страницы логина"""
        return MainPage(driver)
    
    @allure.title("Успешный переход на форму заказа из кнопки в заголовке")
    def test_successful_order_btn_header_click_is_open_order_page(self, main_page):
        main_page.load_page()
        main_page.click_order_btn_header()
        main_page.assert_current_page_url(Url.ORDER_PAGE)
    
    @allure.title("Успешный переход на форму заказа из кнопки внизу страницы")
    def test_successful_order_btn_header_click_is_open_order_page(self, main_page):
        main_page.load_page()
        main_page.click_order_btn_footer()
        main_page.assert_current_page_url(Url.ORDER_PAGE)