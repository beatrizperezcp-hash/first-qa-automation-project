from selenium.webdriver.common.by import By
from helper.utils import highlight_element as highlight


class Login_page_object:
    def __init__(self, driver):
        self.driver = driver
        self.__login_field_locator = '//label[normalize-space(text())="{}"]/following::input'
        self.__invalid_message = "//span[contains(., {})]"
        self.__text_locator = "//p[contains(., {})]"

    def open_url(self, url):
        self.driver.get(f"https://{url}")

    def fill_login_form(self, field, value):
        if field.lower() == "username":
            username_field = self.driver.find_element(By.XPATH, self.__login_field_locator.format("Username"))
            highlight(self.driver, username_field)
            username_field.send_keys(value)
        elif field.lower() == "password":
            password_field = self.driver.find_element(By.XPATH, self.__login_field_locator.format("Password"))
            highlight(self.driver, password_field)
            password_field.send_keys(value)
        else:
            raise ValueError(f"There was a problem filling the field {field}")

    def validate_invalid_message(self, invalid_message):
        try:
            message_locator = self.driver.find_element(By.XPATH, self.__invalid_message.format(invalid_message))
            highlight(self.driver, message_locator)
            message_cleaned = invalid_message.strip("\"'")
            assert message_cleaned in message_locator.text

        except Exception as e:
            raise ValueError(f"There was a problem finding the message {e}")

    def validate_message_after_clicking_on_login_button(self, message):
        try:
            message_locator = self.driver.find_element(By.XPATH, self.__text_locator.format(message))
            highlight(self.driver, message_locator)
            message_cleaned = message.strip("\"'")
            assert message_cleaned in message_locator.text

        except Exception as e:
            raise ValueError(f"There was a problem finding the message {e}")
