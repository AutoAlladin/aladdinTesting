import time

from Aladdin.Accounting import AladdinUtils
from Aladdin.Accounting.AladdinUtils import *
from Aladdin.Accounting.Docs.Docs import Docs
from Aladdin.Accounting.Edit.Edit import Edit
from Aladdin.Accounting.Registration.Employees import Employees
from Aladdin.Accounting.Registration.RegistrationCompanyEDRPOU import RegistrationCompany
from Aladdin.Accounting.Registration.UserRegistrationEDRPOU import UserRegistrationEDRPOU
from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from Aladdin.Accounting.decorators.StoreTestResult import add_res_to_DB

from Prozorro.Utils import waitFadeIn


class LoginAfterRegistrationCompany(ParamsTestCase):
    @add_res_to_DB()
    def test_00_registration_nerez(self):
        w = {"query": {"q": {"name": "UserCompanyRegistrationForm", "version": "0.0.0.3",
                             'group': self.params['query']['q']['group']}
                       },
             'wts': self.wts
             }

        #  RegistrationCompany -> UserRegistrationEDRPOU ->
        # получаем и сохраняем в параметрах сьюита логин и пароль при первой  регистрации
        full_reg = UserRegistrationEDRPOU(_params=w, _parent_suite=self.parent_suite)
        full_reg.test_00_no_resident()




    @add_res_to_DB()
    def test_01(self):
        w={"query": {"q": {"name": "UserCompanyRegistrationForm", "version": "0.0.0.3",
                           'group': self.params['query']['q']['group']}
                   },
           'wts': self.wts
         }


        #  RegistrationCompany -> UserRegistrationEDRPOU ->
        # получаем и сохраняем в параметрах сьюита логин и пароль при первой  регистрации
        full_reg = RegistrationCompany(_params=w, _parent_suite= self.parent_suite)


        full_reg.test_01_registration_user()

        self.test_03_login()

        # company_tab =  self.wts.w_id("profile_tab_company",20)
        # waitFadeIn(self.wts.drv)
        # company_tab.click()
        # waitFadeIn(self.wts.drv)

        full_reg.test_02_tax_system()
        full_reg.test_03_phone_company()
        full_reg.test_04_email_company()
        full_reg.test_05_country_legal()
        full_reg.test_06_region_legal()
        full_reg.test_07_city_legal()
        full_reg.test_08_legal_address()
        full_reg.test_09_legal_index()

        full_reg.test_10_real_country()
        time.sleep(0.5)
        full_reg.test_11_real_region()
        time.sleep(1)
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

    # @add_res_to_DB()
    # def test_02_exit(self):
    #     drop_menu = self.wts.drv.find_element_by_xpath("html/body/app/spa/div/nav/div/div[3]/ul/li[2]/a/b")
    #     drop_menu.click()
    #     exit_menu = self.wts.drv.find_element_by_xpath("html/body/app/spa/div/nav/div/div[3]/ul/li[2]/ul/li[6]/a")
    #     exit_menu.click()
    #     time.sleep(2)

    @add_res_to_DB()
    def test_03_login(self):
        #self.wts.drv.get(self.params['login_url'])
        test_input(self, "exampleInputEmail1", self.parent_suite.suite_params["email"])
        test_input(self, "pswd", self.parent_suite.suite_params["password"])
        btn_sub = self.wts.drv.find_element_by_id("submitLogin")
        btn_sub.click()
        time.sleep(2)

    @add_res_to_DB()
    def test_04_edit(self):
        query = {"q": {"name": "EditInfo", "version": "0.0.0.2",
                                           "group": self.params['query']['q']['group']}}
        w = {"query": query, 'wts': self.wts }
        ed = Edit(_params=w)
        #ed.test_02_click_tab_company()
        self.wts.drv.execute_script("window.scrollBy(0, -1500);")
        ed.test_03_click_btn_edit()
        ed.test_04_clear_field_comp_name()
        ed.test_05_update_comp_name()
        ed.test_06_tax_system()
        ed.test_07_phone_ad()
        ed.test_08_clear_email()
        ed.test_09_update_email()
        ed.test_10_legal_address_country()
        ed.test_11_legal_address_region()
        ed.test_12_legal_address_city()
        ed.test_13_legal_address_street()
        ed.test_14_legal_address_index()
        ed.test_15_real_address_country()
        ed.test_16_real_address_region()
        ed.test_18_real_address_city()
        ed.test_19_clear_field_real_add_str()
        ed.test_20_real_address_street()
        ed.test_21_clear_add_index()
        ed.test_22_real_address_index()
        ed.test_23_bank_name()
        ed.test_24_clear_comp_bank_acc_mfo()
        ed.test_25_comp_bank_acc_mfo()
        ed.test_26_bank_account()
        ed.test_27_lead_name()
        ed.test_28_lead_surname()
        ed.test_29_lead_email()
        ed.test_30_clear_lead_phone()
        ed.test_31_lead_phone()
        ed.test_32_clear_confidant_first_name()
        ed.test_33_confidant_first_name()
        ed.test_34_confidant_last_name()
        ed.test_35_confidant_email()
        ed.test_36_confidant_phone()
        ed.test_37_clear_confidant_position()
        ed.test_38_confidant_position()
        ed.test_39_click_btn_save_changes()
        ed.test_40_click_tab_profile_tab_about()
        ed.test_41_name_clear()
        ed.test_42_name_change()
        ed.test_43_eng_surname_clear()
        ed.test_44_eng_surname_change()
        ed.test_45_clear_phone()
        ed.test_46_change_u_phone()
        ed.test_47_clear_u_position()
        ed.test_48_change_u_position()
        ed.test_49_click_btnSaveUser()

        time.sleep(2)

    @add_res_to_DB()
    def test_05_add_view_delete_docs(self):
        ds = Docs(_params={})
        ds.wts = self.wts
        ds.test_3_add_doc()
        #ds.test_4_doc_view()
        ds.test_5_doc_delete()
        ds.test_6_doc2_add()
        time.sleep(5)

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
        empl.test_13_delete()
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






