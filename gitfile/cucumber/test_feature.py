

from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

scenarios('google_search.feature')

@given("some condition")
def some_condition():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")


@when("some action")
def some_action():
    driver.find_element(By.ID, 'email').send_keys('kugan@123.com')
    driver.find_element(By.ID,'pass').send_keys('kugan123')
    driver.find_element(By.NAME,'login')


@then("some result")
def some_result():
    pass

