import unittest

from Aladdin.AladdinUtils import *
from Aladdin.Registration.OpenMainPage import OpenMainPage
from Aladdin.Registration.RegistrationCompanyEDRPOU import RegistrationCompany
from Aladdin.AladdinUtils import *


publicWST = None;
def setUpModule():
    global publicWST
    publicWST = WebTestSession('https://192.168.80.169:44310/Account/Login')
    #publicWST = WebTestSession('https://identity.ald.in.ua/Account/Login')


def tearDownModule():
    publicWST.drv.close()



class LoginAfterRegistrationCompany(OpenMainPage):
    full_reg = RegistrationCompany()
    wts=None
    @classmethod
    def setUpClass(cls):
        cls.wts = publicWST
    def test_01(self):
        self.full_reg.wts = self.wts
        self.full_reg.test_01_registration_user()
        self.full_reg.test_02_tax_system()
        self.full_reg.test_03_phone_company()
        self.full_reg.test_04_email_company()
        self.full_reg.test_05_country_legal()
        self.full_reg.test_06_region_legal()
        self.full_reg.test_07_city_legal()
        self.full_reg.test_08_legal_address()
        self.full_reg.test_09_legal_index()
        self.full_reg.test_10_real_country()
        self.full_reg.test_11_real_region()
        self.full_reg.test_12_real_city()
        self.full_reg.test_13_real_address()
        self.full_reg.test_14_real_index()
        self.full_reg.test_15_bank_name()
        self.full_reg.test_16_bank_mfo()
        self.full_reg.test_17_bank_account()
        self.full_reg.test_18_lead_first_name()
        self.full_reg.test_19_lead_last_name()
        self.full_reg.test_20_lead_email()
        self.full_reg.test_21_lead_phone()
        self.full_reg.test_22_confidant_first_name()
        self.full_reg.test_23_confidant_last_name()
        self.full_reg.test_24_confidant_position()
        self.full_reg.test_25_confidant_email()
        self.full_reg.test_26_confidant_phone()
        self.full_reg.test_27_contract_offer()
        self.full_reg.test_28_save()

    def test_1111_exit(self):
        pass

    def test_1112_login(self):
        test_input(self, "exampleInputEmail1", self.full_reg.reg.test_params["email"])
        test_input(self, "pswd", self.full_reg.reg.test_params["password"])
        btn_sub = self.wts.drv.find_element_by_id("submitLogin")
        btn_sub.click()

