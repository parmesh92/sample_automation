import pytest
from pywinauto import Desktop
from pages.actions.hp_app_actions import HPAccountActions

@pytest.fixture
def hp_app():
    desktop = Desktop(backend="uia")
    return HPAccountActions(desktop)
