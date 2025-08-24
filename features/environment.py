from selenium import webdriver
import os

def before_all(context):
    context.driver = webdriver.Edge()
    context.driver.maximize_window()


def after_step(context, step):
    ruta = os.path.join(os.getcwd(), "/reports")
    context.driver.save_screenshot(f"{ruta}/{step.name}.png")



def after_all(context):
    context.driver.quit()