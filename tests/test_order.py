import pytest
import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
from models.Order import Order


@allure.feature("Страница заказа самоката")
class TestOrder:
    
    order_data = [
        (
            Order() 
                .set_first_name("Иван")
                .set_last_name("Ясногорский")
                .set_address("ул. Ленина д.125 кв.75")
                .set_subway_station("Беляево")
                .set_phone("89264445566")
                .set_rent_duration(Order.Duration.FOUR_DAYS)
                .set_color(Order.Color.grey),
            True
        ),
        (
            Order() 
                .set_first_name("Петр")
                .set_last_name("Петров")
                .set_address("пр. Мира 10")
                .set_subway_station("ВДНХ")
                .set_rent_duration(Order.Duration.TWO_DAYS)
                .set_phone("89151234567"),
            False
        )
    ]
    
    @allure.title("Позитивный сценарий заказа самоката")
    @pytest.mark.parametrize("order_info, is_header_button", order_data)
    def test_positive_order_scooter(self, driver, order_info: Order, is_header_button: bool):
        page = MainPage(driver)
        page.open_order_page(is_header_button)
        page.fill_first_name(order_info.get_first_name())
        page.fill_last_name(order_info.get_last_name())
        page.fill_address(order_info.get_address())
        page.fill_subway_station_name(order_info.get_subway_station())
        page.fill_phone(order_info.get_phone())
        page.click_btn_next()
        page.fill_delivery_date_as_tomorrow()
        page.fill_rent_duration(order_info.get_rent_duration())
        page.fill_color(order_info.get_color())
        page.fill_comment(order_info.get_comment())
        page.click_btn_order_finish()
        page.click_btn_submit_order()
        assert page.assert_modal_order_confirmed()
        
    @allure.title("При клике на лого самоката открывается главная страница")   
    def test_navigation_logo_scooter(self, driver):
        page = OrderPage(driver)
        page.load_page()
        assert page.assert_navigation_logo_scooter()
    
    @allure.title("При клике на лого яндекса - перекидывает на страницу дзена")   
    def test_navigation_logo_yandex(self, driver):
        page = OrderPage(driver)
        page.load_page()
        assert page.assert_navigation_logo_yandex()
