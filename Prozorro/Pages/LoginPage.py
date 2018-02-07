from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Prozorro.Pages.UserRegForm import UserRegForm
from Prozorro.Utils import waitFadeIn


class LoginPage:
    def __init__(self, _drv):
        self.drv = _drv

        try:
            self.txtLogin = WebDriverWait(self.drv, 10).until(
                  expected_conditions.visibility_of_element_located((By.ID, "Email")))
        except:
            raise Exception("not txtLogin found - Email")

        try:
         self.label_for_email = WebDriverWait(self.drv, 10).until(
                  expected_conditions.visibility_of_element_located((By.XPATH, "//label[@class='control-label'][@for='Email']")))
        except:
            raise Exception("not label_for_email found - //label[@class='control-label'][@for='Email']")

        try:
            self.msg_email  = WebDriverWait(self.drv, 10).until(
                  expected_conditions.visibility_of_element_located((By.XPATH, "//input[@id='Email']/../span[not(@data-valmsg-for)]")))
        except:
            raise Exception("not msg_email found - //input[@id='Email']/../span[not(@data-valmsg-for)]")

        try:
            self.txtPassword = WebDriverWait(self.drv, 10).until(
                  expected_conditions.visibility_of_element_located((By.ID, "Password")))
        except:
            raise Exception("not txtPassword found - Password")

        try:
            self.label_for_password = WebDriverWait(self.drv, 10).until(
                  expected_conditions.visibility_of_element_located((By.XPATH, "//label[@class='control-label'][@for='Password']")))
        except:
            raise Exception("not label_for_password found - //label[@class='control-label'][@for='Password']")

        try:
            self.msg_password = WebDriverWait(self.drv, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//input[@id='Password']/../span[not(@data-valmsg-for)]")))
        except:
            raise Exception("not msg_password found - //input[@id='Password']/../span[not(@data-valmsg-for)]")

        try:
            self.btnLogin = WebDriverWait(self.drv, 10).until(
                  expected_conditions.visibility_of_element_located((By.ID, "submitLogin")))
        except:
            raise Exception("not btnLogin found submitLogin")

        try:
            self.en = WebDriverWait(self.drv, 10).until(
                  expected_conditions.visibility_of_element_located((By.ID, "select_lang_en-us")))
        except:
            raise Exception("not select_lang_en-us found")

        try:
            self.ua = WebDriverWait(self.drv, 10).until(
                  expected_conditions.visibility_of_element_located((By.ID, "select_lang_uk-ua")))
        except:
            raise Exception("not select_lang_uk-ua found")

        try:
            self.ru = WebDriverWait(self.drv, 10).until(
                  expected_conditions.visibility_of_element_located((By.ID, "select_lang_ru-ru")))
        except:
            raise Exception("not select_lang_ru-ru found")

        try:
            self.greeting=WebDriverWait(self.drv, 10).until(
                  expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='login-container']//h1")))
        except:
            raise Exception("not greeting found - //div[@class='login-container']//h1")

        try:
            self.remember_me = WebDriverWait(self.drv, 10).until(
                  expected_conditions.presence_of_element_located((By.ID, "RememberMe")))
        except:
            raise Exception("not remember_me found - RememberMe")

        try:
            self.remember_me_label = WebDriverWait(self.drv, 10).until(
               expected_conditions.presence_of_element_located((By.XPATH, "//input[@id='RememberMe']/../label[@for='RememberMe']")))
        except:
            raise Exception("not remember_me_label found - //input[@id='RememberMe']/../label[@for='RememberMe']")

        try:
            self.remember_me_private = WebDriverWait(self.drv, 10).until(
               expected_conditions.presence_of_element_located(
                (By.XPATH, "//input[@id='RememberMe']/../p")))
        except:
            raise Exception("not remember_me_private found - //input[@id='RememberMe']/../p")

        try:
            self.register = WebDriverWait(self.drv, 10).until(
                  expected_conditions.visibility_of_element_located((By.ID, "btnRegister")))
        except:
            raise Exception("not register found - btnRegister")

        try:
            self.restorePass =WebDriverWait(self.drv, 10).until(
                expected_conditions.visibility_of_element_located((By.ID, "btnForgotPassword")))
        except:
            raise Exception("not restorePass found - btnForgotPassword")


    def open_register(self):
        self.register.click()
        WebDriverWait(self.drv, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//form[@action='/Account/Register']//button[@type='submit']")))

        r = UserRegForm(self.drv)

        return r

    def login(self, login, password):
        self.txtLogin.send_keys(login)
        self.txtPassword.send_keys(password)
        waitFadeIn(self.drv)
        self.btnLogin.click()

    def set_ua(self):
        self.ua.click()
        sleep(2)
        return LoginPage(self.drv)

    def set_ru(self):
        self.ru.click()
        sleep(2)
        return LoginPage(self.drv)

    def set_en(self):
        self.en.click()
        sleep(2)
        return LoginPage(self.drv)
