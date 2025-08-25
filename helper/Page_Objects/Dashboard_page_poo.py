from selenium.webdriver.common.by import By
from helper.utils import highlight_element as highlight

class Dashboard_page_object:
    def __init__(self, driver):
       self.driver = driver
       self.__title_header = "//h6[normalize-space(.)={} and ancestor::header]"
       self.__section = "//a[contains(., {})]"


    def validate_header_message(self, title):
        try:
            title_locator = self.driver.find_element(By.XPATH, self.__title_header.format(title))
            highlight(self.driver, title_locator)
            message_cleaned = title.strip("\"'")
            assert message_cleaned in title_locator.text

        except Exception as e:
            raise ValueError(f"There was a problem finding the title {e}")

    def navigate_to_web_section(self, section_name):
        try:
            section_locator = self.driver.find_element(By.XPATH, self.__section.format(section_name))
            highlight(self.driver, section_locator)
            section_locator.click()
        except Exception as e:
            raise ValueError(f"There was a problem locating section {e}")