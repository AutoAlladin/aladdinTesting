import unittest
from selenium import webdriver

from Aladdin.AladdinUtils import *
from Aladdin import Authorization

# browser = None;
# def setUpModule():
#     global browser
#     browser = openChrome()
from Aladdin.Registration.OpenMainPage import OpenMainPage

publicWST = None;
def setUpModule():
    global publicWST
    publicWST = WebTestSession( 'https://identity.ald.in.ua/Account/Login')


def tearDownModule():
    publicWST.drv.close()


class Login(unittest.TestCase):

    query = {"input_val": None, "q": {"name": "Login", "version": "0.0.0.1"}}

    @classmethod
    def setUpClass(cls):
        cls.wts = publicWST
        cls.wts.url = 'https://identity.ald.in.ua/Account/Login'


    def test_01_email(self):
        test_input(self, "exampleInputEmail1", **self.query)

    def test_02_pswd(self):
        test_input(self,"pswd", **self.query)

    def test_03_btn(self):
        btn_sub = self.wts.drv.find_element_by_id("submitLogin")
        btn_sub.click()
        time.sleep(10)

class EditInfo(unittest.TestCase):
    def test_01_go_to_user_profile(self):
        WebDriverWait(self.wts.drv, 10).until(
            EC.visibility_of_element_located((By.ID, "link_about")))

        user_prof = self.wts.drv.find_element_by_id("link_about")
        user_prof.click()
        WebDriverWait(self.wts.drv, 20).until(
            EC.element_to_be_clickable((By.ID, "btnSaveUser")))

    def test_02_click_tab_company(self):

        btn_tab_company = self.wts.drv.find_element_by_id("profile_tab_company")
        time.sleep(10)
        btn_tab_company.click()
        self.wts.drv.execute_script("window.scrollTo(0, 2500);")

    def test_03_click_btn_edit(self):
        btn_edit = self.wts.drv.find_element_by_id("btn_edit")
        time.sleep(10)
        btn_edit.click()

    def test_04_update_comp_name(self):
        test_input()
        time.sleep(5)
        comp_name = self.wts.drv.find_element_by_id("nameUA")
        comp_name.send_keys("SunnyBunny")
        time.sleep(10)

    def test_05_click_btn_save_changes(self):
        self.wts.drv.execute_script("window.scrollTo(0, 2500);")
        btn_s_changes = self.wts.drv.find_element_by_id("btn_save_changes")
        time.sleep(5)
        btn_s_changes.click()
