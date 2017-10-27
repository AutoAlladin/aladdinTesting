import unittest

from Aladdin.AladdinUtils import *
from Prozorro.Utils import *
from Aladdin.Registration.OpenMainPage import *


class UserRegistrationEDRPOU(OpenMainPage):
    query = {"input_val": None, "q": {"name": "UserRegistrationForm", "version": "0.0.0.3"}}
    test_params = {}

    def test_01_company_name(self):
        test_input(self, "nameUA", **self.query)

    def test_02_company_name_en(self):
        test_input(self, "nameEN", **self.query)

    def test_03_check_ownership(self):
        test_select(self, "ownership_type", **self.query)

    def test_04_code_edrpou(self):
        test_input(self, "company_code_USREOU", **self.query)
        company_code_USREOU = self.wts.__mongo__.test_params.find_one(self.query["q"])

        val = company_code_USREOU["inputs"]["company_code_USREOU_val"]+1
        code = str(val).rjust(8, "0")

        # print(val)
        # print(code)

        self.wts.__mongo__.test_params.update_one({"_id": company_code_USREOU["_id"]},
                                                  {"$set": {"inputs.company_code_USREOU_val": val}})
        self.wts.__mongo__.test_params.update_one({"_id": company_code_USREOU["_id"]},
                                                  {"$set": {"inputs.company_code_USREOU": code}})



    def test_05_name(self):
        test_input(self, "admin_name_ua", **self.query)

    def test_06_name_en(self):
        test_input(self, "admin_name_en", **self.query)

    def test_07_last_name(self):
        test_input(self, "admin_last_name_ua", **self.query)

    def test_08_last_name_en(self):
        test_input(self, "admin_last_name_en", **self.query)

    def test_09_position(self):
        test_input(self, "position", **self.query)

    def test_10_phone(self):
        test_input(self, "resident_phone", **self.query)

    def test_11_email(self):
        test_input(self, "email", **self.query)
        eml = self.wts.__mongo__.test_params.find_one(self.query["q"])
        self.test_params.update({"email": eml["inputs"]["email"]})
        print("email",  self.test_params["email"])
        next = str(int(eml["inputs"]["email_next"]) + 1)
        self.wts.__mongo__.test_params.update_one({"_id": eml["_id"]}, {
        "$set": {"inputs.email": "forTestRegEmail_" + next.rjust(5, '0') + "@cucumber.com"}})
        self.wts.__mongo__.test_params.update_one({"_id": eml["_id"]}, {"$set": {"inputs.email_next": next}})

    def test_12_password(self):
        test_input(self, "password", **self.query)
        psw = self.wts.__mongo__.test_params.find_one(self.query["q"])
        self.test_params.update({"password": psw["inputs"]["password"]})
        print("password", self.test_params["password"])

    def test_13_confirm_password(self):
        test_input(self, "confirm_password", **self.query)

    def test_14_click_next_step_btn(self):
        try:
            next_step_btn = self.wts.drv.find_element_by_id("btn_next_step")
            next_step_btn.click()
            WebDriverWait(self.wts.drv, 20).until(
                EC.element_to_be_clickable((By.ID, "btn_edit")))
            btn_edit = self.wts.drv.find_element_by_id("btn_edit")
            self.assertIsNotNone(btn_edit)
        except Exception as e:
            self.assertTrue(False, 'Не отображается кнопка Зберегти\n' + e.__str__())


# class UserRegistration_Company(OpenMainPage):
#     query = {"name": "UserCompanyRegistrationForm", "version": "0.0.0.3"}
#
#
#     # def test_01_click_edit_btn(self):
#     #     # Key
#     #     try:
#     #
#     #         WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable(((By.ID, "btn_edit"))))
#     #         edit_btn = self.wts.drv.find_element_by_id("btn_edit")
#     #         scroll_to_element(self.wts.drv,edit_btn,'0')
#     #
#     #         edit_btn.click()
#     #         self.assertTrue(True)
#     #     except Exception as e:
#     #         self.assertTrue(False, 'Не кликается кнопка Редагувати\n' + e.__str__())
#
#     def test_02_tax_system(self):
#         test_select(self, "company_taxSystem", "5")
#
#     def test_03_phone_company(self):
#         test_input(self, "phone", q=self.query)
#
#     def test_04_email_company(self):
#         test_input(self, "email", q=self.query)
#
#     def test_05_country_legal(self):
#         test_select(self, "legal_address_country", q=self.query)
#
#     def test_06_region_legal(self):
#         test_select(self, "legal_address_region", q=self.query)
#
#     def test_07_city_legal(self):
#         test_select(self, "legal_address_city", q=self.query)
#
#     def test_08_legal_address(self):
#         test_input(self, "legal_address_street", q=self.query)
#
#     def test_09_legal_index(self):
#         test_input(self, "legal_address_index", q=self.query)
#
#     def test_10_real_country(self):
#         test_select(self, "real_address_country", q=self.query)
#
#     def test_11_real_region(self):
#         test_select(self, "real_address_region", q=self.query)
#
#     def test_12_real_city(self):
#         test_select(self, "real_address_city", q=self.query)
#
#     def test_13_real_address(self):
#         test_input(self, "real_address_street", q=self.query)
#
#     def test_14_real_index(self):
#         test_input(self, "real_address_index", q=self.query)
#
#     def test_15_bank_name(self):
#         test_input(self, "company_bank_account_name", q=self.query)
#
#     def test_16_bank_mfo(self):
#         test_input(self, "company_bank_account_mfo", q=self.query)
#
#     def test_17_bank_account(self):
#         test_input(self, "company_bank_account_account", q=self.query)
#
#     def test_18_lead_first_name(self):
#         test_input(self, "lead_first_name", q=self.query)
#
#     def test_19_lead_last_name(self):
#         test_input(self, "lead_last_name", q=self.query)
#
#     def test_20_lead_email(self):
#         test_input(self, "lead_email", q=self.query)
#
#     def test_21_lead_phone(self):
#         test_input(self, "lead_phone", q=self.query)
#
#     def test_22_confidant_first_name(self):
#         test_input(self, "confidant_first_name", q=self.query)
#
#     def test_23_confidant_last_name(self):
#         test_input(self, "confidant_last_name", q=self.query)
#
#     def test_24_confidant_position(self):
#         test_input(self, "confidant_position", q=self.query)
#
#     def test_25_confidant_email(self):
#         test_input(self, "confidant_email", q=self.query)
#
#     def test_26_confidant_phone(self):
#         test_input(self, "confidant_phone", q=self.query)
#
#     def test_27_contract_offer(self):
#         contract_offer_check = self.wts.drv.find_element_by_xpath(".//*[@id='contract_offer_container']/label")
#         contract_offer_check.click()
#        # WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.XPATH, "")))
#
#     def test_28_save(self):
#         btn_save = self.wts.drv.find_element_by_id("btn_save_changes")
#         btn_save.click()
#         #WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "btn_save_changes")))
