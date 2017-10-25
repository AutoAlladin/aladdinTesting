import unittest
import sys
from unittest import TestLoader

from Aladdin.Docs import Docs
from Aladdin.Registration.UserRegistrationEDRPOU  import UserRegistrationEDRPOU
from Aladdin.Registration.UserRegistration_FOP  import  UserRegistration_FOP
from Aladdin.Registration.RegistrationCompanyEDRPOU import RegistrationCompany
from Aladdin.Registration.RegistrationCompanyFOP import RegistrationCompanyFop
from Aladdin.Authorization.Login import Login
from Aladdin.Edit.Edit import Edit
from Aladdin.Registration.Employees import Employees
from Aladdin.Authorization.LoginAfterRegistration import LoginAfterRegistrationCompany


import os


def s_user_registration():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(UserRegistrationEDRPOU)
    return suite


def s_user_registration_FOP():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(UserRegistration_FOP)
    return suite

def s_company_fop():
    suite = unittest.TestSuite()

    suite.addTest(RegistrationCompanyFop("test_01_registration_userFOP"))
    suite.addTest(RegistrationCompanyFop("test_02_tax_system"))
    suite.addTest(RegistrationCompanyFop("test_03_phone_company"))
    suite.addTest(RegistrationCompanyFop("test_04_email_company"))
    suite.addTest(RegistrationCompanyFop("test_05_country_legal"))
    suite.addTest(RegistrationCompanyFop("test_06_region_legal"))
    suite.addTest(RegistrationCompanyFop("test_07_city_legal"))
    suite.addTest(RegistrationCompanyFop("test_08_legal_address"))
    suite.addTest(RegistrationCompanyFop("test_09_legal_index"))
    suite.addTest(RegistrationCompanyFop("test_10_real_country"))
    suite.addTest(RegistrationCompanyFop("test_11_real_region"))
    suite.addTest(RegistrationCompanyFop("test_12_real_city"))
    suite.addTest(RegistrationCompanyFop("test_13_real_address"))
    suite.addTest(RegistrationCompanyFop("test_14_real_index"))
    suite.addTest(RegistrationCompanyFop("test_15_bank_name"))
    suite.addTest(RegistrationCompanyFop("test_16_bank_mfo"))
    suite.addTest(RegistrationCompanyFop("test_17_bank_account"))
    suite.addTest(RegistrationCompanyFop("test_18_lead_first_name"))
    suite.addTest(RegistrationCompanyFop("test_19_lead_last_name"))
    suite.addTest(RegistrationCompanyFop("test_20_lead_email"))
    suite.addTest(RegistrationCompanyFop("test_21_lead_phone"))
    suite.addTest(RegistrationCompanyFop("test_22_confidant_first_name"))
    suite.addTest(RegistrationCompanyFop("test_23_confidant_last_name"))
    suite.addTest(RegistrationCompanyFop("test_24_confidant_position"))
    suite.addTest(RegistrationCompanyFop("test_25_confidant_email"))
    suite.addTest(RegistrationCompanyFop("test_26_confidant_phone"))
    suite.addTest(RegistrationCompanyFop("test_27_contract_offer"))
    suite.addTest(RegistrationCompanyFop("test_28_save"))
    return suite

def s_company_reg():
    suite = unittest.TestSuite()

    suite.addTest(RegistrationCompany("test_01_registration_user"))
    suite.addTest(RegistrationCompany("test_02_tax_system"))
    suite.addTest(RegistrationCompany("test_03_phone_company"))
    suite.addTest(RegistrationCompany("test_04_email_company"))
    suite.addTest(RegistrationCompany("test_05_country_legal"))
    suite.addTest(RegistrationCompany("test_06_region_legal"))
    suite.addTest(RegistrationCompany("test_07_city_legal"))
    suite.addTest(RegistrationCompany("test_08_legal_address"))
    suite.addTest(RegistrationCompany("test_09_legal_index"))
    suite.addTest(RegistrationCompany("test_10_real_country"))
    suite.addTest(RegistrationCompany("test_11_real_region"))
    suite.addTest(RegistrationCompany("test_12_real_city"))
    suite.addTest(RegistrationCompany("test_13_real_address"))
    suite.addTest(RegistrationCompany("test_14_real_index"))
    suite.addTest(RegistrationCompany("test_15_bank_name"))
    suite.addTest(RegistrationCompany("test_16_bank_mfo"))
    suite.addTest(RegistrationCompany("test_17_bank_account"))
    suite.addTest(RegistrationCompany("test_18_lead_first_name"))
    suite.addTest(RegistrationCompany("test_19_lead_last_name"))
    suite.addTest(RegistrationCompany("test_20_lead_email"))
    suite.addTest(RegistrationCompany("test_21_lead_phone"))
    suite.addTest(RegistrationCompany("test_22_confidant_first_name"))
    suite.addTest(RegistrationCompany("test_23_confidant_last_name"))
    suite.addTest(RegistrationCompany("test_24_confidant_position"))
    suite.addTest(RegistrationCompany("test_25_confidant_email"))
    suite.addTest(RegistrationCompany("test_26_confidant_phone"))
    suite.addTest(RegistrationCompany("test_27_contract_offer"))
    suite.addTest(RegistrationCompany("test_28_save"))

    return suite

def s_login():
    suite = unittest.TestSuite()

    suite.addTest(Login("test_01_email"))
    suite.addTest(Login("test_02_pswd"))
    suite.addTest(Login("test_03_btn"))

    return suite



def s_edit_information():
    suite = unittest.TestSuite()

    suite.addTest(Edit("test_01_go_to_user_profile"))
    suite.addTest(Edit("test_02_click_tab_company"))
    suite.addTest(Edit("test_03_click_btn_edit"))
    suite.addTest(Edit("test_04_clear_field_comp_name"))
    suite.addTest(Edit("test_05_update_comp_name"))
    suite.addTest(Edit("test_06_ownership_type"))
    suite.addTest(Edit("test_07_company_taxSystem"))
    suite.addTest(Edit("test_08_clear_email"))
    suite.addTest(Edit("test_09_update_email"))
    #suite.addTest(Edit("test_08_select_real_address_city"))
    suite.addTest(Edit("test_10_legal_address_country"))
    suite.addTest(Edit("test_11_clear_field_real_add_str"))
    suite.addTest(Edit("test_12_real_address_street"))
    suite.addTest(Edit("test_13_clear_add_index"))
    suite.addTest(Edit("test_14_real_address_index"))
    suite.addTest(Edit("test_15_clear_comp_bank_acc_mfo"))
    suite.addTest(Edit("test_16_comp_bank_acc_mfo"))
    suite.addTest(Edit("test_17_clear_lead_phone"))
    suite.addTest(Edit("test_18_lead_phone"))
    suite.addTest(Edit("test_19_clear_confidant_first_name"))
    suite.addTest(Edit("test_20_confidant_first_name"))
    suite.addTest(Edit("test_21_clear_confidant_position"))
    suite.addTest(Edit("test_22_confidant_position"))
    suite.addTest(Edit("test_23_contract_offer"))
    suite.addTest(Edit("test_24_click_btn_save_changes"))

    return suite

def s_docs():
    #suite = unittest.defaultTestLoader.loadTestsFromTestCase(Docs)
    suite = unittest.TestSuite()
    suite.addTest(Docs('test_1_Login'))
    suite.addTest(Docs('test_2_User_profile'))
    return suite

def s_Employees():
    suite = unittest.TestSuite()

    suite.addTest(Employees("test_01_go_to_user_profile"))
    suite.addTest(Employees("test_02_tab_empl"))
    suite.addTest(Employees("test_03_add_user"))
    suite.addTest(Employees("test_04_name"))
    suite.addTest(Employees("test_05_name_eu"))
    suite.addTest(Employees("test_06_last_name"))
    suite.addTest(Employees("test_07_last_name_eu"))
    suite.addTest(Employees("test_08_position"))
    suite.addTest(Employees("test_09_email"))
    suite.addTest(Employees("test_10_phone"))
    suite.addTest(Employees("test_11_save"))
    return suite


def s_login_after_full_registration():
    suite = unittest.TestSuite()

    suite.addTest(LoginAfterRegistrationCompany("test_01"))

    return suite


if __name__ == '__main__':
    args=sys.argv[1:]
    runner = unittest.TextTestRunner(verbosity=2)

    if args[0] == 'UserRegistration':
        runner.run(s_user_registration())
    elif args[0] == 'UserRegistration_FOP':
        runner.run(s_user_registration_FOP())
    elif args[0] == 'Login':
        runner.run(s_login())
    elif args[0] == 'UserRegistration_Company':
        runner.run(s_company_reg())
    elif args[0] == 'edit_information':
        runner.run(s_edit_information())
    elif args[0] == 'docs':
        runner.run(s_docs())
    elif args[0] == 'Employees':
        runner.run(s_Employees())
    elif args[0] == 'UserRegistration_Company_Fop':
        runner.run(s_company_fop())
    elif args[0] == 'Login_after_full_registration':
        runner.run(s_login_after_full_registration())