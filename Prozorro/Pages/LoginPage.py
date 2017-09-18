from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LoginPage:
    def __init__(self, _drv):
        self.drv = _drv
        self.__txtLogin = self.drv.find_element_by_id("Email")
        self.__txtPassword = self.drv.find_element_by_id("Password")
        self.__btnLogin = self.drv.find_element_by_id("submitLogin")

    def login(self, login, password):
        self.__txtLogin.send_keys(login)
        self.__txtPassword.send_keys(password)
        self.__btnLogin.click()
