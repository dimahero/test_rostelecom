from selenium.webdriver.common.by import By

class AuthLocators:
    AUTH_EMAIL = (By.ID, "username")
    AUTH_PASS = (By.ID, "password")
    AUTH_TELNUMBER = (By.ID, "username")
    AUTH_LOGIN = (By.ID, "username")
    AUTH_PERSACCOUNT = (By.CLASS_NAME, "rt-input__input")
    AUTH_USER_NAME = (By.CLASS_NAME, "user-name user-info__name")
    AUTH_BTN = (By.ID, "kc-login")
    AUTH_BTNPOST = (By.ID, "t-btn-tab-mail")
    AUTH_BTNLOGIN = (By.ID, "t-btn-tab-login")
    AUTH_BTNPERSACCOUNT = (By.ID, "t-btn-tab-ls")
    AGREEMENT = (By.ID, "rt-auth-agreement-link")
    HELP = (By.XPATH, '//*[@id="faq-open"]/a[1]')