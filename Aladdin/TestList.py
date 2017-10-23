import unittest
import sys
from unittest import TestLoader

from Aladdin.Docs import Docs
from Aladdin.Registration.UserRegistrationEDRPOU  import UserRegistrationEDRPOU
from Aladdin.Registration.UserRegistration_FOP  import UserRegistration_FOP
from Aladdin.Registration.RegistrationCompany import RegistrationCompany
from Aladdin.Authorization.Login import Login

import os


def s_user_registration():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(UserRegistrationEDRPOU)
    return suite


def s_user_registration_FOP():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(UserRegistration_FOP)
    return suite


def s_company_reg():
    suite = unittest.TestSuite()

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

    suite.addTest(Login.Login("test_01_email"))
    suite.addTest(Login.Login("test_02_pswd"))
    suite.addTest(Login.Login("test_03_btn"))

    return suite



def s_edit_information():
    suite = unittest.TestSuite()

    suite.addTest(Login.Login("test_01_email"))
    suite.addTest(Login.Login("test_02_pswd"))
    suite.addTest(Login.Login("test_03_btn"))
    suite.addTest(Login.EditInfo("test_01_go_to_user_profile"))
    suite.addTest(Login.EditInfo("test_02_click_tab_company"))
    suite.addTest(Login.EditInfo("test_03_ownership_tax"))
    suite.addTest(Login.EditInfo("test_04_click_btn_edit"))
    suite.addTest(Login.EditInfo("test_05_update_comp_name"))
    suite.addTest(Login.EditInfo("test_06_contract_offer"))
    suite.addTest(Login.EditInfo("test_07_click_btn_save_changes"))

    return suite

def s_docs():
    #suite = unittest.defaultTestLoader.loadTestsFromTestCase(Docs)
    suite = unittest.TestSuite()
    suite.addTest(Docs('test_1_Login'))
    suite.addTest(Docs('test_2_User_profile'))
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