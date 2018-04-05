from datetime import time

from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase

from Aladdin.Accounting.AladdinUtils import *
from Prozorro.Utils import *


class UserRegistrationEDRPOU(ParamsTestCase):

    def test_01_company_name(self):
        test_input(self, "nameUA", **self.params['query'])

    def test_02_company_name_en(self):
        test_input(self, "nameEN", **self.params['query'])

    def test_03_check_ownership(self):
        test_select(self, "ownership_type", **self.params['query'])

    def test_04_code_edrpou(self):
        test_input(self, "company_code_USREOU", **self.params['query'])
        company_code_USREOU = self.wts.__mongo__.test_params.find_one(self.params['query']["q"])

        val = (company_code_USREOU["inputs"]["company_code_USREOU_val"]+1)
        code = str(val).rjust(8, "0")

        self.wts.__mongo__.test_params.update_one({"_id": company_code_USREOU["_id"]},
                                                  {"$set": {"inputs.company_code_USREOU_val": val}})
        self.wts.__mongo__.test_params.update_one({"_id": company_code_USREOU["_id"]},
                                                  {"$set": {"inputs.company_code_USREOU": code}})


    def test_05_name(self):
        test_input(self, "admin_name_ua", **self.params['query'])

    def test_06_name_en(self):
        test_input(self, "admin_name_en", **self.params['query'])

    def test_07_last_name(self):
        test_input(self, "admin_last_name_ua", **self.params['query'])

    def test_08_last_name_en(self):
        test_input(self, "admin_last_name_en", **self.params['query'])

    def test_09_position(self):
        test_input(self, "position", **self.params['query'])

    def test_10_phone(self):
        test_input(self, "resident_phone", **self.params['query'])

    #@create_result_DB


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


    def test_12_password(self):
        test_input(self, "password", **self.params['query'])
        psw = self.wts.__mongo__.test_params.find_one(self.params['query']["q"])
        self.parent_suite.suite_params.update({"password": psw["inputs"]["password"]})
        self.log("password " + self.parent_suite.suite_params["password"])
        print("password", self.parent_suite.suite_params["password"])


    def test_13_confirm_password(self):
        test_input(self, "confirm_password", **self.params['query'])
        policy_chb = self.wts.drv.find_element_by_css_selector("#content > div > div > div > div > div > div > form > div.personal-data > div:nth-child(7) > div > div > label")
        WebDriverWait(self.wts.drv, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#content > div > div > div > div > div > div > form > div.personal-data > div:nth-child(7) > div > div > label")))
        #policy_chb = self.wts.drv.find_element_by_xpath("//input[@id='user_agreementPolicy']/../label")
        #policy_chb = self.wts.drv.find_element_by_id("user_agreementPolicy")
        #time.sleep(10)
        policy_chb.click()

    def test_14_click_next_step_btn(self):
        try:
            next_step_btn = self.wts.drv.find_element_by_id("btn_next_step")
            self.wts.drv.execute_script("window.scroll(0, {0}-{1})".format(next_step_btn.location.get("y"),0))
            WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "btn_next_step")))
            next_step_btn.click()

            #self.wts.drv.execute_script("window.scroll(0, 2000)")

            WebDriverWait(self.wts.drv, 30).until(
                EC.element_to_be_clickable((By.ID, "btn_save_changes")))


            btn_edit = self.wts.drv.find_element_by_id("btn_save_changes")

            self.assertIsNotNone(btn_edit)
        except Exception as e:
            self.assertTrue(False, 'Не отображается кнопка Зберегти\n' + e.__str__())

