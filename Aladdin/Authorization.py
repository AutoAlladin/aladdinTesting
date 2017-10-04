import unittest

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def set_web_driver():
    chrm = webdriver.Chrome()
    #chrm = webdriver.Chrome(chrm)
    chrm.maximize_window()
    chrm.implicitly_wait(5)
    return chrm

def click_reg_btn(хром):
    хром.get('https://alltenders.ald.in.ua/uk')
    btn_registration = хром.find_element_by_xpath(".//*[@id='navbarCollapse']/div[2]/div[1]/a[2]")
    btn_registration.click()
    WebDriverWait(хром, 15).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "РЕЄСТРАЦІЯ ПІДПРИЄМСТВА"))

class OpenMainPage(unittest.TestCase):
    хром_для_всего_тэста=None
    def setUp(self):
        self.хром_для_всего_тэста = set_web_driver()

    def tearDown(self):
        self.хром_для_всего_тэста.close()

    @unittest.skip("qqq")
    def test_open_page(self):
        try:
            self.хром_для_всего_тэста.get('https://alltenders.ald.in.ua/uk')
            WebDriverWait(self.хром_для_всего_тэста, 5).until(
                EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "РЕЄСТРАЦІЯ"))
            self.assertTrue(True)
        except Exception as e:
            self.assertTrue(False, 'внятное слово '+e.__str__())


class OpenRegistrationPage(OpenMainPage):
    @unittest.skip("Не представляет интереса на даный момент")
    def test_open_registration_page(self):
        try:
            click_reg_btn(хром=self.хром_для_всего_тэста)
            self.assertTrue(True)
        except Exception as e:
            self.assertTrue(False, 'Ошибка открытия формы регистрации\n'+e.__str__())

class FullFillPage(OpenRegistrationPage):
    def test_company_name(self):
        try:
            input_val_company_name = "Тестовое название компании"
            click_reg_btn(хром=self.хром_для_всего_тэста)
            company_name = self.хром_для_всего_тэста.find_element_by_id("nameUA")
            company_name.send_keys(input_val_company_name)
            self.хром_для_всего_тэста.get_screenshot_as_file("company_name.png")

            result_val_company_name = company_name.get_attribute('value')
            self.assertEqual(input_val_company_name, result_val_company_name, "Не совпадают исходные даные и то что оказалось в поле браузера")
        except Exception as e:
            self.хром_для_всего_тэста.get_screenshot_as_file("company_name_ERROR.png")
            self.assertTrue(False, "Ошибка при вводе названия компании\n"+e.__str__())

    def test_company_name_en(self):
        try:
            input_val_company_name_en = "Test name jf company"
            company_name_en = self.хром_для_всего_тэста.find_element_by_id("nameEN")
            company_name_en.send_keys(input_val_company_name_en)
            self.хром_для_всего_тэста.get_screenshot_as_file("company_name_en.png")
            result_val_company_name_en = company_name_en.


