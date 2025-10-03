from selenium.webdriver.common.by import By

class OrderPageLocators:
    """
    Локаторы для страницы заказа самоката
    """
    # Первый шаг
    NEXT_BTN = (By.XPATH, "//button[text()='Далее']")
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    SUBWAY_STATION_SEARCH = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    
    # Второй шаг
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_DURATION_SELECT = (By.XPATH, "//div[contains(@class,'Dropdown-placeholder') and text()='* Срок аренды']")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    FINISH_ORDER_BTN = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    SUBMIT_ORDER_BTN = (By.XPATH, "//button[text()='Да']")
    
