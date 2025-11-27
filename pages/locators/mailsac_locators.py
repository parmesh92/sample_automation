from selenium.webdriver.common.by import By

class MailsacLocators:
    MAILBOX_FIELD = (By.XPATH, "//input[@placeholder='mailbox']")
    CHECK_MAIL_BTN = (By.XPATH, "//button[contains(text(),'Check the mail!')]")
    EMAIL_ROW = (By.XPATH, "//tr[contains(@class,'clickable')][1]")
    EMAIL_BODY = (By.CSS_SELECTOR, "#emailBody")
