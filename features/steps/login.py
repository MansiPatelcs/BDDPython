from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@given('I launch Chrome browser')
def launchbrowser(context):
    serv_obj= Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
    context.driver=webdriver.Chrome(service=serv_obj)
    context.driver.implicitly_wait(10)

@when('I open orange HRM Homepage')
def homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context,user,pwd):
    context.driver.find_element(By.NAME,"username").send_keys(user)
    context.driver.find_element(By.NAME,"password").send_keys(pwd)

@when('Click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//button[@type='submit']").click()


@then('User must successfully login to the Dashboard page')
def step_impl(context):
    try:
        a=context.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
    except:
        context.driver.close()
        assert False,"Test Failed"

    if a=="Dashboard":
        context.driver.close()
        assert True, "Test Passed"
