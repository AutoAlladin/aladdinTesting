import unittest
from selenium import webdriver
from Aladdin.AladdinUtils import *
from Aladdin import Authorization
from Aladdin.Registration.OpenMainPage import *
from Aladdin.Authorization.Login import Login


publicWST = None;
def setUpModule():
    global publicWST
    publicWST = WebTestSession()


def tearDownModule():
    publicWST.drv.close()


class EditInfo(OpenMainPage):
    def test_01_go_to_user_profile(self):

        Login.test_01_email(self)
        Login.test_02_pswd(self)
        Login.test_03_btn(self)
        user_prof = self.wts.drv.find_element_by_id("link_about")
        time.sleep(5)
        user_prof.click()

    def test_02_click_tab_company(self):

        btn_tab_company = self.wts.drv.find_element_by_id("profile_tab_company")
        time.sleep(10)
        btn_tab_company.click()
        self.wts.drv.execute_script("window.scrollTo(0, 2500);")


    def test_03_ownership_tax(self, r, id_field, input_val=None, q=None):
        select_ownership = browser.drv.find_element_by_id("ownership_type")
        select_ownership.send_keys("0")
        time.sleep(10)
        code = browser.drv.find_element_by_id("company_code_USREOU")
        return code.get_attribute("id")
        self.assertTrue("id" == code)


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



    def test_04_click_btn_edit(self):
        btn_edit = self.wts.drv.find_element_by_id("btn_edit")
        time.sleep(10)
        btn_edit.click()

    def test_05_update_comp_name(self):
        test_input()
        time.sleep(5)
        comp_name = self.wts.drv.find_element_by_id("nameUA")
        comp_name.send_keys("SunnyBunny")
        time.sleep(10)

    def test_06_contract_offer(self):
        contract_offer_check = browser.drv.find_element_by_xpath(".//*[@id='contract_offer_container']/label")
        contract_offer_check.click()



    def test_07_click_btn_save_changes(self):
        self.wts.drv.execute_script("window.scrollTo(0, 2500);")
        btn_s_changes = self.wts.drv.find_element_by_id("btn_save_changes")
        time.sleep(5)
        btn_s_changes.click()
