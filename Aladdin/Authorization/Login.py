import unittest
from selenium import webdriver

from Aladdin.AladdinUtils import *
from Aladdin import Authorization

# browser = None;
# def setUpModule():
#     global browser
#     browser = openChrome()

publicWST = None;
def setUpModule():
    global publicWST
    publicWST = WebTestSession()


def tearDownModule():
    publicWST.drv.close()

#
# def field_input(_id, val):
#     field_input=browser.drv.find_element_by_id("_id")
#     field_input.send_keys("val")
#     return field_input.get_attribute('value')
#
# def text_input(_id, val, input_val=None):
#     try:
#         if input_val is None:
#             input_val = field_input(_id, val)
#         browser.drv.assertEqual(
#             input_val,
#             browser.drv.field_input
#         )
#     except Exception as e:
#         browser.assertTrue(False, "Ошибка при вводе текста\n" + e.__str__())




# class openChrome(unittest.TestCase):
#     def __init__(self):
#         try:
#             self.drv = webdriver.Chrome()
#             self.drv.maximize_window()
#             self.drv.implicitly_wait(10)
#             #self.drv.get('https://192.168.80.169:44310/Account/Login')
#             self.drv.get('https://identity.ald.in.ua/Account/Login')
#             self.assertTrue(True)
#         except Exception as e:
#             self.assertTrue(False, 'Не открывается форма логина\n' + e.__str__())
#
#



class Login(unittest.TestCase):
    wts = None

    @classmethod
    def setUpClass(cls):
        cls.wts = publicWST
        cls.wts.url = 'https://identity.ald.in.ua/Account/Login'

    @classmethod
    def test_01_email(self):
        #text_input("exampleInputEmail1", "envarra@gmail.com")
        # email = browser.drv.find_element_by_id("exampleInputEmail1")
        # email.send_keys("envarra@gmail.com")
        test_input(self, "exampleInputEmail1", "envarra@gmail.com")

    @classmethod
    def test_02_pswd(self):
        # pswd = browser.drv.find_element_by_id("pswd")
        # pswd.send_keys("qwerty1234")
        # time.sleep(10)
        test_input(self, "pswd", "qwerty1234")

    @classmethod
    def test_03_btn(self):
        btn = self.wts.drv.find_element_by_id("submitLogin")
        btn.click()
        #WebDriverWait(browser.drv, 10).until(EC._find_element(By.XPATH), "html/body")
        time.sleep(10)

