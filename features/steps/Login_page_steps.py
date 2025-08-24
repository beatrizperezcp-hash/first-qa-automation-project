import time

from helper.Page_Objects.Login_page_poo import Login_page_object as login
from helper.Page_Objects.Main_functions_poo import Main_functions_page_object as main_functions
from behave import given, then, when

@given("Open the following url {url}")
def open_web(context, url):
  login_po = login(context.driver)
  login_po.open_url(url)

@when("Fill the following fields")
def fill_login_fields(context):
  time.sleep(5)
  login_po = login(context.driver)
  for i in context.table:
   login_po.fill_login_form(i["field"], i["value"])

@then("Click on button {button_name}")
def fill_login_fields(context, button_name):
   main_functions_steps = main_functions(context.driver)
   main_functions_steps.click_on_button(button_name)


@then("Verify the following message {message}")
def fill_login_fields(context, message):
    time.sleep(5)
    main_functions_steps = main_functions(context.driver)
    main_functions_steps.validate_message_after_clicking_on_login_button(message)


@then("Navigate to the following section {section_name}")
def navigate_to_section(context, section_name):
    time.sleep(5)
    main_functions_steps = main_functions(context.driver)
    main_functions_steps.navigate_to_web_section(section_name)

