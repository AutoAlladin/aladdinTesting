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
        test_input(self, "firstName_0", "Валерка")

    def test_05_name_eu(self):
        test_input(self,"firstNameEn_0", "Valerka")

    def test_06_last_name(self):
        test_input(self, "lastName_0", "Пупкин")

    def test_07_last_name_eu(self):
        test_input(self, "lastNameEn_0", "Pupkin")

    def test_08_position(self):
        test_input(self, "position_0", "Супер пупер админ")

    def test_09_email(self):
        test_input(self, "email_0", "test@ff.ru")
        eml = self.wts.__mongo__.test_params.find_one(self.query["q"])
        self.test_params.update({"email": eml["inputs"]["email"]})
        print("email", self.test_params["email"])
        next = str(int(eml["inputs"]["email_next"]) + 1)
        self.wts.__mongo__.test_params.update_one({"_id": eml["_id"]}, {
            "$set": {"inputs.email": "forAddEmloyeesEmail_" + next.rjust(5, '0') + "@cucumber.com"}})
        self.wts.__mongo__.test_params.update_one({"_id": eml["_id"]}, {"$set": {"inputs.email_next": next}})

    def test_10_phone(self):
        test_input(self, "phone_0", "+380 (90) 000-00-00")

    def test_11_role(self):
        test_select(self, "role", "3")
        time.sleep(10)

    def test_12_save(self):
        btn_save = self.wts.drv.find_element_by_id("save_changes_0")
        btn_save.click()
        time.sleep(20)
        locator = (By.ID, "butAddNewUser")
        WebDriverWait(self.wts.drv, 5).until(EC.element_to_be_clickable(locator))



