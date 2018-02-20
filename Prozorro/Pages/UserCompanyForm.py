from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.support.select import Select
from Prozorro import  Utils


class UserCompanyForm:
    def set_actiny_region(self,company):
        if company["addr_region"].strip() == '77':
            Select(self.drv.find_element_by_id("select_regions")). \
                select_by_visible_text("Чернігівська")
        elif company["addr_region"].strip() == '05':
            Select(self.drv.find_element_by_id("select_regions")). \
                select_by_visible_text("Вінницька")
        elif company["addr_region"].strip() == '46':
            Select(self.drv.find_element_by_id("select_regions")). \
                select_by_visible_text("Львівська")
        elif company["addr_region"].strip() == '48':
            Select(self.drv.find_element_by_id("select_regions")). \
                select_by_visible_text("Миколаївська")
        elif company["addr_region"].strip() == '63':
            Select(self.drv.find_element_by_id("select_regions")). \
                select_by_visible_text("Харківська")
        elif company["addr_region"].strip() == '18':
            Select(self.drv.find_element_by_id("select_regions")). \
                select_by_visible_text("Житомирська")
        elif company["addr_region"].strip() == '74':
            Select(self.drv.find_element_by_id("select_regions")). \
                select_by_visible_text("Чернівецька")
        elif company["addr_region"].strip() == '59':
            Select(self.drv.find_element_by_id("select_regions")). \
                select_by_visible_text("Сумська")
        elif company["addr_region"].strip() == '12':
            Select(self.drv.find_element_by_id("select_regions")). \
                select_by_visible_text("Дніпропетровська")
        elif company["addr_region"].strip() == '26':
            Select(self.drv.find_element_by_id("select_regions")). \
                select_by_visible_text("Івано-Франківська")
        elif company["addr_region"].strip() == '21':
            Select(self.drv.find_element_by_id("select_regions")). \
                select_by_visible_text("Закарпатська")
        elif company["addr_region"].strip() == '07':
            Select(self.drv.find_element_by_id("select_regions")). \
                select_by_visible_text("Волинська")
        elif company["addr_region"].strip() == '30':
            Select(self.drv.find_element_by_id("select_regions")). \
                select_by_visible_text("Київська")
        elif company["addr_region"].strip() == '71':
            Select(self.drv.find_element_by_id("select_regions")). \
                select_by_visible_text("Черкаська")
        elif company["addr_region"].strip() == '23':
            Select(self.drv.find_element_by_id("select_regions")). \
                select_by_visible_text("Запорізька")
        elif company["addr_region"].strip() == '56':
            Select(self.drv.find_element_by_id("select_regions")). \
                select_by_visible_text("Рівненська")
        elif company["addr_region"].strip() == '68':
            Select(self.drv.find_element_by_id("select_regions")). \
                select_by_visible_text("Хмельницька")
        elif company["addr_region"].strip() == '14':
            Select(self.drv.find_element_by_id("select_regions")). \
                select_by_visible_text("Донецька")
        elif company["addr_region"].strip() == '65':
            Select(self.drv.find_element_by_id("select_regions")). \
                select_by_visible_text("Херсонська")
        elif company["addr_region"].strip() == '53':
            Select(self.drv.find_element_by_id("select_regions")). \
                select_by_visible_text("Полтавська")
        elif company["addr_region"].strip() == '51':
            Select(self.drv.find_element_by_id("select_regions")). \
                select_by_visible_text("Одеська")
        else:
            Select(self.drv.find_element_by_id("select_regions")). \
                select_by_visible_text("Автономна Республіка Крим")

    def __init__(self,_drv):
        self.drv = _drv
        #self.drv = webdriver.Chrome(_drv)
        self.select_type = self.drv.find_element_by_id("select_type")
        self.role0 = self.drv.find_element_by_xpath("//label[@for='role0']")
        self.role1 = self.drv.find_element_by_xpath("//label[@for='role1']")
        self.full_name = self.drv.find_element_by_id("full_name")
        self.full_name_en = self.drv.find_element_by_id("full_name_en")
        self.short_name = self.drv.find_element_by_id("short_name")
        self.short_name_en = self.drv.find_element_by_id("short_name_en")
        self.select_scheme_edrpous = self.drv.find_element_by_id("select_scheme_edrpous")
        self.edrpou = self.drv.find_element_by_id("edrpou")
        self.site_url = self.drv.find_element_by_id("site_url")
        self.phones0 = self.drv.find_element_by_id("phones0")
        self.emails0 = self.drv.find_element_by_id("emails0")
        self.select_countries = self.drv.find_element_by_id("select_countries")
        self.bankName_0 = self.drv.find_element_by_id("bankName_0")
        self.mfo_0 = self.drv.find_element_by_id("mfo_0")
        self.bankAccount_0 = self.drv.find_element_by_id("bankAccount_0")
        self.add_bank_account_0_btn = self.drv.find_element_by_id("add_bank_account_0")
        self.is_vat = self.drv.find_element_by_id("is_vat")
        self.checkAgreementPolicy = self.drv.find_element_by_id("checkAgreementPolicy")
        self.save_changes_btn = self.drv.find_element_by_id("save_changes")

    def set_subj_legal_name(self, val):
        self.full_name.send_keys(val)

    def set_subj_legal_name_eng(self, val):
        self.full_name_en.send_keys(val)

    def set_subj_short_name(self, val):
        self.short_name.send_keys(val)

    def set_subj_short_name_eng(self, val):
        self.short_name_en.send_keys(val)

    def set_subj_ident_code(self, val):
        self.edrpou.send_keys(val)

    def set_subj_phone(self, val):
        self.phones0.send_keys(val)

    def set_subj_email(self, val):
        self.emails0.send_keys(val)

    def set_state_company(self, v):
        if v == True:
            # self.drv.execute_script("$('#role0').click()")
            #self.role0.click()
            if v == "general":
                self.drv.find_element_by_xpath("//label[@for='customerRoleId1']").click()
            elif v == "special":
                self.drv.find_element_by_xpath("//label[@for='customerRoleId2']").click()
            else:
                print("NOT KNOW customer type")
        else:
            self.role1.click()

    def set_subj_ident_scheme(self, v):
        Select(self.select_scheme_edrpous).select_by_visible_text(v.strip())

    def set_countries(self, v):
        Select(self.select_countries).select_by_visible_text(v)

    def set_addr_region(self, v):
        sleep(1)
        Select(self.drv.find_element_by_id("select_regions")).select_by_visible_text(v.strip())
        Utils.waitFadeIn(self.drv)

    def set_addr_locality(self, v):
        self.drv.find_element_by_xpath("//input[@ng-click='changeModeEnterCity()']").click()
        self.drv.find_element_by_id("cityName").send_keys(v)

    def set_addr_street(self, v):
        self.drv.find_element_by_id("street").send_keys(v)

    def set_addr_post_code(self, v):
        self.drv.find_element_by_id("post_code").send_keys(v)

    def set_bank_name(self, v):
        self.bankName_0.send_keys(v)

    def set_mfo(self, v):
        self.mfo_0.send_keys(v)

    def set_account(self, v):
        self.bankAccount_0.send_keys(v)

    def set_Ownership(self, v):
        Select(self.select_type).select_by_visible_text(v)
        Utils.waitFadeIn(self.drv)

    def set_company_role(self, v):
        if v=="supplier":
            self.role1.click()
        elif v == "owner":
            self.role0.click()

        Utils.waitFadeIn(self.drv)

    def save_company(self):
        self.is_vat.click()
        self.drv.execute_script("$('#checkAgreementPolicy').click()")
        self.save_changes_btn.click()

    def companyForm(self, company):
        try:
            self.set_Ownership(company["Ownership"])
            self.set_company_role(company["company_role"])
            self.set_subj_legal_name(company["subj_legal_name"])
            self.set_subj_legal_name_eng(company["subj_legal_name_eng"])
            self.set_subj_short_name(company["subj_short_name"])
            self.set_subj_short_name_eng(company["subj_short_name_eng"])
            self.set_subj_ident_code(company["subj_ident_code"])
            self.set_subj_phone(company["subj_phone"])
            self.set_subj_email(company["subj_email"])
            self.set_state_company(company["state_company"])
            self.set_subj_ident_scheme(company["subj_ident_scheme"].strip())
            self.set_countries("Україна")
            self.set_addr_region(company["addr_region"].strip())
            self.set_addr_locality(company["addr_locality"])
            self.set_addr_street(company["addr_street"])
            self.set_addr_post_code(company["addr_post_code"])
            self.set_bank_name(company["bank_name"])
            self.set_mfo(company["mfo"])
            self.set_account(company["account"])
            self.save_company()

        except Exception as e:
            print(str(e))











