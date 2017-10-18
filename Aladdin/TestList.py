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