import unittest
from selenium import webdriver

from Aladdin.AladdinUtils import *
from Aladdin.Authorization import *

browser = None;
def setUpModule():
    global browser
    browser = openChrome()

def tearDownModule():
    browser.drv.close()

class openChrome(unittest.TestCase):
    def __init__(self):
        try:
            self.drv = webdriver.Chrome()
            self.drv.maximize_window()
            self.drv.implicitly_wait(10)
            self.drv.get('https://192.168.80.169:44310/Account/Login')
            self.assertTrue(True)
        except Exception as e:
            self.assertTrue(False, 'Не открывается форма логина\n' + e.__str__())



class Login(unittest.TestCase):
    def test_01_email(self):

        email = browser.drv.find_element_by_id("exampleInputEmail1")
        email.send_keys("envarra@gmail.com")
        #test_input(self, "exampleInputEmail1", "envarra@gmail.com")


    def test_02_pswd(self):
        pswd = browser.drv.find_element_by_id("pswd")
        pswd.send_keys("qwerty1234")
        time.sleep(10)
        #test_input(self, "pswd", "qwerty1234")

    def test_03_btn(self):
        btn = browser.drv.find_element_by_id("submitLogin")
        btn.click()
        #WebDriverWait(browser.drv, 10).until(EC._find_element(By.XPATH), "html/body")
        time.sleep(10)





# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)


# if __name__ == '__main__':
#     unittest.main()
