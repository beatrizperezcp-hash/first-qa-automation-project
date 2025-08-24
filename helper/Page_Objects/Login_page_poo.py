from selenium.webdriver.common.by import By


class Login_page_object:
    def __init__(self, driver):
        self.driver = driver
        self.__login_field_locator = '//label[normalize-space(text())="{}"]/following::input'

    def open_url(self, url):
        self.driver.get(f"https://{url}")

    def fill_login_form(self, field, value):
        if field.lower() == "username":
            username_field = self.driver.find_element(By.XPATH, self.__login_field_locator.format("Username"))
            username_field.send_keys(value)
        elif field.lower() == "password":
            password_field = self.driver.find_element(By.XPATH, self.__login_field_locator.format("Password"))
            password_field.send_keys(value)
        else:
            raise ValueError(f"There was a problem filling the field {field}")
