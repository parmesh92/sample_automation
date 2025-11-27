from utils.helpers import generate_random_mailbox
from utils.logger import log_step


def test_hp_account_creation(hp_app, mailsac):
    mailbox = generate_random_mailbox()
    email = f"{mailbox}@mailsac.com"

    log_step(f"Generated email: {email}")

    hp_app.launch_and_navigate_to_signup()
    hp_app.fill_and_submit_account_form(email)

    otp = mailsac.fetch_otp(mailbox)
    assert otp, "OTP could not be retrieved"

    hp_app.complete_web_verification(otp)

    log_step("🎉 Account creation test completed successfully!")
