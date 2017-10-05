import unittest

import time
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

    def test_1_company_name(self):
        test_input(self, "nameUA",q=self.query)

    def test_2_company_name_en(self):
        test_input(self, "nameEN", q=self.query)

    def test_3_check_ownership(self):
        test_select(self, "ownership_type",  q=self.query )

    def test_4_code_edrpou(self):
        test_input(self, "company_code_USREOU", "12121212")

    def test_5_name(self):
        test_input(self, "admin_name_ua", "Тестовое имя")

    def test_6_name_en(self):
        test_input(self, "admin_name_en", "Admin`s test name")

    def test_7_last_name(self):
        test_input(self, "admin_last_name_ua", "Тестовая фамилия")

    def test_8_last_name_en(self):
        test_input(self, "admin_last_name_en", "Admin`s test last name")

