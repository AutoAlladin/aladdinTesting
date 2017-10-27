import unittest

from Aladdin.AladdinUtils import *
from Aladdin.Registration.UserRegistrationEDRPOU import UserRegistrationEDRPOU
from Aladdin.Registration.OpenMainPage import *

publicWST = None;
def setUpModule():
    global publicWST
    #publicWST = WebTestSession('https://identity.ald.in.ua/i_uk/registration/user')
    publicWST = WebTestSession('https://192.168.80.169:44310/i_uk/registration/user')

def tearDownModule():
    publicWST.close()


class UserRegistration_FOP(UserRegistrationEDRPOU):
    wts=None
    @classmethod
    def setUpClass(cls):
        cls.wts = publicWST

    def test_03_check_ownership(self):
        test_select(self, "ownership_type", "11")

    def test_04_code_edrpou(self):
        test_input(self,"company_code_USREOUFop", "1234567897")


