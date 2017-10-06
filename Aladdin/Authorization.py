import unittest

import time

from dns.e164 import query
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from Aladdin.AladdinUtils import *


def test_select(cls, id_field, input_val=None, q=None):
    try:
        if input_val is None:
            input_val = cls.wts.__mongo__.get_select_val(id_field, q)

        cls.assertEqual(
            input_val,
            cls.wts.select_value(id_field, input_val),
            "Не совпадают исходные даные и то что оказалось в поле браузера")
    except Exception as e:
        cls.wts.drv.get_screenshot_as_file("output\\"+id_field+"_ERROR.png")
        cls.assertTrue(False, "Ошибка при выборе значения\n" + e.__str__())


def test_input(cls, id_field, input_val=None, q=None):
    try:
        if input_val is None:
            input_val = cls.wts.__mongo__.get_input_val(id_field, q)

        cls.assertEqual(
            input_val,
            cls.wts.input_text_field(id_field, input_val),
            "Не совпадают исходные даные и то что оказалось в поле браузера")
    except Exception as e:
        cls.wts.drv.get_screenshot_as_file("output\\"+id_field+"_ERROR.png")
        cls.assertTrue(False, "Ошибка при вводе текста\n" + e.__str__())

class OpenMainPage(unittest.TestCase):
    wts=None
    @classmethod
    def setUpClass(cls):
        cls.wts = WebTestSession()
    @classmethod
    def tearDownClass(cls):
        cls.wts.close()

    @unittest.skip("test_open_page - Не представляет интереса на даный момент")
    def test_open_page(self):
        try:
            self.wst.drv.get('https://alltenders.ald.in.ua/uk')
            WebDriverWait(self.wst.drv, 5).until(
                EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "РЕЄСТРАЦІЯ"))
            self.assertTrue(True)
        except Exception as e:
            self.assertTrue(False, 'внятное слово '+e.__str__())

class OpenRegistrationPage(OpenMainPage):
    @unittest.skip("test_open_registration_page - Не представляет интереса на даный момент")
    def test_open_registration_page(self):
        try:
            self.wts.click_reg_btn()
            self.assertTrue(True)
        except Exception as e:
            self.assertTrue(False, 'Ошибка открытия формы регистрации\n'+e.__str__())

class FullFillPage(OpenRegistrationPage):
    query = {"name": "RegistartionForm", "version": "0.0.0.2"}

    def test_101_company_name(self):
        test_input(self, "nameUA",q=self.query)

    def test_02_company_name_en(self):
        test_input(self, "nameEN", q=self.query)

    def test_03_check_ownership(self):
        test_select(self, "ownership_type",  q=self.query )

    def test_04_code_edrpou(self):
        test_input(self, "company_code_USREOU", q=self.query)

    def test_05_name(self):
        test_input(self, "admin_name_ua", q=self.query)

    def test_06_name_en(self):
        test_input(self, "admin_name_en", q=self.query)

    def test_07_last_name(self):
        test_input(self, "admin_last_name_ua", q=self.query)

    def test_08_last_name_en(self):
        test_input(self, "admin_last_name_en", q=self.query)

    def test_09_position(self):
        test_input(self, "position", q=self.query)

    def test_10_phone(self):
        test_input(self, "phone", q=self.query)

    def test_011_email(self):
        #test_input(self, "email", q=self.query)
        eml=self.wts.__mongo__.test_params.find_one(self.query)
        next=str(int(eml["inputs"]["email_next"])+1)
        self.wts.__mongo__.test_params.update_one({"_id":eml["_id"]},{"$set":{"inputs.email":"forTestRegEmail_"+next.rjust(5,'0')+"@cucumber.com"}})
        self.wts.__mongo__.test_params.update_one({"_id":eml["_id"]}, {"$set":{"inputs.email_next": next}})

    def test_12_password(self):
        test_input(self, "password", q=self.query)

    def test_13_confirm_password(self):
        test_input(self, "confirm_password", q=self.query)

    def test_14_click_next_step_btn(self):
        try:
            next_step_btn = self.wts.drv.find_element_by_id("btn_next_step")
            next_step_btn.click()
            WebDriverWait(self.wts.drv, 10).until(
                EC.text_to_be_present_in_element((By.ID, "btn_save_changes"), "Зберегти"))
            self.assertTrue(True)
        except Exception as e:
            self.assertTrue(False, 'Не отображается кнопка Зберегти\n' + e.__str__())



