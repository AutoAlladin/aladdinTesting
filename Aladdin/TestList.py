import unittest
import sys
from Aladdin  import Authorization
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


def edit_information():
    suite = unittest.TestSuite()

    suite.addTest(Authorization.UserRegistration("test_01_company_name"))

if __name__ == '__main__':
    args=sys.argv[1:]
    runner = unittest.TextTestRunner()

    if args[0] == 'UserRegistration':
        runner.run(s_user_registration())

