import pytest
from selenium import webdriver
from pages.actions.mailsac_actions import MailsacActions

@pytest.fixture(scope="session")
def driver():
    d = webdriver.Chrome()
    yield d
    d.quit()

@pytest.fixture
def mailsac(driver):
    return MailsacActions(driver)
