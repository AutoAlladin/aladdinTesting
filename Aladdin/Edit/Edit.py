from Aladdin.AladdinUtils import *
from Aladdin.Authorization.Login import Login
from Aladdin.decorators.ParamsTestCase import ParamsTestCase


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
        WebDriverWait(self.wts.drv, 10).until(EC.element_to_be_clickable((By.ID, "profile_tab_company")))
        btn_tab_company = self.wts.drv.find_element_by_id("profile_tab_company")
        btn_tab_company.click()
        WebDriverWait(self.wts.drv, 10).until(EC.element_to_be_clickable((By.ID, "btn_edit")))
        self.wts.drv.execute_script("window.scrollTo(0, 0);")

    def test_03_click_btn_edit(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "btn_edit")))
        btn_edit = self.wts.drv.find_element_by_id("btn_edit")
        self.wts.drv.execute_script("window.scrollBy(0, 1500);")
        btn_edit.click()

    def test_04_clear_field_comp_name(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "nameUA")))
        f_comp_name = self.wts.drv.find_element_by_id("nameUA")
        f_comp_name.clear()


    def test_05_update_comp_name(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "nameUA")))
        test_input(self, "nameUA", **self.params['query'])


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

    def test_11_clear_field_real_add_str(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "real_address_street")))
        f_real_add = self.wts.drv.find_element_by_id("real_address_street")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "real_address_street")))
        f_real_add.clear()

    def test_12_real_address_street(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "real_address_street")))
        test_input(self, "real_address_street", **self.params['query'])

    def test_13_clear_add_index(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "real_address_index")))
        add_index = self.wts.drv.find_element_by_id("real_address_index")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "real_address_index")))
        add_index.clear()

    def test_14_real_address_index(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "real_address_index")))
        test_input(self, "real_address_index", **self.params['query'])

    def test_15_clear_comp_bank_acc_mfo(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "company_bank_account_mfo")))
        comp_bank_acc_mfo = self.wts.drv.find_element_by_id("company_bank_account_mfo")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "company_bank_account_mfo")))
        comp_bank_acc_mfo.clear()

    def test_16_comp_bank_acc_mfo(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "company_bank_account_mfo")))
        test_input(self, "company_bank_account_mfo", **self.params['query'])
        self.wts.drv.execute_script("window.scrollBy(0, 300);")

    def test_17_clear_lead_phone(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "lead_phone_resident")))
        lead_phone = self.wts.drv.find_element_by_id("lead_phone_resident")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "lead_phone_resident")))
        lead_phone.clear()

    def test_18_lead_phone(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "lead_phone_resident")))
        test_input(self, "lead_phone_resident", **self.params['query'])
        self.wts.drv.execute_script("window.scrollBy(0, 1500);")

    def test_19_clear_confidant_first_name(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "confidant_first_name")))
        conf_fst_name = self.wts.drv.find_element_by_id("confidant_first_name")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "confidant_first_name")))
        conf_fst_name.clear()

    def test_20_confidant_first_name(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "confidant_first_name")))
        test_input(self, "confidant_first_name", **self.params['query'])

    def test_21_clear_confidant_position(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "confidant_position")))
        f_conf_position = self.wts.drv.find_element_by_id("confidant_position")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "confidant_position")))
        f_conf_position.clear()

    def test_22_confidant_position(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "confidant_position")))
        test_input(self, "confidant_position", **self.params['query'])

    def test_23_click_btn_save_changes(self):
    #self.wts.drv.execute_script("window.scrollTo(0, 2500);")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "btn_save_changes")))
        btn_s_changes = self.wts.drv.find_element_by_id("btn_save_changes")
        btn_s_changes.click()
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "btn_edit")))

    def test_24_click_tab_profile_tab_about(self):
        self.wts.drv.execute_script("window.scrollTo(0, 0);")
        #WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "profile_tab_about")))
        tab_personal_data = self.wts.drv.find_element_by_id("profile_tab_about")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "profile_tab_about")))
        tab_personal_data.click()

    def test_25_name_clear(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "userFirstName")))
        name_clear = self.wts.drv.find_element_by_id("userFirstName")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "userFirstName")))
        name_clear.clear()

    def test_26_name_change(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "userFirstName")))
        test_input(self, "userFirstName", **self.params['query'])

    def test_27_eng_surname_clear(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "userLastNameEn")))
        surname_clear = self.wts.drv.find_element_by_id("userLastNameEn")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "userLastNameEn")))
        surname_clear.clear()

    def test_28_eng_surname_change(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "userLastNameEn")))
        test_input(self, "userLastNameEn", **self.params['query'])

    def test_29_clear_phone(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "userPhone")))
        u_phone_clear = self.wts.drv.find_element_by_id("userPhone")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "userPhone")))
        u_phone_clear.clear()

    def test_30_change_u_phone(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "userPhone")))
        test_input(self, "userPhone", **self.params['query'])
        self.wts.drv.execute_script("window.scrollTo(250, 0);")

    def test_31_clear_u_position(self):
        u_pos_clear = self.wts.drv.find_element_by_id("userPosition")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "userPosition")))
        u_pos_clear.clear()

    def test_32_change_u_position(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "userPosition")))
        test_input(self, "userPosition", **self.params['query'])

    def test_33_click_btnSaveUser(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "btnSaveUser")))
        btnSaveUser = self.wts.drv.find_element_by_id("btnSaveUser")
        btnSaveUser.click()

















