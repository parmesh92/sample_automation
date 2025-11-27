class HPAppLocators:
    APP_TITLE = ".*HP Smart.*"
    BTN_MANAGE_ACCOUNT = {"title": "Manage HP Account", "auto_id": "HpcSignedOutIcon", "control_type": "Button"}
    BTN_CREATE_ACCOUNT = {"auto_id": "HpcSignOutFlyout_CreateBtn", "control_type": "Button"}

    WEB_TITLE = ".*HP account.*"
    FIELD_FIRST_NAME = {"auto_id": "firstName", "control_type": "Edit"}
    FIELD_LAST_NAME = {"auto_id": "lastName", "control_type": "Edit"}
    FIELD_EMAIL = {"auto_id": "email", "control_type": "Edit"}
    FIELD_PASSWORD = {"auto_id": "password", "control_type": "Edit"}
    BTN_CREATE_SUBMIT = {"auto_id": "sign-up-submit", "control_type": "Button"}

    FIELD_OTP_CODE = {"auto_id": "code", "control_type": "Edit"}
    BTN_VERIFY_CODE = {"auto_id": "submit-code", "control_type": "Button"}
