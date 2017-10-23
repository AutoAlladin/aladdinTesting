import unittest

from Aladdin.AladdinUtils import *
from Aladdin.Registration.UserRegistrationEDRPOU import UserRegistrationEDRPOU
from Aladdin.Registration.OpenMainPage import *



class RegistrationCompany(OpenMainPage):
    query = {"name": "UserCompanyRegistrationForm", "version": "0.0.0.3"}
    query = {"input_val": None, "q": {"name": "UserRegistrationForm", "version": "0.0.0.3"}}


    # def test_01_click_edit_btn(self):
    #     # Key
    #     try:
    #
    #         WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable(((By.ID, "btn_edit"))))
    #         edit_btn = self.wts.drv.find_element_by_id("btn_edit")
    #         scroll_to_element(self.wts.drv,edit_btn,'0')
    #
    #         edit_btn.click()
    #         self.assertTrue(True)
    #     except Exception as e:
    #         self.assertTrue(False, 'Не кликается кнопка Редагувати\n' + e.__str__())


    def test_01_registration_user(self):
        UserRegistrationEDRPOU.test_01_company_name(self)
        UserRegistrationEDRPOU.test_02_company_name_en(self)
        UserRegistrationEDRPOU.test_03_check_ownership(self)
        UserRegistrationEDRPOU.test_04_code_edrpou(self)
        UserRegistrationEDRPOU.test_05_name(self)
        UserRegistrationEDRPOU.test_06_name_en(self)
        UserRegistrationEDRPOU.test_07_last_name(self)
        UserRegistrationEDRPOU.test_08_last_name_en(self)
        UserRegistrationEDRPOU.test_09_position(self)
        UserRegistrationEDRPOU.test_10_phone(self)
        UserRegistrationEDRPOU.test_11_email(self)
        UserRegistrationEDRPOU.test_12_password(self)
        UserRegistrationEDRPOU.test_13_confirm_password(self)
        UserRegistrationEDRPOU.test_14_click_next_step_btn(self)

    def test_02_tax_system(self):
        test_select(self, "company_taxSystem", "5")

    def test_03_phone_company(self):
        test_input(self, "phone", q=self.query)

    def test_04_email_company(self):
        test_input(self, "email", q=self.query)

    def test_05_country_legal(self):
        test_select(self, "legal_address_country", q=self.query)

    def test_06_region_legal(self):
        test_select(self, "legal_address_region", q=self.query)

    def test_07_city_legal(self):
        test_select(self, "legal_address_city", q=self.query)

    def test_08_legal_address(self):
        test_input(self, "legal_address_street", q=self.query)

    def test_09_legal_index(self):
        test_input(self, "legal_address_index", q=self.query)

    def test_10_real_country(self):
        test_select(self, "real_address_country", q=self.query)

    def test_11_real_region(self):
        test_select(self, "real_address_region", q=self.query)

    def test_12_real_city(self):
        test_select(self, "real_address_city", q=self.query)

    def test_13_real_address(self):
        test_input(self, "real_address_street", q=self.query)

    def test_14_real_index(self):
        test_input(self, "real_address_index", q=self.query)

    def test_15_bank_name(self):
        test_input(self, "company_bank_account_name", q=self.query)

    def test_16_bank_mfo(self):
        test_input(self, "company_bank_account_mfo", q=self.query)

    def test_17_bank_account(self):
        test_input(self, "company_bank_account_account", q=self.query)

    def test_18_lead_first_name(self):
        test_input(self, "lead_first_name", q=self.query)

    def test_19_lead_last_name(self):
        test_input(self, "lead_last_name", q=self.query)

    def test_20_lead_email(self):
        test_input(self, "lead_email", q=self.query)

    def test_21_lead_phone(self):
        test_input(self, "lead_phone", q=self.query)

    def test_22_confidant_first_name(self):
        test_input(self, "confidant_first_name", q=self.query)

    def test_23_confidant_last_name(self):
        test_input(self, "confidant_last_name", q=self.query)

    def test_24_confidant_position(self):
        test_input(self, "confidant_position", q=self.query)

    def test_25_confidant_email(self):
        test_input(self, "confidant_email", q=self.query)

    def test_26_confidant_phone(self):
        test_input(self, "confidant_phone", q=self.query)

    def test_27_contract_offer(self):
        contract_offer_check = self.wts.drv.find_element_by_xpath(".//*[@id='contract_offer_container']/label")
        contract_offer_check.click()
       # WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.XPATH, "")))

    def test_28_save(self):
        btn_save = self.wts.drv.find_element_by_id("btn_save_changes")
        btn_save.click()
        #WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "btn_save_changes")))

