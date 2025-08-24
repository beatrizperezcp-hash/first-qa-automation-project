from selenium.webdriver.common.by import By


class Main_functions_page_object:
    def __init__(self, driver):
       self.driver = driver
       self._button =  "//button[contains(., {})]"
       self.__text_locator =  "//p[contains(., {})]"
       self.__section = "//a[contains(., {})]"

    def click_on_button(self, button_name):
        try:
          button = self.driver.find_element(By.XPATH, self._button.format(button_name))
          button.click()
        except Exception as e:
            raise ValueError(f"There was a problem clicking the button {e}")


    def validate_message_after_clicking_on_login_button(self, message):
        try:
             self.driver.find_element(By.XPATH, self.__text_locator.format(message)).text
        except Exception as e:
            raise ValueError(f"There was a problem finding the message {e}")

    def navigate_to_web_section(self, section_name):
        try:
            section_locator = self.driver.find_element(By.XPATH, self.__section.format(section_name))
            section_locator.click()
        except Exception as e:
            raise ValueError(f"There was a problem locating section {e}")