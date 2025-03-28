import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()