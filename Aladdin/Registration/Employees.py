import unittest

from Aladdin.AladdinUtils import *
from tkinter import filedialog
from tkinter import *
import os
from urllib.parse import urlparse
from Prozorro.Utils import scroll_to_element
from selenium.webdriver.support import expected_conditions as EC
from Prozorro.Utils import *
from Aladdin.Registration.OpenMainPage import *
from Aladdin.Authorization.Login import Login
from Aladdin.Edit.Edit import Edit

publicWST = None;
def setUpModule():
    global publicWST
    publicWST = WebTestSession('https://identity.ald.in.ua/Account/Login')

def tearDownModule():
    publicWST.close()

class OpenMainPage(unittest.TestCase):
    wts=None
    @classmethod
    def setUpClass(cls):
        cls.wts = publicWST

class Employees(OpenMainPage):

    def test_01_go_to_user_profile(self):
        log = Login()
        log.wts = self.wts
        log.wts.set_main_page()
        log.test_01_email()
        log.test_02_pswd()
        log.test_03_btn()

    def test_02_tab_empl(self):
        ed = Edit()
        ed.wts = self.wts
        ed.test_01_go_to_user_profile()

        btn_tab_empl = self.wts.drv.find_element_by_id("profile_tab_employees")
        btn_tab_empl.click()

    def test_03_add_user(self):
        btn_add_user = self.wts.drv.find_element_by_id("butAddNewUser")
        btn_add_user.click()

    def test_04_name(self):
        test_input(self, "firstName_0", "Ввававіав")

    def test_05_name_eu(self):
        test_input(self,"firstNameEn_0", "Gfgfgdfdfdf")

    def test_06_last_name(self):
        test_input(self, "lastName_0", "Смсмсмсм")

    def test_07_last_name_eu(self):
        test_input(self, "lastNameEn_0", "Ffdfdfx")

    def test_08_position(self):
        test_input(self, "position_0", "папапсмсм пмсм")

    def test_09_email(self):
        test_input(self, "email_0", "fdfdf@fdf.ru")

    def test_10_phone(self):
        test_input(self, "phone_0", "44545454")

    def test_11_save(self):
        btn_save = self.wts.drv.find_element_by_id("save_changes_0")
        btn_save.click()

