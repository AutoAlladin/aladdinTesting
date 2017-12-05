from selenium.webdriver.chrome import webdriver
from selenium import webdriver


class UserCompanyForm:
    def __init__(self,_drv):
        self.drv = _drv
        self.drv = webdriver.Chrome(_drv)
        self.select_type = self.drv.find_element_by_id("select_type")
        self.role0 = self.drv.find_element_by_id("role0")
        self.role1 = self.drv.find_element_by_id("role1")
        self.full_name = self.drv.find_element_by_id("full_name")
        self.full_name_en = self.drv.find_element_by_id("full_name_en")
        self.short_name = self.drv.find_element_by_id("short_name")
        self.short_name_en = self.drv.find_element_by_id("short_name_en")
        self.select_scheme_edrpous = self.drv.find_element_by_id("select_scheme_edrpous")
        self.edrpou = self.drv.find_element_by_id("edrpou")
        self.site_url = self.drv.find_element_by_id("site_url")
        self.phones0 = self.drv.find_element_by_id("phones0")
        self.add_phone_btn = self.drv.find_element_by_id("add_phone_")
        self.phones1_added = self.drv.find_element_by_id("phones1")
        self.delete_phone_1_btn = self.drv.find_element_by_id("delete_phone_1")
        self.emails0 = self.drv.find_element_by_id("emails0")
        self.add_email_btn = self.drv.find_element_by_id("add_email_")
        self.emails1_added = self.drv.find_element_by_id("emails1")
        self.delete_email_1_btn = self.drv.find_element_by_id("delete_email_1")
        self.select_countries = self.drv.find_element_by_id("select_countries")
        self.select_regions = self.drv.find_element_by_id("select_regions")
        self.select_cities = self.drv.find_element_by_id("select_cities")
        self.street = self.drv.find_element_by_id("street")
        self.post_code = self.drv.find_element_by_id("post_code")
        self.bankName_0 = self.drv.find_element_by_id("bankName_0")
        self.mfo_0 = self.drv.find_element_by_id("mfo_0")
        self.bankAccount_0 = self.drv.find_element_by_id("bankAccount_0")
        self.add_bank_account_0_btn = self.drv.find_element_by_id("add_bank_account_0")
        self.bankName_1_added = self.drv.find_element_by_id("bankName_1")
        self.mfo_1 = self.drv.find_element_by_id("mfo_1")
        self.bankAccount_1 = self.drv.find_element_by_id("bankAccount_1")
        self.delete_bank_account_1_btn = self.drv.find_element_by_id("delete_bank_account_1")
        self.is_vat = self.drv.find_element_by_id("is_vat")
        self.checkAgreementPolicy = self.drv.find_element_by_id("checkAgreementPolicy")
        self.save_changes_btn = self.drv.find_element_by_id("save_changes")

    def companyForm(self, dic, company):
        self.full_name.send_keys(company["subj_legal_name"])
        self.full_name_en.send_keys(company["subj_legal_name_eng"])
        self.short_name.send_keys(company["subj_short_name"])
        self.short_name_en.send_keys(company["subj_short_name_eng"])
        self.bankName_0.send_keys(company["bank_name"])
        self.mfo_0.send_keys(company["mfo"])
        self.bankAccount_0.send_keys(company["account"])
        self.street.send_keys(company["addr_street"])
        self.post_code.send_keys(company["addr_post_code"])
        Select(select_type).select_by_label("Ownership")










