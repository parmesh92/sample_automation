import re
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.retry import retry
from utils.logger import log_step
from config.config import Mailsac_URL, MAX_WEB_WAIT
from pages.locators.mailsac_locators import MailsacLocators


class MailsacActions:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, MAX_WEB_WAIT)

    @retry(attempts=5, delay=5)
    def fetch_otp(self, mailbox, timeout=40, poll=5):
        self.driver.get(Mailsac_URL)

        field = self.wait.until(EC.presence_of_element_located(MailsacLocators.MAILBOX_FIELD))
        field.send_keys(mailbox)

        self.driver.find_element(*MailsacLocators.CHECK_MAIL_BTN).click()

        start = time.time()
        while time.time() - start < timeout:
            try:
                row = WebDriverWait(self.driver, poll).until(
                    EC.element_to_be_clickable(MailsacLocators.EMAIL_ROW)
                )
                row.click()
                break
            except:
                self.driver.find_element(*MailsacLocators.CHECK_MAIL_BTN).click()

        body = self.wait.until(EC.presence_of_element_located(MailsacLocators.EMAIL_BODY)).text
        match = re.search(r"\b(\d{6})\b", body)

        return match.group(1) if match else None
