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

publicWST = None;
def setUpModule():
    global publicWST
    publicWST = WebTestSession()

def tearDownModule():
    publicWST.close()



class Employees(OpenMainPage):
    def test_01_tab_empl(self):
        btn_tab_empl = self.wts.drv.find_element_by_id("profile_tab_employees")
        btn_tab_empl.click()

    def test_02_add_user(self):
        btn_add_user = self.wts.drv.find_element_by_id("butAddNewUser")
        btn_add_user.click()

    def test_03_name(self):
        test_input(self, "firstName_0", "Ввававіав")

    def test_04_name_eu(self):
        test_input(self,"firstNameEn_0", "Gfgfgdfdfdf")

    def test_05_last_name(self):
        test_input(self, "lastName_0", "Смсмсмсм")

    def test_06_last_name_eu(self):
        test_input(self, "lastNameEn_0", "Ffdfdfx")

    def test_07_position(self):
        test_input(self, "position_0", "папапсмсм пмсм")

    def test_08_email(self):
        test_input(self, "email_0", "fdfdf@fdf.ru")

    def test_09_phone(self):
        test_input(self, "phone_0", "44545454")

    def test_10_save(self):
        btn_save = self.wts.drv.find_element_by_id("save_changes")
        btn_save.click()

