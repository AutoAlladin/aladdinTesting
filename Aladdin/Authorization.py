import unittest

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Aladdin.AladdinUtils import *


class OpenMainPage(unittest.TestCase):
    wts=None
    def setUp(self):
        self.wts = WebTestSession()

    def tearDown(self):
        self.wts.close()

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
        try:
            input_val_company_name = "Тестовое название компании"
            self.assertEqual(
                input_val_company_name,
                self.wts.input_text_field("nameUA",input_val_company_name) ,
                "Не совпадают исходные даные и то что оказалось в поле браузера")
        except Exception as e:
            self.wts.drv.get_screenshot_as_file("company_name_ERROR.png")
            self.assertTrue(False, "Ошибка при вводе названия компании\n"+e.__str__())
