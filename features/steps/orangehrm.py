from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def launchBrowser(context):
    serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
    context.driver = webdriver.Chrome(service=serv_obj)
    context.driver.implicitly_wait(10)

@when('open orange hrm homepage')
def openhomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then('verify that the logo present on page')
def verifylogo(context):
    status = context.driver.find_element(By.XPATH, "//img[@alt='company-branding']").is_displayed()
    assert status is True


@then('close browser')
def closebrowser(context):
    context.driver.close()

