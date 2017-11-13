import unittest

from Aladdin.decorators.ParamsTestCase import  ParamsTestCase
from Aladdin.AladdinUtils import test_input, test_click
from Aladdin.decorators.StoreTestResult import add_res_to_DB


class Login(ParamsTestCase):

    @add_res_to_DB(test_name="email_input")
    def test_01_email(self):
        test_input(self, "exampleInputEmail1", **self.params['query'])

    @add_res_to_DB(test_name="pssword_input")
    def test_02_pswd(self):
        test_input(self,"pswd",  **self.params['query'])

    @add_res_to_DB(test_name="button_click")
    def test_03_btn(self):
        test_click(self,"btn_sub",  **self.params['query'] )



