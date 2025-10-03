from selenium.webdriver.common.by import By


class BaseLocators:
    @staticmethod
    def get_search_locator(option):
        return (By.XPATH, f"//li//div[text()='{option}']")
    
    @staticmethod
    def get_option_locator(option):
        return (By.XPATH, f"//div[@role='option' and text()='{option}']")
    
    @staticmethod
    def get_checkbox_locator(checkbox_group_name, value):
        return (By.XPATH, f"""//div[contains(@class,'Checkboxes')]//div[text()='{checkbox_group_name}']
                //ancestor::div[contains(@class,'Checkboxes')]//input[@id='{value}']""")
        
    @staticmethod
    def get_modal_locator(modal_text):
        return (By.XPATH, f"//div[contains(@class,'ModalHeader') and text()='{modal_text}']")
    
    @staticmethod
    def get_modal_button(modal_button_text):
        return (By.XPATH, f"//div[contains(@class,'Modal')]//button[text()='{modal_button_text}']")
