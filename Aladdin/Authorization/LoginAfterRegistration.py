import unittest
import webbrowser
from Aladdin.AladdinUtils import *
from Aladdin.Registration.OpenMainPage import OpenMainPage
from Aladdin.Registration.RegistrationCompanyEDRPOU import RegistrationCompany
from Aladdin.AladdinUtils import *
from Aladdin.Edit.Edit import Edit
from Aladdin.Registration.Employees import Employees

publicWST = None;
def setUpModule():
    global publicWST
    publicWST = WebTestSession('https://192.168.80.169:44310/i_uk/registration/user')
    #publicWST = WebTestSession('https://identity.ald.in.ua/Account/Login')


def tearDownModule():
    publicWST.drv.close()



class LoginAfterRegistrationCompany(OpenMainPage):
    full_reg = RegistrationCompany()
    wts=None
    @classmethod
    def setUpClass(cls):
        cls.wts = publicWST
    def test_01(self):
        self.full_reg.wts = self.wts
        with self.subTest(msg="registration_user"):
            self.full_reg.test_01_registration_user()
        with self.subTest(msg="tax_system"):
            self.full_reg.test_02_tax_system()

        self.full_reg.test_03_phone_company()
        self.full_reg.test_04_email_company()
        self.full_reg.test_05_country_legal()
        self.full_reg.test_06_region_legal()
        self.full_reg.test_07_city_legal()
        self.full_reg.test_08_legal_address()
        self.full_reg.test_09_legal_index()
        self.full_reg.test_10_real_country()
        self.full_reg.test_11_real_region()
        self.full_reg.test_12_real_city()
        self.full_reg.test_13_real_address()
        self.full_reg.test_14_real_index()
        self.full_reg.test_15_bank_name()
        self.full_reg.test_16_bank_mfo()
        self.full_reg.test_17_bank_account()
        self.full_reg.test_18_lead_first_name()
        self.full_reg.test_19_lead_last_name()
        self.full_reg.test_20_lead_email()
        self.full_reg.test_21_lead_phone()
        self.full_reg.test_22_confidant_first_name()
        self.full_reg.test_23_confidant_last_name()
        self.full_reg.test_24_confidant_position()
        self.full_reg.test_25_confidant_email()
        self.full_reg.test_26_confidant_phone()
        self.full_reg.test_27_contract_offer()
        self.full_reg.test_28_save()

    def test_02_exit(self):
        drop_menu = self.wts.drv.find_element_by_xpath("html/body/app/spa/div/nav/div/div[3]/ul/li[2]/a/b")
        drop_menu.click()
        exit_menu = self.wts.drv.find_element_by_xpath("html/body/app/spa/div/nav/div/div[3]/ul/li[2]/ul/li[6]/a")
        exit_menu.click()
        time.sleep(10)


    def test_03_login(self):
        self.wts.drv.get('https://192.168.80.169:44310/Account/Login')
        test_input(self, "exampleInputEmail1", self.full_reg.reg.test_params["email"])
        test_input(self, "pswd", self.full_reg.reg.test_params["password"])
        btn_sub = self.wts.drv.find_element_by_id("submitLogin")
        btn_sub.click()
        time.sleep(10)

    def test_04_edit(self):
        # user_prof = self.wts.drv.find_element_by_id("link_about")
        # user_prof.click()
        # time.sleep(10)
        # #WebDriverWait(self.wts.drv, 5).until(EC.element_to_be_clickable(By.ID, "profile_tab_company"))
        # btn_tab_company = self.wts.drv.find_element_by_id("profile_tab_company")
        # btn_tab_company.click()
        # self.wts.drv.execute_script("window.scrollTo(0, 2500);")
        #user_prof = self.wts.drv.find_element_by_id("link_about")
        #user_prof.click()
        ed = Edit()
        ed.wts = self.wts
        ed.test_02_click_tab_company()
        time.sleep(10)
        self.wts.drv.execute_script("window.scrollBy(0, 1500);")
        time.sleep(10)
        ed.test_03_click_btn_edit()
        ed.test_04_clear_field_comp_name()
        ed.test_05_update_comp_name()
        #ed.test_06_ownership_type()
        #ed.test_07_company_taxSystem()
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
        time.sleep(10)

    def test_05_add_doc(self):
        self.wts.drv.execute_script("window.scrollTo(0, 0);")
        btn_tab_documents = self.wts.drv.find_element_by_id("profile_tab_documents")
        btn_tab_documents.click()
        WebDriverWait(self.wts.drv, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ui-datatable")))

        taxpayerCertificateINN = self.wts.drv.find_element_by_id("load_TaxpayerCertificateINN")
        file_name = self.wts.__mongo__.get_file(doc_name="TaxpayerCertificateINN")
        taxpayerCertificateINN.send_keys(file_name)

        self.wts.drv.refresh()


    def test_06_add_employees(self):
        empl = Employees()
        empl.wts = self.wts
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


