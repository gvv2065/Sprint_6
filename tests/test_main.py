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
    def test_order_btn_header_click_is_open_order_page(self, main_page):
        main_page.load_page()
        main_page.click_order_btn_header()
        main_page.assert_current_page_url(Url.ORDER_PAGE)
    
    @allure.title("Успешный переход на форму заказа из кнопки внизу страницы")
    def test__order_btn_header_click_is_open_order_page(self, main_page):
        main_page.load_page()
        main_page.click_order_btn_footer()
        main_page.assert_current_page_url(Url.ORDER_PAGE)

    faq_data = [
        ("Сколько это стоит? И как оплатить?", "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        ("Хочу сразу несколько самокатов! Так можно?", "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        ("Как рассчитывается время аренды?", "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        ("Можно ли заказать самокат прямо на сегодня?", "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        ("Можно ли продлить заказ или вернуть самокат раньше?", "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        ("Вы привозите зарядку вместе с самокатом?", "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
        ("Можно ли отменить заказ?", "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        ("Я жизу за МКАДом, привезёте?", "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
    ]
    @pytest.mark.parametrize("expected_question, expected_answer", faq_data)
    def test_faq_component_question_click_will_expand_expected_answer(self, expected_question, expected_answer, main_page):
        main_page.load_page()
        main_page.assert_question(expected_question, expected_answer)