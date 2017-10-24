import unittest
from selenium import webdriver
from Aladdin.AladdinUtils import *
from Aladdin import Authorization
from Aladdin.Registration.OpenMainPage import *
from Aladdin.Authorization.Login import Login


publicWST = None
def setUpModule():
    global publicWST
    publicWST = WebTestSession( 'https://identity.ald.in.ua/Account/Login')

def tearDownModule():
    publicWST.drv.close()

class Edit(OpenMainPage):
    query = {"input_val": None, "q": {"name": "EditInfo", "version": "0.0.0.1"}}
    wts=None
    @classmethod
    def setUpClass(cls):
        cls.wts = publicWST

    def test_01_go_to_user_profile(self):
        l = Login()
        l.wts = self.wts
        l.wts.set_main_page()
        l.test_01_email()
        l.test_02_pswd()
        l.test_03_btn()
        user_prof = self.wts.drv.find_element_by_id("link_about")
        time.sleep(5)
        user_prof.click()



    def test_02_click_tab_company(self):
        WebDriverWait(self.wts.drv, 10).until(
            EC.element_to_be_clickable((By.ID, "profile_tab_company")))
        btn_tab_company = self.wts.drv.find_element_by_id("profile_tab_company")
        btn_tab_company.click()
        self.wts.drv.execute_script("window.scrollTo(0, 2500);")


    #  def test_03_ownership_tax(self, r, id_field, input_val=None, q=None):
    #     select_ownership = self.wts.drv.find_element_by_id("ownership_type")
    #      select_ownership.send_keys("0")
    #    code = self.wts.drv.find_element_by_id("company_code_USREOU")
    #     return code.get_attribute("id")
    #     self.assertTrue("id" == code)


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



    def test_03_click_btn_edit(self):
        btn_edit = self.wts.drv.find_element_by_id("btn_edit")
        btn_edit.click()

    def test_04_clear_field_comp_name(self):
        f_comp_name = self.wts.drv.find_element_by_id("nameUA")
        f_comp_name.clear()

    def test_05_update_comp_name(self):
        test_input(self, "nameUA", **self.query)

    def test_06_contract_offer(self):
        contract_offer_check = self.wts.drv.find_element_by_xpath(".//*[@id='contract_offer_container']/label")
        contract_offer_check.click()

    def test_07_legal_address_country(self):
        test_select(self, "legal_address_country", **self.query)

    def test_08_select_real_address_city(self):
        test_select(self, "real_address_city", **self.query)

    def test_09_real_address_street(self):
        test_input(self, "real_address_street", **self.query)

    def test_10_confidant_position(self):
        test_input(self, "confidant_position", **self.query)

    def test_11_click_btn_save_changes(self):
    #self.wts.drv.execute_script("window.scrollTo(0, 2500);")
        btn_s_changes = self.wts.drv.find_element_by_id("btn_save_changes")
        time.sleep(5)
        btn_s_changes.click()
