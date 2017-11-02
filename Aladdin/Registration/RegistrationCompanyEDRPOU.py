import unittest

from Aladdin.AladdinUtils import *
from Aladdin.Registration.UserRegistrationEDRPOU import UserRegistrationEDRPOU
from Aladdin.Registration.OpenMainPage import *
from selenium.common.exceptions import WebDriverException


class RegistrationCompany(OpenMainPage):
    query = {"input_val": None, "q": {"name": "UserCompanyRegistrationForm", "version": "0.0.0.3"}}
    reg = UserRegistrationEDRPOU()

    def test_01_registration_user(self):
        self.reg.wts = self.wts
        self.reg.wts.set_main_page(self.query)
        self.reg.test_01_company_name()
        self.reg.test_02_company_name_en()
        self.reg.test_03_check_ownership()
        self.reg.test_04_code_edrpou()
        self.reg.test_05_name()
        self.reg.test_06_name_en()
        self.reg.test_07_last_name()
        self.reg.test_08_last_name_en()
        self.reg.test_09_position()
        self.reg.test_10_phone()
        self.reg.test_11_email()
        self.reg.test_12_password()
        self.reg.test_13_confirm_password()
        self.reg.test_14_click_next_step_btn()

    def test_02_tax_system(self):
        test_select(self, "company_taxSystem", "5")

    def test_03_phone_company(self):
        test_input(self, "resident_phone", **self.query)

    def test_04_email_company(self):
        test_input(self, "email", **self.query)

    def test_05_country_legal(self):
        test_select(self, "legal_address_country", **self.query)

    def test_06_region_legal(self):
        test_select(self, "legal_address_region", **self.query)

    def test_07_city_legal(self):
        test_select(self, "legal_address_city", **self.query)

    def test_08_legal_address(self):
        test_input(self, "legal_address_street", **self.query)

    def test_09_legal_index(self):
        test_input(self, "legal_address_index", **self.query)

    def test_10_real_country(self):
        test_select(self, "real_address_country", **self.query)

    def test_11_real_region(self):
        test_select(self, "real_address_region", **self.query)

    def test_12_real_city(self):
        test_select(self, "real_address_city", **self.query)

    def test_13_real_address(self):
        test_input(self, "real_address_street", **self.query)

    def test_14_real_index(self):
        test_input(self, "real_address_index", **self.query)

    def test_15_bank_name(self):
        test_input(self, "company_bank_account_name", **self.query)

    def test_16_bank_mfo(self):
        test_input(self, "company_bank_account_mfo", **self.query)

    def test_17_bank_account(self):
        test_input(self, "company_bank_account_account", **self.query)

    def test_18_lead_first_name(self):
        test_input(self, "lead_first_name", **self.query)

    def test_19_lead_last_name(self):
        test_input(self, "lead_last_name", **self.query)

    def test_20_lead_email(self):
        test_input(self, "lead_email", **self.query)

    def test_21_lead_phone(self):
        test_input(self, "lead_phone_resident", **self.query)

    def test_22_confidant_first_name(self):
        test_input(self, "confidant_first_name", **self.query)

    def test_23_confidant_last_name(self):
        test_input(self, "confidant_last_name", **self.query)

    def test_24_confidant_position(self):
        test_input(self, "confidant_position", **self.query)

    def test_25_confidant_email(self):
        test_input(self, "confidant_email", **self.query)

    def test_26_confidant_phone(self):
        test_input(self, "confidant_phone_resident", **self.query)

    def test_27_contract_offer(self):
        contract_offer_check = self.wts.drv.find_element_by_xpath(".//*[@id='contract_offer_container']/label")
        contract_offer_check.click()
       # WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.XPATH, "")))


    def test_28_save(self):
        btn_save = self.wts.drv.find_element_by_id("btn_save_changes")
        btn_save.click()
        WebDriverWait(self.wts.drv, 5).until(EC.element_to_be_clickable((By.ID, "btn_edit")))
