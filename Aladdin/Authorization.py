import unittest

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from Aladdin.AladdinUtils import *


def test_input(cls, id_field, input_val):
    try:
        cls.assertEqual(
            input_val,
            cls.wts.input_text_field(id_field, input_val),
            "Не совпадают исходные даные и то что оказалось в поле браузера")
    except Exception as e:
        cls.wts.drv.get_screenshot_as_file("company_name_ERROR.png")
        cls.assertTrue(False, "Ошибка при вводе названия компании\n" + e.__str__())

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
    def test_company_name(self):
        test_input(self, "nameUA","Тестовое название компании")

    def test_company_name_en(self):
        test_input(self, "nameEN", "Test company name")

    def test_check_ownership(self):
        try:
            select_ownership = self.wts.drv.find_element_by_id("ownership_type")
            Select(select_ownership).select_by_visible_text("string:ООО")
            sel_own = self.wts.drv.find_element_by_xpath("")
            sel_own.click()
            self.assertTrue(True)
        except Exception as e:
            self.assertTrue(False)

    def test_code_edrpou(self):
        test_input(self, "company_code_USREOU", "12121212")

    def test_name(self):
        test_input(self, "admin_name_ua", "Тестовое имя")

    def test_name_en(self):
        test_input(self, "admin_name_en", "Admin`s test name")

    def test_last_name(self):
        test_input(self, "admin_last_name_ua", "Тестовая фамилия")

    def test_last_name_en(self):
        test_input(self, "admin_last_name_en", "Admin`s test last name")

