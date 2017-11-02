import unittest
from Aladdin.decorators.StoreTestResult import *
from Aladdin.AladdinUtils import WebTestSession, test_input


publicWST = None;
def setUpModule():
    global publicWST
    publicWST = WebTestSession()


def tearDownModule():
    publicWST.drv.close()

class Login(unittest.TestCase):


    query = {"input_val": None, "q": {"name": "Login", "version": "0.0.0.1"}}

    @classmethod
    @create_result_DB
    def setUpClass(cls):
        cls.tlog = [{}]
        cls.wts = publicWST
        cls.wts.set_main_page(cls.query)
        cls.wts.test_name="Авторизация уже зарегистрированого пользователя"
        return cls.wts

    @add_res_to_DB
    def test_01_email(self):
        test_input(self, "exampleInputEmail1", **self.query)

    @add_res_to_DB
    def test_02_pswd(self):
        test_input(self,"pswd", **self.query)

    @add_res_to_DB
    def test_03_btn(self):
        btn_sub = self.wts.drv.find_element_by_id("submitLogin")
        btn_sub.click()



