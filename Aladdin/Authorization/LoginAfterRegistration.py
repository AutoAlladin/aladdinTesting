
from Aladdin.Registration.OpenMainPage import OpenMainPage
from Aladdin.Registration.RegistrationCompanyEDRPOU import RegistrationCompany
from Aladdin.AladdinUtils import *
from Aladdin.Edit.Edit import Edit
from Aladdin.Registration.Employees import Employees
from Aladdin.Docs.Docs import Docs
from Aladdin.decorators.ParamsTestCase import ParamsTestCase
from Aladdin.decorators.StoreTestResult import add_res_to_DB


class LoginAfterRegistrationCompany(ParamsTestCase):

    @add_res_to_DB()
    def test_01(self):
        w={"query": {"q": {"name": "UserCompanyRegistrationForm", "version": "0.0.0.3",
                           'group': self.params['query']['q']['group']}
                   },
           'wts': self.wts
         }

        full_reg = RegistrationCompany(_params=w)

        full_reg.test_01_registration_user()
        full_reg.test_02_tax_system()
        full_reg.test_03_phone_company()
        full_reg.test_04_email_company()
        full_reg.test_05_country_legal()
        full_reg.test_06_region_legal()
        full_reg.test_07_city_legal()
        full_reg.test_08_legal_address()
        full_reg.test_09_legal_index()
        full_reg.test_10_real_country()
        full_reg.test_11_real_region()
        full_reg.test_12_real_city()
        full_reg.test_13_real_address()
        full_reg.test_14_real_index()
        full_reg.test_15_bank_name()
        full_reg.test_16_bank_mfo()
        full_reg.test_17_bank_account()
        full_reg.test_18_lead_first_name()
        full_reg.test_19_lead_last_name()
        full_reg.test_20_lead_email()
        full_reg.test_21_lead_phone()
        full_reg.test_22_confidant_first_name()
        full_reg.test_23_confidant_last_name()
        full_reg.test_24_confidant_position()
        full_reg.test_25_confidant_email()
        full_reg.test_26_confidant_phone()
        full_reg.test_27_contract_offer()
        full_reg.test_28_save()
        self.params["email"] = full_reg.params["email"]
        self.params["password"] = full_reg.params["password"]

    @add_res_to_DB()
    def test_02_exit(self):
        drop_menu = self.wts.drv.find_element_by_xpath("html/body/app/spa/div/nav/div/div[3]/ul/li[2]/a/b")
        drop_menu.click()
        exit_menu = self.wts.drv.find_element_by_xpath("html/body/app/spa/div/nav/div/div[3]/ul/li[2]/ul/li[6]/a")
        exit_menu.click()
        time.sleep(2)

    @add_res_to_DB()
    def test_03_login(self):
        self.wts.drv.get(self.params['login_url'])
        test_input(self, "exampleInputEmail1", self.params["email"])
        test_input(self, "pswd", self.params["password"])
        btn_sub = self.wts.drv.find_element_by_id("submitLogin")
        btn_sub.click()
        time.sleep(2)

    @add_res_to_DB()
    def test_04_edit(self):
        query = {"q": {"name": "EditInfo", "version": "0.0.0.2",
                                           "group": self.params['query']['q']['group']}}
        w = {"query": query, 'wts': self.wts }
        ed = Edit(_params=w)
        ed.test_02_click_tab_company()
        self.wts.drv.execute_script("window.scrollBy(0, 1500);")
        ed.test_03_click_btn_edit()
        ed.test_04_clear_field_comp_name()
        ed.test_05_update_comp_name()
        ed.test_06_tax_system()
        ed.test_08_clear_email()
        ed.test_09_update_email()
        ed.test_10_legal_address_country()
        ed.test_11_clear_field_real_add_str()
        ed.test_12_real_address_street()
        ed.test_13_clear_add_index()
        ed.test_14_real_address_index()
        ed.test_15_clear_comp_bank_acc_mfo()
        ed.test_16_comp_bank_acc_mfo()
        ed.test_17_clear_lead_phone()
        ed.test_18_lead_phone()
        ed.test_19_clear_confidant_first_name()
        ed.test_20_confidant_first_name()
        ed.test_21_clear_confidant_position()
        ed.test_22_confidant_position()
        ed.test_23_click_btn_save_changes()
        ed.test_24_click_tab_profile_tab_about()
        ed.test_25_name_clear()
        ed.test_26_name_change()
        ed.test_27_eng_surname_clear()
        ed.test_28_eng_surname_change()
        ed.test_29_clear_phone()
        ed.test_30_change_u_phone()
        ed.test_31_clear_u_position()
        ed.test_32_change_u_position()
        ed.test_33_click_btnSaveUser()

        time.sleep(2)

    @add_res_to_DB()
    def test_05_add_view_delete_docs(self):
        ds = Docs(_params={})
        ds.wts = self.wts
        ds.test_3_add_doc()
        #ds.test_4_doc_view()
        ds.test_5_doc_delete()
        ds.test_6_doc2_add()
        time.sleep(10)

    @add_res_to_DB()
    def test_06_add_employees(self):
        empl = Employees(_params={"query": {"q": {"name": "EmployeeesInfo", "version": "0.0.0.2",
                                            'group': self.params['query']['q']['group']}
                                           },
                                  'wts': self.wts
                         })

        btn_tab_empl = self.wts.drv.find_element_by_id("profile_tab_employees")
        btn_tab_empl.click()
        empl.test_03_add_user()
        empl.test_04_name()
        empl.test_05_name_eu()
        empl.test_06_last_name()
        empl.test_07_last_name_eu()
        empl.test_08_position()
        empl.test_09_email()
        empl.test_10_phone()
        empl.test_11_role()
        empl.test_12_save()
    #
    # @add_res_to_DB
    # def test_07_edit_employees(self):
    #     empl = Edit_employees()
    #     empl.wts = self.wts
    #     empl.test_01_click_tab_employees()
    #     empl.test_02_update_name()
    #     empl.test_03_update_last_name_eu()
    #     empl.test_04_update_position()
    #     empl.test_05_update_role()
    #     empl.test_06_save()






