import unittest
from selenium import webdriver

from Aladdin.AladdinUtils import *
from Aladdin import Authorization

# browser = None;
# def setUpModule():
#     global browser
#     browser = openChrome()
from Aladdin.Registration.OpenMainPage import OpenMainPage

publicWST = None;
def setUpModule():
    global publicWST
    publicWST = WebTestSession('https://identity.ald.in.ua/Account/Login')


def tearDownModule():
    publicWST.drv.close()


class Login(unittest.TestCase):

    query = {"input_val": None, "q": {"name": "Login", "version": "0.0.0.1"}}

    @classmethod
    def setUpClass(cls):
        cls.wts = publicWST
        cls.wts.url = 'https://identity.ald.in.ua/Account/Login'


    def test_01_email(self):
        test_input(self, "exampleInputEmail1", **self.query)

    def test_02_pswd(self):
        test_input(self,"pswd", **self.query)

    def test_03_btn(self):
        btn_sub = self.wts.drv.find_element_by_id("submitLogin")
        btn_sub.click()
        time.sleep(10)



