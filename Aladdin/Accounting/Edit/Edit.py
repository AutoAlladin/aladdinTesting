import time

from Aladdin.Accounting.Authorization.Login import Login
from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from selenium.webdriver.common.keys import Keys

from Aladdin.Accounting.AladdinUtils import *
from Aladdin.Accounting.decorators.StoreTestResult import add_res_to_DB

class Edit(ParamsTestCase):

    def test_01_go_to_user_profile(self):
        l = Login(_params={"q": {"name": "Login", "version": "0.0.0.2",
                                 'group': self.params['query']['q']['group']},
                           'wts': self.wts})
        l.test_01_email()
        l.test_02_pswd()
        l.test_03_btn()
        user_prof = self.wts.drv.find_element_by_id("link_about")
        user_prof.click()


    def test_02_click_tab_company(self):
        # WebDriverWait(self.wts.drv, 10).until(EC.element_to_be_clickable((By.ID, "profile_tab_company")))
        # btn_tab_company = self.wts.drv.find_element_by_id("profile_tab_company")
        # btn_tab_company.click()
        # time.sleep(5)
        #WebDriverWait(self.wts.drv, 10).until(EC.element_to_be_clickable((By.ID, "btn_edit")))
        #self.wts.drv.execute_script("window.scrollTo(0, 0);")
        pass

    @add_res_to_DB()
    def test_03_click_btn_edit(self):
        self.wts.drv.execute_script("window.scrollTo(0, 0);")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "btn_edit_no_active")))
        btn_edit = self.wts.drv.find_element_by_id("btn_edit_no_active")
        time.sleep(2)
        btn_edit.click()
        time.sleep(5)

    def test_04_clear_field_comp_name(self):
        #f_comp_name = self.wts.drv.find_element_by_id("nameUA")
        #WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "nameUA")))
        #f_comp_name.clear()
        pass

        #WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "nameUA")))
        #input_ELEMENT_IN_BROWSER_U_KOTOROGO_EST_METODY = self.wts.drv.find_element_by_id("nameUA")
        ####self.wts.drv.execute_script("window.scrollBy(0, 1500);")
        #test_KOTORYI_IZ_ELEMENTA_NET_METODA_SEND_KEYS = input_ELEMENT_IN_BROWSER_U_KOTOROGO_EST_METODY.get_attribute('value')
        #print("Текст, который находится в веб єлементе" + test_KOTORYI_IZ_ELEMENTA_NET_METODA_SEND_KEYS)
        #time.sleep(5)
        #le = len(test_KOTORYI_IZ_ELEMENTA_NET_METODA_SEND_KEYS)
        #deleter=""
        #for n in range(le):
            #deleter += Keys.BACK_SPACE
        #input_ELEMENT_IN_BROWSER_U_KOTOROGO_EST_METODY.send_keys(deleter)
        #time.sleep(1)
        #time.sleep(1)

        ####self.wts.drv.execute_script("$("#nameUA").val('');")
        ####self.wts.drv.execute_script("nameUA".val('');")
        ####self.wts.drv.execute_script("#nameUA").val('');""


    def test_05_update_comp_name(self):
        # time.sleep(2)
        # WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "nameUA")))
        # test_input(self, "nameUA", **self.params['query'])
        pass

    def test_06_tax_system(self):
        #tax_system = self.wts.drv.find_element_by_id("company_taxSystem")
        #WebDriverWait(self.wts.drv, 10).until(EC.element_to_be_clickable((By.ID, "company_taxSystem")))
        #test_select(self, "company_taxSystem", **self.params['query'])
        pass


    def test_07_phone_ad(self):
        upd_phone = self.wts.drv.find_element_by_id("resident_phone")
        upd_phone.clear()
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "resident_phone")))
        test_input(self, "resident_phone", **self.params['query'])

    def test_08_clear_email(self):
        upd_email = self.wts.drv.find_element_by_id("email")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "email")))
        upd_email.clear()

    def test_09_update_email(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "email")))
        test_input(self, "email", **self.params['query'])

    def test_10_legal_address_country(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "legal_address_country")))
        test_select(self, "legal_address_country", **self.params['query'])

    def test_11_legal_address_region(self):
        test_select(self, "legal_address_region", **self.params['query'])

    def test_12_legal_address_city(self):
        test_select(self, "legal_address_city", **self.params['query'])

    def test_13_legal_address_street(self):
        upd_str = self.wts.drv.find_element_by_id("legal_address_street")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "legal_address_street")))
        upd_str.clear()
        test_input(self, "legal_address_street", **self.params['query'])

    def test_14_legal_address_index(self):
        upd_index = self.wts.drv.find_element_by_id("legal_address_index")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "legal_address_index")))
        upd_index.clear()
        test_input(self, "legal_address_index", **self.params['query'])

    def test_15_real_address_country(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "real_address_country")))
        test_select(self, "real_address_country", **self.params['query'])


    def test_16_real_address_region(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "real_address_region")))
        test_select(self, "real_address_region", **self.params['query'])
        time.sleep(5)

    def test_18_real_address_city(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "real_address_city")))
        test_select(self, "real_address_city", **self.params['query'])

    def test_19_clear_field_real_add_str(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "real_address_street")))
        f_real_add = self.wts.drv.find_element_by_id("real_address_street")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "real_address_street")))
        f_real_add.clear()

    def test_20_real_address_street(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "real_address_street")))
        test_input(self, "real_address_street", **self.params['query'])

    def test_21_clear_add_index(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "real_address_index")))
        add_index = self.wts.drv.find_element_by_id("real_address_index")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "real_address_index")))
        add_index.clear()

    def test_22_real_address_index(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "real_address_index")))
        test_input(self, "real_address_index", **self.params['query'])

    def test_23_bank_name(self):
        comp_bank_name = self.wts.drv.find_element_by_id("company_bank_account_name")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "company_bank_account_name")))
        comp_bank_name.clear()
        test_input(self, "company_bank_account_name", **self.params['query'])

    def test_24_clear_comp_bank_acc_mfo(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "company_bank_account_mfo")))
        comp_bank_acc_mfo = self.wts.drv.find_element_by_id("company_bank_account_mfo")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "company_bank_account_mfo")))
        comp_bank_acc_mfo.clear()

    def test_25_comp_bank_acc_mfo(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "company_bank_account_mfo")))
        test_input(self, "company_bank_account_mfo", **self.params['query'])
        self.wts.drv.execute_script("window.scrollBy(0, 300);")

    def test_26_bank_account(self):
        comp_bank_ac = self.wts.drv.find_element_by_id("company_bank_account_account")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "company_bank_account_account")))
        comp_bank_ac.clear()
        test_input(self, "company_bank_account_account", **self.params['query'])

    def test_27_lead_name(self):
        lead_name = self.wts.drv.find_element_by_id("lead_first_name")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "lead_first_name")))
        lead_name.clear()
        test_input(self, "lead_first_name", **self.params['query'])

    def test_28_lead_surname(self):
        lead_sname = self.wts.drv.find_element_by_id("lead_last_name")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "lead_last_name")))
        lead_sname.clear()
        test_input(self, "lead_last_name", **self.params['query'])

    def test_29_lead_email(self):
        lead_mail = self.wts.drv.find_element_by_id("lead_email")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "lead_email")))
        lead_mail.clear()
        test_input(self, "lead_email", **self.params['query'])

    def test_30_clear_lead_phone(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "lead_phone_resident")))
        lead_phone = self.wts.drv.find_element_by_id("lead_phone_resident")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "lead_phone_resident")))
        lead_phone.clear()

    def test_31_lead_phone(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "lead_phone_resident")))
        test_input(self, "lead_phone_resident", **self.params['query'])
        self.wts.drv.execute_script("window.scrollBy(0, 1500);")

    def test_32_clear_confidant_first_name(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "confidant_first_name")))
        conf_fst_name = self.wts.drv.find_element_by_id("confidant_first_name")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "confidant_first_name")))
        conf_fst_name.clear()

    def test_33_confidant_first_name(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "confidant_first_name")))
        test_input(self, "confidant_first_name", **self.params['query'])

    def test_34_confidant_last_name(self):
        conf_lst_name = self.wts.drv.find_element_by_id("confidant_last_name")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "confidant_last_name")))
        conf_lst_name.clear()
        test_input(self, "confidant_last_name", **self.params['query'])

    def test_35_confidant_email(self):
        conf_mail = self.wts.drv.find_element_by_id("confidant_email")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "confidant_email")))
        conf_mail.clear()
        test_input(self, "confidant_email", **self.params['query'])

    def test_36_confidant_phone(self):
        conf_phone = self.wts.drv.find_element_by_id("confidant_phone_resident")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "confidant_phone_resident")))
        conf_phone.clear()
        test_input(self, "confidant_phone_resident", **self.params['query'])

    def test_37_clear_confidant_position(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "confidant_position")))
        f_conf_position = self.wts.drv.find_element_by_id("confidant_position")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "confidant_position")))
        f_conf_position.clear()


    def test_38_confidant_position(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "confidant_position")))
        test_input(self, "confidant_position", **self.params['query'])

    @add_res_to_DB()
    def test_39_click_btn_save_changes(self):
    #self.wts.drv.execute_script("window.scrollTo(0, 2500);")
        contract_offer_s = self.wts.drv.find_element_by_xpath("//*[@id='contract_offer_container']/label")
        contract_offer_s.click()

        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "save_company_bottom")))

        btn_s_changes = self.wts.drv.find_element_by_id("save_company_bottom")
        btn_s_changes.click()
        time.sleep(5)
        #WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "btn_edit")))

    @add_res_to_DB()
    def test_40_click_tab_profile_tab_about(self):
        self.wts.drv.execute_script("window.scrollTo(0, 0);")
        #WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "profile_tab_about")))
        tab_personal_data = self.wts.drv.find_element_by_id("profile_tab_about")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "profile_tab_about")))
        tab_personal_data.click()

    def test_41_name_clear(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "userFirstName")))
        name_clear = self.wts.drv.find_element_by_id("userFirstName")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "userFirstName")))
        name_clear.clear()

    def test_42_name_change(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "userFirstName")))
        test_input(self, "userFirstName", **self.params['query'])

    def test_43_eng_surname_clear(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "userLastNameEn")))
        surname_clear = self.wts.drv.find_element_by_id("userLastNameEn")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "userLastNameEn")))
        surname_clear.clear()

    def test_44_eng_surname_change(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "userLastNameEn")))
        test_input(self, "userLastNameEn", **self.params['query'])

    def test_45_clear_phone(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "userPhone")))
        u_phone_clear = self.wts.drv.find_element_by_id("userPhone")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "userPhone")))
        u_phone_clear.clear()

    def test_46_change_u_phone(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "userPhone")))
        test_input(self, "userPhone", **self.params['query'])
        self.wts.drv.execute_script("window.scrollTo(250, 0);")

    def test_47_clear_u_position(self):
        u_pos_clear = self.wts.drv.find_element_by_id("userPosition")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "userPosition")))
        u_pos_clear.clear()

    def test_48_change_u_position(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "userPosition")))
        test_input(self, "userPosition", **self.params['query'])

    @add_res_to_DB()
    def test_49_click_btnSaveUser(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "btnSaveUser")))
        btnSaveUser = self.wts.drv.find_element_by_id("btnSaveUser")
        btnSaveUser.click()
















