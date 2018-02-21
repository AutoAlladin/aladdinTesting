from Aladdin.Accounting.AladdinUtils import *
from Aladdin.Accounting.Authorization.Login import Login
from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase

from Aladdin.Accounting.Edit.Edit import Edit
import time

class Employees(ParamsTestCase):

    def test_01_go_to_user_profile(self):
        log = Login()
        log.wts = self.wts
        log.wts.set_main_page()
        log.test_01_email()
        log.test_02_pswd()
        log.test_03_btn()

    def test_02_tab_empl(self):
        ed = Edit()
        ed.wts = self.wts
        ed.test_01_go_to_user_profile()

        btn_tab_empl = self.wts.drv.find_element_by_id("profile_tab_employees")
        btn_tab_empl.click()

    def test_03_add_user(self):
        btn_add_user = self.wts.drv.find_element_by_id("butAddNewUser")
        btn_add_user.click()

    def test_04_name(self):
        test_input(self, "firstName_", **self.params["query"])

    def test_05_name_eu(self):
        test_input(self, "firstNameEn_", **self.params["query"])

    def test_06_last_name(self):
        test_input(self, "lastName_", **self.params["query"])

    def test_07_last_name_eu(self):
        test_input(self, "lastNameEn_", **self.params["query"])

    def test_08_position(self):
        test_input(self, "position_", **self.params["query"])

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

    def test_10_phone(self):
        test_input(self, "userPhone", **self.params["query"])

    def test_11_role(self):
        #role_ = self.wts.drv.find_elements_by_xpath("//p-multiselect")
        role_ = self.wts.drv.find_element_by_xpath("//p-multiselect[@formcontrolname='roles']/div/div/label")
        #role_ = self.wts.drv.find_elements_by_xpath("// *[ @class ='ui-multiselect-label-container']")
        role_.click()
        #test_select(self, "//*[@class='ui-multiselect-label ui-corner-all']", "//div[@class='ui-chkbox ui-widget']")
        #role_check = self.wts.drv.find_element_by_xpath("//div[@class='ui-chkbox ui-widget']")
        role_check = self.wts.drv.find_element_by_xpath("//div[@class='ui-chkbox-box ui-widget ui-corner-all ui-state-default']")
        role_check.click()

        time.sleep(2)

    def test_12_save(self):
        btn_save = self.wts.drv.find_element_by_id("save_changes_")
        btn_save.click()
        time.sleep(5)

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




