from time import sleep

from Aladdin.Accounting.AladdinUtils import *
from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from Aladdin.Accounting.decorators.StoreTestResult import add_res_to_DB
from Aladdin.Accounting.Registration.UserRegistrationEDRPOU import UserRegistrationEDRPOU


class RegistrationCompany(ParamsTestCase):

    @add_res_to_DB()
    def test_01_registration_user(self):
        w = {"query": {"q": {"name": "UserRegistrationForm", "version": "0.0.0.3",
                             'group': self.params['query']['q']['group']}},
             'wts': self.wts
             }
        reg = UserRegistrationEDRPOU(_params=w, _parent_suite= self.parent_suite)
        reg.test_01_company_name()
        reg.test_02_company_name_en()
        reg.test_03_check_ownership()
        reg.test_04_code_edrpou()
        reg.test_05_name()
        reg.test_06_name_en()
        reg.test_07_last_name()
        reg.test_08_last_name_en()
        reg.test_09_position()
        reg.test_10_phone()
        reg.test_11_email()
        reg.test_12_password()
        reg.test_13_confirm_password()
        reg.test_14_click_next_step_btn()
        self.wts.close_toast()

    @add_res_to_DB()
    def test_02_tax_system(self):
        test_select(self, "company_taxSystem", **self.params['query'])

    @add_res_to_DB()
    def test_03_phone_company(self):
        test_input(self, "resident_phone", **self.params['query'])

    @add_res_to_DB()
    def test_04_email_company(self):
        test_input(self, "email", **self.params['query'])

    @add_res_to_DB()
    def test_05_country_legal(self):
        test_select(self, "legal_address_country", **self.params['query'])

    @add_res_to_DB()
    def test_06_region_legal(self):
        test_select(self, "legal_address_region", **self.params['query'])

    @add_res_to_DB()
    def test_07_city_legal(self):
        test_select(self, "legal_address_city", **self.params['query'])

    @add_res_to_DB()
    def test_08_legal_address(self):
        test_input(self, "legal_address_street", **self.params['query'])

    @add_res_to_DB()
    def test_09_legal_index(self):
        test_input(self, "legal_address_index", **self.params['query'])

    @add_res_to_DB()
    def test_10_real_country(self):
        test_select(self, "real_address_country", **self.params['query'])

    @add_res_to_DB()
    def test_11_real_region(self):
        test_select(self, "real_address_region", **self.params['query'])

    @add_res_to_DB()
    def test_12_real_city(self):
        test_select(self, "real_address_city", **self.params['query'])

    @add_res_to_DB()
    def test_13_real_address(self):
        test_input(self, "real_address_street", **self.params['query'])

    @add_res_to_DB()
    def test_14_real_index(self):
        test_input(self, "real_address_index", **self.params['query'])

    @add_res_to_DB()
    def test_15_bank_name(self):
        test_input(self, "company_bank_account_name", **self.params['query'])

    @add_res_to_DB()
    def test_16_bank_mfo(self):
        test_input(self, "company_bank_account_mfo", **self.params['query'])

    @add_res_to_DB()
    def test_17_bank_account(self):
        test_input(self, "company_bank_account_account", **self.params['query'])

    @add_res_to_DB()
    def test_18_lead_first_name(self):
        test_input(self, "lead_first_name", **self.params['query'])

    @add_res_to_DB()
    def test_19_lead_last_name(self):
        test_input(self, "lead_last_name", **self.params['query'])

    @add_res_to_DB()
    def test_20_lead_email(self):
        test_input(self, "lead_email", **self.params['query'])

    @add_res_to_DB()
    def test_21_lead_phone(self):
        test_input(self, "lead_phone_resident", **self.params['query'])

    @add_res_to_DB()
    def test_22_confidant_first_name(self):
        test_input(self, "confidant_first_name", **self.params['query'])

    @add_res_to_DB()
    def test_23_confidant_last_name(self):
        test_input(self, "confidant_last_name", **self.params['query'])

    @add_res_to_DB()
    def test_24_confidant_position(self):
        test_input(self, "confidant_position", **self.params['query'])

    @add_res_to_DB()
    def test_25_confidant_email(self):
        test_input(self, "confidant_email", **self.params['query'])

    @add_res_to_DB()
    def test_26_confidant_phone(self):
        test_input(self, "confidant_phone_resident", **self.params['query'])

    @add_res_to_DB()
    def test_27_contract_offer(self):
        contract_offer_check = self.wts.drv.find_element_by_xpath(".//*[@id='contract_offer_container']/label")
        contract_offer_check.click()
       # WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.XPATH, "")))

    @add_res_to_DB()
    def test_28_save(self):
        btn_save = self.wts.drv.find_element_by_id("save_company_bottom")
        btn_save.click()

        #WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "btn_edit")))
