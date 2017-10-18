import unittest
import sys
from Aladdin  import Authorization
from Aladdin import Login
import os


def s_user_registration():
    suite = unittest.TestSuite()

    suite.addTest(Authorization.UserRegistration("test_01_company_name"))
    suite.addTest(Authorization.UserRegistration("test_02_company_name_en"))
    suite.addTest(Authorization.UserRegistration("test_03_check_ownership"))
    suite.addTest(Authorization.UserRegistration("test_04_code_edrpou"))
    suite.addTest(Authorization.UserRegistration("test_05_name"))
    suite.addTest(Authorization.UserRegistration("test_06_name_en"))
    suite.addTest(Authorization.UserRegistration("test_07_last_name"))
    suite.addTest(Authorization.UserRegistration("test_08_last_name_en"))
    suite.addTest(Authorization.UserRegistration("test_09_position"))
    suite.addTest(Authorization.UserRegistration("test_10_phone"))
    suite.addTest(Authorization.UserRegistration("test_11_email"))
    suite.addTest(Authorization.UserRegistration("test_12_password"))
    suite.addTest(Authorization.UserRegistration("test_13_confirm_password"))
    suite.addTest(Authorization.UserRegistration("test_14_click_next_step_btn"))

    return suite


def s_user_registration_FOP():
    suite = unittest.TestSuite()

    suite.addTest(Authorization.UserRegistration("test_01_company_name"))
    suite.addTest(Authorization.UserRegistration("test_02_company_name_en"))
    suite.addTest(Authorization.UserRegistration("test_03_ownership_type_fop"))
    suite.addTest(Authorization.UserRegistration("test_04_code_company"))
    suite.addTest(Authorization.UserRegistration("test_05_name"))
    suite.addTest(Authorization.UserRegistration("test_06_name_en"))
    suite.addTest(Authorization.UserRegistration("test_07_last_name"))
    suite.addTest(Authorization.UserRegistration("test_08_last_name_en"))
    suite.addTest(Authorization.UserRegistration("test_09_position"))
    suite.addTest(Authorization.UserRegistration("test_10_phone"))
    suite.addTest(Authorization.UserRegistration("test_11_email"))
    suite.addTest(Authorization.UserRegistration("test_12_password"))
    suite.addTest(Authorization.UserRegistration("test_13_confirm_password"))
    suite.addTest(Authorization.UserRegistration("test_14_click_next_step_btn"))

    return suite


def s_company_reg():
    suite = unittest.TestSuite()

    suite.addTest(Authorization.UserRegistration_Company("test_02_tax_system"))
    suite.addTest(Authorization.UserRegistration_Company("test_03_phone_company"))
    suite.addTest(Authorization.UserRegistration_Company("test_04_email_company"))
    suite.addTest(Authorization.UserRegistration_Company("test_05_country_legal"))
    suite.addTest(Authorization.UserRegistration_Company("test_06_region_legal"))
    suite.addTest(Authorization.UserRegistration_Company("test_07_city_legal"))
    suite.addTest(Authorization.UserRegistration_Company("test_08_legal_address"))
    suite.addTest(Authorization.UserRegistration_Company("test_09_legal_index"))
    suite.addTest(Authorization.UserRegistration_Company("test_10_real_country"))
    suite.addTest(Authorization.UserRegistration_Company("test_11_real_region"))
    suite.addTest(Authorization.UserRegistration_Company("test_12_real_city"))
    suite.addTest(Authorization.UserRegistration_Company("test_13_real_address"))
    suite.addTest(Authorization.UserRegistration_Company("test_14_real_index"))
    suite.addTest(Authorization.UserRegistration_Company("test_15_bank_name"))
    suite.addTest(Authorization.UserRegistration_Company("test_16_bank_mfo"))
    suite.addTest(Authorization.UserRegistration_Company("test_17_bank_account"))
    suite.addTest(Authorization.UserRegistration_Company("test_18_lead_first_name"))
    suite.addTest(Authorization.UserRegistration_Company("test_19_lead_last_name"))
    suite.addTest(Authorization.UserRegistration_Company("test_20_lead_email"))
    suite.addTest(Authorization.UserRegistration_Company("test_21_lead_phone"))
    suite.addTest(Authorization.UserRegistration_Company("test_22_confidant_first_name"))
    suite.addTest(Authorization.UserRegistration_Company("test_23_confidant_last_name"))
    suite.addTest(Authorization.UserRegistration_Company("test_24_confidant_position"))
    suite.addTest(Authorization.UserRegistration_Company("test_25_confidant_email"))
    suite.addTest(Authorization.UserRegistration_Company("test_26_confidant_phone"))
    suite.addTest(Authorization.UserRegistration_Company("test_27_contract_offer"))
    suite.addTest(Authorization.UserRegistration_Company("test_28_save"))

    return suite

def s_login():
    suite = unittest.TestSuite()

    suite.addTest(Login.Login("test_01_email"))
    suite.addTest(Login.Login("test_02_pswd"))
    suite.addTest(Login.Login("test_03_btn"))

    return suite


if __name__ == '__main__':
    args=sys.argv[1:]
    runner = unittest.TextTestRunner()

    if args[0] == 'UserRegistration':
        runner.run(s_user_registration())

    if args[0] == 'UserRegistration_FOP':
        runner.run(s_user_registration_FOP())

    if args[0] == 'Login':
        runner.run(s_login())

    if args[0] == 'UserRegistration_Company':
        runner.run(s_company_reg())