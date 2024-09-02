from pages.base_page import BasePage
from pages.locators import AuthLocators

import time,os

class AuthPage(BasePage):

    def __init__(self, driver,timeout=10):
        super().__init__(driver, timeout) # мы обращаемся к методу __init__ нашего родительского класса BasePage, так как наш новый метод __init__ затрёт его.
        url = os.getenv("LOGIN_URL") or "https://b2c.passport.rt.ru"
        driver.get(url) #открываем страничку

        #ищем элементы по локаторам

        self.telnumber = driver.find_element(*AuthLocators.AUTH_TELNUMBER)
        self.login = driver.find_element(*AuthLocators.AUTH_LOGIN)
        self.email = driver.find_element(*AuthLocators.AUTH_EMAIL)
        self.persaccount = driver.find_element(*AuthLocators.AUTH_PERSACCOUNT)
        self.passw = driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
        self.btn_post = driver.find_element(*AuthLocators.AUTH_BTNPOST)
        self.btn_login = driver.find_element(*AuthLocators.AUTH_BTNLOGIN)
        self.btn_persaccount = driver.find_element(*AuthLocators.AUTH_BTNPERSACCOUNT)
        self.btn_agreement = driver.find_element(*AuthLocators.AGREEMENT)
        self.btn_help = driver.find_element(*AuthLocators.HELP)

        time.sleep(3) #даем три секунды для визуализации

    def enter_telnumber(self, value): # метод ввода емейла
        self.telnumber.send_keys(value)

    def enter_login(self, value):  # метод ввода емейла
        self.login.send_keys(value)

    def enter_email(self, value): # метод ввода емейла
        self.email.send_keys(value)

    def enter_persaccount(self, value): # метод ввода емейла
        self.persaccount.send_keys(value)

    def enter_pass(self, value):  # метод ввода пароля
        self.passw.send_keys(value)

    def btn_click(self): # метод нажатия на кнопку
        self.btn.click()
        time.sleep(3)

    def btnpost_click(self): # метод нажатия на кнопку
        self.btn_post.click()
        time.sleep(3)

    def btnlogin_click(self): # метод нажатия на кнопку
        self.btn_login.click()
        time.sleep(3)

    def btnpersaccount_click(self): # метод нажатия на кнопку
        self.btn_persaccount.click()
        time.sleep(3)

    def agreement_click(self):  # метод нажатия на кнопку
        self.btn_agreement.click()
        time.sleep(3)

    def help_click(self):  # метод нажатия на кнопку
        self.btn_help.click()
        time.sleep(3)