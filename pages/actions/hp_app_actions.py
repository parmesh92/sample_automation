import time
import pyperclip
from pywinauto import Desktop, keyboard
from utils.retry import retry
from utils.logger import log_step
from pages.locators.hp_app_locators import HPAppLocators
from config.config import MAX_APP_WAIT, MAX_WEB_WAIT, DEFAULT_PASSWORD


class HPAccountActions:

    def __init__(self, desktop: Desktop):
        self.desktop = desktop

    @retry(attempts=3, delay=3)
    def launch_and_navigate_to_signup(self):
        log_step("Launching HP Smart…")
        keyboard.send_keys("{VK_LWIN}HP Smart{ENTER}")

        main = self.desktop.window(title_re=HPAppLocators.APP_TITLE)
        main.wait("exists enabled visible ready", timeout=MAX_APP_WAIT)
        main.set_focus()

        manage = main.child_window(**HPAppLocators.BTN_MANAGE_ACCOUNT)
        manage.click_input()

        create = main.child_window(**HPAppLocators.BTN_CREATE_ACCOUNT)
        create.click_input()

        log_step("Navigated to account creation screen")

    @retry(attempts=3, delay=2)
    def fill_and_submit_account_form(self, email):
        browser = self.desktop.window(title_re=HPAppLocators.WEB_TITLE)
        browser.wait("visible ready enabled", timeout=MAX_WEB_WAIT)

        browser.child_window(**HPAppLocators.FIELD_FIRST_NAME).type_keys("John")
        browser.child_window(**HPAppLocators.FIELD_LAST_NAME).type_keys("Doe")
        browser.child_window(**HPAppLocators.FIELD_EMAIL).type_keys(email)
        browser.child_window(**HPAppLocators.FIELD_PASSWORD).type_keys(DEFAULT_PASSWORD)

        browser.child_window(**HPAppLocators.BTN_CREATE_SUBMIT).click_input()
        log_step("Account form submitted")

    @retry(attempts=3, delay=3)
    def complete_web_verification(self, otp):
        browser = self.desktop.window(title_re=HPAppLocators.WEB_TITLE)
        browser.wait("exists visible ready", timeout=MAX_WEB_WAIT)

        pyperclip.copy(otp)
        otp_box = browser.child_window(**HPAppLocators.FIELD_OTP_CODE)
        otp_box.click_input()
        otp_box.type_keys("^v")

        browser.child_window(**HPAppLocators.BTN_VERIFY_CODE).click_input()
        log_step("OTP verification completed")
