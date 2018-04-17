from datetime import time
from time import sleep

from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase

from Aladdin.Accounting.AladdinUtils import *
from Prozorro.Utils import *
from Aladdin.Accounting.decorators.StoreTestResult import add_res_to_DB

class UserRegistrationEDRPOU(ParamsTestCase):

    @add_res_to_DB()
    def test_00_no_resident(self):
        sleep(0.5)
        no_res = self.wts.w_xpath("// label[@for ='resident']")
        sleep(0.5)
        no_res.click()
        test_select(self, "ownership_type", "6a80945d-ff2d-4e9c-8d3f-8718b885bb21")
        test_input(self, "comapny_code_USREOUNotResident", "123456789987654")
        sleep(0.5)
        no_res.click()
        sleep(0.5)
        test_input(self, "no_resident_phone", "+1234567890245")

    @add_res_to_DB()
    def test_01_company_name(self):
        test_input(self, "nameUA", **self.params['query'])

    @add_res_to_DB()
    def test_02_company_name_en(self):
        test_input(self, "nameEN", **self.params['query'])

    @add_res_to_DB()
    def test_03_check_ownership(self):
        test_select(self, "ownership_type", **self.params['query'])

    @add_res_to_DB()
    def test_04_code_edrpou(self):
        test_input(self, "company_code_USREOU", **self.params['query'])
        company_code_USREOU = self.wts.__mongo__.test_params.find_one(self.params['query']["q"])

        val = (company_code_USREOU["inputs"]["company_code_USREOU_val"]+1)
        code = str(val).rjust(8, "0")

        self.wts.__mongo__.test_params.update_one({"_id": company_code_USREOU["_id"]},
                                                  {"$set": {"inputs.company_code_USREOU_val": val}})
        self.wts.__mongo__.test_params.update_one({"_id": company_code_USREOU["_id"]},
                                                  {"$set": {"inputs.company_code_USREOU": code}})

    @add_res_to_DB()
    def test_05_name(self):
        test_input(self, "admin_name_ua", **self.params['query'])

    @add_res_to_DB()
    def test_06_name_en(self):
        test_input(self, "admin_name_en", **self.params['query'])

    @add_res_to_DB()
    def test_07_last_name(self):
        test_input(self, "admin_last_name_ua", **self.params['query'])

    @add_res_to_DB()
    def test_08_last_name_en(self):
        test_input(self, "admin_last_name_en", **self.params['query'])

    @add_res_to_DB()
    def test_09_position(self):
        test_input(self, "position", **self.params['query'])

    @add_res_to_DB()
    def test_10_phone(self):
        test_input(self, "resident_phone", **self.params['query'])

    #@create_result_DB

    @add_res_to_DB()
    def test_11_email(self):
        test_input(self, "email", **self.params['query'])
        eml = self.wts.__mongo__.test_params.find_one(self.params['query']["q"])
        self.parent_suite.suite_params.update({"email": eml["inputs"]["email"]})
        self.log("email " + self.parent_suite.suite_params["email"])
        print("email",  self.parent_suite.suite_params["email"])
        next = str(int(eml["inputs"]["email_next"]) + 1)
        self.wts.__mongo__.test_params.update_one({"_id": eml["_id"]}, {
        "$set": {"inputs.email": "forTestRegEmail_" + next.rjust(5, '0') + "@cucumber.com"}})
        self.wts.__mongo__.test_params.update_one({"_id": eml["_id"]}, {"$set": {"inputs.email_next": next}})

    @add_res_to_DB()
    def test_12_password(self):
        test_input(self, "password", **self.params['query'])
        psw = self.wts.__mongo__.test_params.find_one(self.params['query']["q"])
        self.parent_suite.suite_params.update({"password": psw["inputs"]["password"]})
        self.log("password " + self.parent_suite.suite_params["password"])
        print("password", self.parent_suite.suite_params["password"])

    @add_res_to_DB()
    def test_13_confirm_password(self):
        test_input(self, "confirm_password", **self.params['query'])
        sleep(0.5)
        policy_chb = self.wts.w_xpath("//input[@id='user_agreementPolicy']/../label")
        sleep(0.5)
        policy_chb.click()

    @add_res_to_DB()
    def test_14_click_next_step_btn(self):
        try:
            next_step_btn = self.wts.drv.find_element_by_id("btn_next_step")
            self.wts.drv.execute_script("window.scroll(0, {0}-{1})".format(next_step_btn.location.get("y"),0))
            WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "btn_next_step")))
            next_step_btn.click()

            btn_edit =  WebDriverWait(self.wts.drv, 30).until(
                EC.element_to_be_clickable((By.ID, "submitLogin")))

            self.assertIsNotNone(btn_edit)
        except Exception as e:
            self.assertTrue(False, 'Не отображается кнопка Зберегти\n' + e.__str__())

