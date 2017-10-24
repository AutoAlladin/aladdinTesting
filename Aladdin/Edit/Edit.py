import unittest
from selenium import webdriver
from Aladdin.AladdinUtils import *
from Aladdin import Authorization
from Aladdin.Registration.OpenMainPage import OpenMainPage
from Aladdin.Authorization.Login import Login


publicWST = None;
def setUpModule():
    global publicWST
    publicWST = WebTestSession('https://identity.ald.in.ua/Account/Login')


def tearDownModule():
    publicWST.drv.close()

class OpenMainPage(unittest.TestCase):
    wts=None
    @classmethod
    def setUpClass(cls):
        cls.wts = publicWST

class Edit(OpenMainPage):
    def test_01_go_to_user_profile(self):
        l = Login()
        l.wts = self.wts
        l.wts.set_main_page()
        l.test_01_email()
        l.test_02_pswd()
        l.test_03_btn()
        user_prof = self.wts.drv.find_element_by_id("link_about")
        user_prof.click()


        # WebDriverWait(self.wts.drv, 10).until(
        #     EC.visibility_of_element_located((By.ID, "link_about")))
        #
        # user_prof = self.wts.drv.find_element_by_id("link_about")
        # user_prof.click()
        # WebDriverWait(self.wts.drv, 20).until(
        #     EC.element_to_be_clickable((By.ID, "btnSaveUser")))

    def test_02_click_tab_company(self):
        btn_tab_company = self.wts.drv.find_element_by_id("profile_tab_company")
        time.sleep(5)
        btn_tab_company.click()
        self.wts.drv.execute_script("window.scrollTo(0, 2500);")


    def test_03_click_btn_edit(self):
        btn_edit = self.wts.drv.find_element_by_id("btn_edit")
        time.sleep(5)
        btn_edit.click()

    def test_04_update_comp_name(self):
        test_input()
        time.sleep(5)
        comp_name = self.wts.drv.find_element_by_id("nameUA")
        comp_name.send_keys("SunnyBunny")
        time.sleep(10)

    # def test_05_ownership_tax(self, r, id_field, input_val=None, q=None):
    #     select_ownership = self.wts.drv.find_element_by_id("ownership_type")
    #     select_ownership.send_keys("0")
    #     time.sleep(10)
    #     code = self.wts.drv.find_element_by_id("company_code_USREOU")
    #     code.send_keys("12345678")
    #     value = code.get_attribute("value")
    #     self.assertEqual(value, code)

        # try:
        #     if input_val is None:
        #         input_val = r.wts.__mongo__.get_input_val(id_field, q)
        #
        #     select_ownership = browser.drv.find_element_by_id("ownership_type")
        #     select_ownership.send_keys("0")
        #     time.sleep(10)
        #     code = browser.drv.find_element_by_id("company_code_USREOU")
        #     return code.get_attribute("id")
        #
        #     r.assertTrue("id" == code)
        #
        # except Expection as e:
        #     r.assertTrue(False, "При редактировании формы собственности - код не изменился\n" + e.__str__())


    def test_05_contract_offer(self):
        contract_offer_check = self.wts.drv.find_element_by_xpath(".//*[@id='contract_offer_container']/label")
        contract_offer_check.click()
        time.sleep(10)

    def test_06_click_btn_save_changes(self):
        self.wts.drv.execute_script("window.scrollTo(0, 2500);")
        btn_s_changes = self.wts.drv.find_element_by_id("btn_save_changes")
        time.sleep(5)
        btn_s_changes.click()
