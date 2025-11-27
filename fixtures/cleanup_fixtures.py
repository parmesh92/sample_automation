import pytest
from pywinauto import Desktop
from pages.locators.hp_app_locators import HPAppLocators

@pytest.fixture(autouse=True)
def cleanup():
    yield
    desktop = Desktop(backend="uia")
    try:
        desktop.window(title_re=HPAppLocators.WEB_TITLE).close()
    except: pass
    try:
        desktop.window(title_re=HPAppLocators.APP_TITLE).close()
    except: pass
