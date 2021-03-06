from Aladdin.Accounting.AladdinUtils import *
from Aladdin.Accounting.Authorization.Login import Login
from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from Aladdin.Accounting.decorators.StoreTestResult import add_res_to_DB
from Aladdin.Accounting.Edit.Edit import Edit
import time

class Employees(ParamsTestCase):

    @add_res_to_DB()
    def test_01_go_to_user_profile(self):
        log = Login()
        log.wts = self.wts
        log.wts.set_main_page()
        log.test_01_email()
        log.test_02_pswd()
        log.test_03_btn()

    @add_res_to_DB()
    def test_02_tab_empl(self):
        ed = Edit()
        ed.wts = self.wts
        ed.test_01_go_to_user_profile()

        btn_tab_empl = self.wts.drv.find_element_by_id("profile_tab_employees")
        btn_tab_empl.click()

    @add_res_to_DB()
    def test_03_add_user(self):
        btn_add_user = self.wts.drv.find_element_by_id("butAddNewUser")
        time.sleep(5)
        btn_add_user.click()

    @add_res_to_DB()
    def test_04_name(self):
        test_input(self, "firstName_", **self.params["query"])

    @add_res_to_DB()
    def test_05_name_eu(self):
        test_input(self, "firstNameEn_", **self.params["query"])

    @add_res_to_DB()
    def test_06_last_name(self):
        test_input(self, "lastName_", **self.params["query"])

    @add_res_to_DB()
    def test_07_last_name_eu(self):
        test_input(self, "lastNameEn_", **self.params["query"])

    @add_res_to_DB()
    def test_08_position(self):
        test_input(self, "position_", **self.params["query"])

    @add_res_to_DB()
    def test_09_email(self):
        test_input(self, "userEmail", **self.params["query"])
        eml = self.wts.__mongo__.test_params.find_one(self.params["query"]["q"])
        time.sleep(3)
        self.params.update({"userEmail": eml["inputs"]["userEmail"]})
        print("email", self.params["userEmail"])
        next = str(int(eml["inputs"]["email_next"]) + 1)
        self.wts.__mongo__.test_params.update_one({"_id": eml["_id"]}, {
            "$set": {"inputs.userEmail": "employeesmail_" + next.rjust(5, '0') + "@ff.ru"}})
        self.wts.__mongo__.test_params.update_one({"_id": eml["_id"]}, {"$set": {"inputs.email_next": next}})

    @add_res_to_DB()
    def test_10_phone(self):
        test_input(self, "userPhone", **self.params["query"])

    @add_res_to_DB()
    def test_11_role(self):
        role_ = self.wts.drv.find_element_by_xpath("//p-multiselect[@formcontrolname='roles']/div/div/label")
        time.sleep(5)
        role_.click()
        role_check = self.wts.drv.find_element_by_xpath("//div[@class='ui-chkbox-box ui-widget ui-corner-all ui-state-default']")
        time.sleep(5)
        role_check.click()

        time.sleep(5)

    @add_res_to_DB()
    def test_12_save(self):
        btn_save = self.wts.drv.find_element_by_id("save_changes_")
        btn_save.click()
        time.sleep(5)

    @add_res_to_DB()
    def test_13_delete(self):
        btn_del = self.wts.drv.find_element_by_xpath(".//*[contains(@id, 'delete_empoyee_')]")
        time.sleep(5)
        btn_del.click()
        btn_del_real = self.wts.drv.find_element_by_xpath("// div[contains(@class ,'jconfirm-box-container')] // button[1]")
        #btn_del_real = self.wts.drv.find_element_by_id("edit_empoyee_")
        time.sleep(5)
        btn_del_real.click()
        time.sleep(2)

        wanted_email=None
        email_list = self.wts.drv.find_elements_by_xpath(".//*[contains(@id, 'userEmail')]")
        inp_email = self.params['userEmail']
        for email in email_list:
            if email.text == inp_email:
                wanted_email = inp_email
                print("Все ОК, email отображается")
                break

        if wanted_email==None:
            print("Сотрудник не добавлен")




