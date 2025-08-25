import time

from selenium.webdriver.common.by import By
from helper.utils import highlight_element as highlight

class Main_functions_page_object:
    def __init__(self, driver):
       self.driver = driver
       self._button =  "//button[contains(., {})]"
       self.__text_locator =  "//p[contains(., {})]"
       self.__message_header = "//h6[normalize-space(.)={} and ancestor::header]"


    def click_on_button(self, button_name):
        try:
          button = self.driver.find_element(By.XPATH, self._button.format(button_name))
          highlight(self.driver, button)
          button.click()
        except Exception as e:
            raise ValueError(f"There was a problem clicking the button {e}")


