import unittest
import sys
from copy import deepcopy
from optparse import make_option, OptionParser

import xmlrunner
from bson import ObjectId

from Aladdin.Accounting.AladdinUtils import WebTestSession, AvaliableBrowsers
from Aladdin.Accounting.decorators.StoreTestResult import create_result_DB
from Aladdin.Billing.CreateAccount import *
from BillingMethods.UnitTestByBilling import TestByBilling
from OnPublish.MainPage.load_main_page import Load_main_page, Tender_Tab
from OnPublish.MainPage.login_page import Login_page
from OnPublish.MainPage.registration import Registartion
from OnPublish.Procedures.below import Test_Below
from OnPublish.Procedures.bid import Below_Bid
from billing_UI.Billing import BalanceAfterBid


def s_load_main_page(g, t, cmbro):
    @create_result_DB
    def s_load_main_page_init(bro):
        qa = {"query": { "q": {
                        "name": "load_main_page",
                        "version": "0.0.0.1",
                        "group": g}
                },
              'test_name': t,
              'wts': WebTestSession()
              }
        qa['wts'].set_main_page(qa['query'])
        return qa

    #dbid = 18
    qqq = s_load_main_page_init(cmbro)
    suite = ParamsTestSuite(_params={"result_id": qqq["wts"].result_id, "DB": qqq["wts"].__mongo__})

    suite.suite_params.update({
        "authorization":{
            "owner_login": "aladdin.for.test+owner@gmail.com",
            "owner_password": "zxcvbn00",
            "provider_login":"aladdin.for.test+provider@gmail.com",
            "provider_password":"123123"
        },
        "lang": {
            "ru": {"greeting": "Добро пожаловать на Aladdin Government",
                   "label_for_email": "Электронная почта",
                   "label_for_password": "Пароль",
                   "msg_email": "Ваше уникальное имя пользователя",
                   "msg_password": "Пароль",
                   "remember_me_label": "Запомнить меня?",
                   "remember_me_private": "(если это частный компьютер)",
                   "btnLogin": "Вход",
                   "register": "Регистрация",
                   "restorePass": "Забыли пароль ?"
                   },
            "ua": {"greeting": "Ласкаво просимо до Aladdin Government",
                   "label_for_email": "Електронна пошта",
                   "label_for_password": "Пароль",
                   "msg_email": "Ваше унікальне ім'я користувача",
                   "msg_password": "Пароль",
                   "remember_me_label": "Запам'ятати мене?",
                   "remember_me_private": "(якщо це приватний комп'ютер)",
                   "btnLogin": "Вхід",
                   "register": "Реєстрація",
                   "restorePass": "Забули пароль ?"
                   },
            "en": {"greeting": "Welcome to Aladdin Government",
                   "label_for_email": "E-mail",
                   "label_for_password": "Password",
                   "msg_email": "Your unique username to app",
                   "msg_password": "Password",
                   "remember_me_label": "Remember me?",
                   "remember_me_private": "(if this is a private computer)",
                   "btnLogin": "Login",
                   "register": "Registration",
                   "restorePass": "Forgot password ?"
                   }
        }
    })

    suite.addTest(Load_main_page("page_loaded", _params=qqq ))
    suite.addTest(Load_main_page("menu_presented", _params=qqq))
    suite.addTest(Load_main_page("set_lang", _params=qqq))

    suite.addTest(Tender_Tab("tab_visible", _params=qqq))
    suite.addTest(Tender_Tab("tab_list", _params=qqq))
    suite.addTest(Tender_Tab("tab_search", _params=qqq))
    suite.addTest(Tender_Tab("tab_filters", _params=qqq))

    suite.addTest(Login_page("login_menu", _params=qqq))
    suite.addTest(Login_page("open_login", _params=qqq))
    suite.addTest(Login_page("check_lang", _params=qqq))
    suite.addTest(Login_page("login_owner", _params=qqq))
    suite.addTest(Login_page("login_provider", _params=qqq))

    suite.addTest(Login_page("open_register_form", _params=qqq))
    suite.addTest(Login_page("open_restore_password", _params=qqq))


    return suite

def s_run_bil(g, t, cmbro):
    @create_result_DB
    def s_load_main_page_init(bro):
        qa = {"query": { "q": {
                        "name": "run_bil",
                        "version": "0.0.0.1",
                        "group": g}
                },
              'test_name': t,
              'wts': WebTestSession()
              }
        qa['wts'].set_main_page(qa['query'])
        return qa

    #dbid = 19
    qqq = s_load_main_page_init(cmbro)

    file_name = os.path.dirname(os.path.abspath(__file__)) + '\\..\\Prozorro\\test_params.json'
    with open(file_name, 'r', encoding="UTF-8") as test_params_file:
        dic_params = json.load(test_params_file)

    suite = ParamsTestSuite(_params={"result_id": qqq["wts"].result_id,
                                     "DB": qqq["wts"].__mongo__,
                                     "dic_params":dic_params["billing_ui"]
                                     })
    suite.addTest(BalanceAfterBid("create_below", _params=qqq, _parent_suite=suite))



    return suite

def s_billing_metods(g, t, cmbro):


    @create_result_DB
    def s_load_main_page_init(bro):
        qa = {"query": { "q": {
                        "name": "billing_metods",
                        "version": "0.0.0.1",
                        "group": g}
                },
                'test_name': t,
                'wts': WebTestSession(useBrowser=False),
                "siteType": '1'
              }

        return qa

    #dbid = 18
    qqq = s_load_main_page_init(cmbro)

    par = qqq["wts"].__mongo__.get_params(24)["par"]
    # tenderId = par["tenderId"]
    # tenderId += 1
    # par["tenderId"] = tenderId

    tenderId_04 = par["test_04"]["tenderId"]
    tenderId_04 += 1
    par["tenderId"] = tenderId_04


    qqq["wts"].__mongo__.\
        test_params.\
        update_one({"_id": 24},
                   {"$set": {"par.test_04.tenderId": tenderId_04}})



    tenderId_07 = par["test_07"]["tenderId"]
    tenderId_07 += 1
    par["tenderId"] = tenderId_07

    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"par.test_07.tenderId": tenderId_07}})
    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"par.test_07_1.tenderId": tenderId_07}})



    tenderId_09 = par["test_09_1"]["tenderId"]
    tenderId_09 += 1
    par["tenderId"] = tenderId_09

    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"par.test_09_1.tenderId": tenderId_09}})



    tenderId_10 = par["test_10_1"]["tenderId"]
    tenderId_10 +=1
    par["tenderId"] = tenderId_10

    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"par.test_10_1.tenderId": tenderId_10}})



    tenderId_18 = par["test_18_1"]["tenderId"]
    tenderId_18 += 1
    par["tenderId"] = tenderId_18

    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"par.test_18.tenderId": tenderId_18}})
    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"par.test_18_1.tenderId": tenderId_18}})





    suite = ParamsTestSuite(
                _params={"result_id": qqq["wts"].result_id,
                         "DB": qqq["wts"].__mongo__,
                         "par":par
                         }
    )

    suite.addTest(TestByBilling("test_01_get_balance_positive", _params=qqq))
    suite.addTest(TestByBilling("test_02_get_balance_acc_negative", _params=qqq))
    suite.addTest(TestByBilling("test_03_get_balance_without_guid_negative", _params=qqq))
    suite.addTest(TestByBilling("test_04_reserve_balance_positive", _params=qqq))
    suite.addTest(TestByBilling("test_05_reserve_balance_tender_id_is_null_negative", _params=qqq))
    suite.addTest(TestByBilling("test_06_reserve_balance_total_money_is_zero_positive", _params=qqq))
    suite.addTest(TestByBilling("test_07_return_monies_positive", _params=qqq))
    suite.addTest(TestByBilling("test_08_return_monies_without_reserve_negative", _params=qqq))
    suite.addTest(TestByBilling("test_09_return_monies_tender_is_null_negative", _params=qqq))
    suite.addTest(TestByBilling("test_10_return_monies_error_negative", _params=qqq))
    suite.addTest(TestByBilling("test_11_return_monies_by_company_uuid_positive", _params=qqq))
    suite.addTest(TestByBilling("test_12_return_monies_by_company_uuid_tender_is_null_negative", _params=qqq))
    suite.addTest(TestByBilling("test_13_return_monies_by_company_uuid_error_negative", _params=qqq))
    suite.addTest(TestByBilling("test_14_write_off_money_positive", _params=qqq))
    suite.addTest(TestByBilling("test_15_write_off_money_tender_is_null_negative", _params=qqq))
    suite.addTest(TestByBilling("test_16_write_off_money_site_type_not_found_negative", _params=qqq))
    suite.addTest(TestByBilling("test_17_write_off_money_error_negative", _params=qqq))
    suite.addTest(TestByBilling("test_18_cancel_reserve_money_positive", _params=qqq))
    suite.addTest(TestByBilling("test_19_cancel_reserve_money_tender_id_is_null_negative", _params=qqq))
    suite.addTest(TestByBilling("test_20_cancel_reserve_money_error_negative", _params=qqq))

    qqq2={"query": { "q": {
                        "name": "billing_metods",
                        "version": "0.0.0.1",
                        "group": g}
                },
                'test_name': t,
                'wts': WebTestSession(useBrowser=False),
                "siteType": '2'
              }

    suite.addTest(TestByBilling("test_04_reserve_balance_positive", _params=qqq2))
    suite.addTest(TestByBilling("test_05_reserve_balance_tender_id_is_null_negative", _params=qqq2))
    suite.addTest(TestByBilling("test_06_reserve_balance_total_money_is_zero_positive", _params=qqq2))
    suite.addTest(TestByBilling("test_07_return_monies_positive", _params=qqq2))
    suite.addTest(TestByBilling("test_08_return_monies_without_reserve_negative", _params=qqq2))
    suite.addTest(TestByBilling("test_09_return_monies_tender_is_null_negative", _params=qqq2))
    suite.addTest(TestByBilling("test_10_return_monies_error_negative", _params=qqq2))
    suite.addTest(TestByBilling("test_11_return_monies_by_company_uuid_positive", _params=qqq2))
    suite.addTest(TestByBilling("test_12_return_monies_by_company_uuid_tender_is_null_negative", _params=qqq2))
    suite.addTest(TestByBilling("test_13_return_monies_by_company_uuid_error_negative", _params=qqq2))
    suite.addTest(TestByBilling("test_14_write_off_money_positive", _params=qqq2))
    suite.addTest(TestByBilling("test_15_write_off_money_tender_is_null_negative", _params=qqq2))
    suite.addTest(TestByBilling("test_16_write_off_money_site_type_not_found_negative", _params=qqq2))
    suite.addTest(TestByBilling("test_17_write_off_money_error_negative", _params=qqq2))
    suite.addTest(TestByBilling("test_18_cancel_reserve_money_positive", _params=qqq2))
    suite.addTest(TestByBilling("test_19_cancel_reserve_money_tender_id_is_null_negative", _params=qqq2))
    suite.addTest(TestByBilling("test_20_cancel_reserve_money_error_negative", _params=qqq2))


    qqq3={"query": { "q": {
                        "name": "billing_metods",
                        "version": "0.0.0.1",
                        "group": g}
                },
                'test_name': t,
                'wts': WebTestSession(useBrowser=False),
                "siteType": '2'
              }

    suite.addTest(TestByBilling("test_14_write_off_money_positive", _params=qqq3))
    suite.addTest(TestByBilling("test_15_write_off_money_tender_is_null_negative", _params=qqq3))
    suite.addTest(TestByBilling("test_16_write_off_money_site_type_not_found_negative", _params=qqq3))
    suite.addTest(TestByBilling("test_17_write_off_money_error_negative", _params=qqq3))


    return suite

def s_publish_test(g, t, cmbro):
    @create_result_DB
    def s_publish_test_init(bro):
        qa = {"query": { "q": {
                        "name": "publish_app",
                        "version": "0.0.0.1",
                        "group": g}
                },
              'test_name': t,
              'wts': WebTestSession(),
              'siteType': '1'
              }
        qa['wts'].set_main_page(qa['query'])
        return qa

    #dbid = 20
    qqq = s_publish_test_init(cmbro)

    suite = ParamsTestSuite(_params={
                "result_id": qqq["wts"].result_id,
                "DB": qqq["wts"].__mongo__,
                "tender_json": qqq["wts"].__mongo__.get_params(21),
                "registartion_data": qqq["wts"].__mongo__.get_params(23)


    })


    # suite.addTest(TestByBilling("test_01_get_balance_positive", _params=qqq))
    # suite.addTest(TestByBilling("test_02_get_balance_acc_negative", _params=qqq))
    # suite.addTest(TestByBilling("test_03_get_balance_without_guid_negative", _params=qqq))
    # suite.addTest(TestByBilling("test_04_reserve_balance_positive", _params=qqq))
    # suite.addTest(TestByBilling("test_05_reserve_balance_tender_id_is_null_negative", _params=qqq))
    # suite.addTest(TestByBilling("test_06_reserve_balance_total_money_is_zero_positive", _params=qqq))
    # suite.addTest(TestByBilling("test_07_return_monies_positive", _params=qqq))
    # suite.addTest(TestByBilling("test_08_return_monies_without_reserve_negative", _params=qqq))
    # suite.addTest(TestByBilling("test_09_return_monies_tender_is_null_negative", _params=qqq))
    # suite.addTest(TestByBilling("test_10_return_monies_error_negative", _params=qqq))
    # suite.addTest(TestByBilling("test_11_return_monies_by_company_uuid_positive", _params=qqq))
    # suite.addTest(TestByBilling("test_12_return_monies_by_company_uuid_tender_is_null_negative", _params=qqq))
    # suite.addTest(TestByBilling("test_13_return_monies_by_company_uuid_error_negative", _params=qqq))
    # suite.addTest(TestByBilling("test_14_write_off_money_positive", _params=qqq))
    # suite.addTest(TestByBilling("test_15_write_off_money_tender_is_null_negative", _params=qqq))
    # suite.addTest(TestByBilling("test_16_write_off_money_site_type_not_found_negative", _params=qqq))
    # suite.addTest(TestByBilling("test_17_write_off_money_error_negative", _params=qqq))
    # suite.addTest(TestByBilling("test_18_cancel_reserve_money_positive", _params=qqq))
    # suite.addTest(TestByBilling("test_19_cancel_reserve_money_tender_id_is_null_negative", _params=qqq))
    # suite.addTest(TestByBilling("test_20_cancel_reserve_money_error_negative", _params=qqq))
    #
    # qqq2 = {"query": {"q": {
    #     "name": "billing_metods",
    #     "version": "0.0.0.1",
    #     "group": g}
    # },
    #     'test_name': t,
    #     'wts': WebTestSession(useBrowser=False),
    #     "siteType": '2'
    # }
    #
    # suite.addTest(TestByBilling("test_04_reserve_balance_positive", _params=qqq2))
    # suite.addTest(TestByBilling("test_05_reserve_balance_tender_id_is_null_negative", _params=qqq2))
    # suite.addTest(TestByBilling("test_06_reserve_balance_total_money_is_zero_positive", _params=qqq2))
    # suite.addTest(TestByBilling("test_07_return_monies_positive", _params=qqq2))
    # suite.addTest(TestByBilling("test_08_return_monies_without_reserve_negative", _params=qqq2))
    # suite.addTest(TestByBilling("test_09_return_monies_tender_is_null_negative", _params=qqq2))
    # suite.addTest(TestByBilling("test_10_return_monies_error_negative", _params=qqq2))
    # suite.addTest(TestByBilling("test_11_return_monies_by_company_uuid_positive", _params=qqq2))
    # suite.addTest(TestByBilling("test_12_return_monies_by_company_uuid_tender_is_null_negative", _params=qqq2))
    # suite.addTest(TestByBilling("test_13_return_monies_by_company_uuid_error_negative", _params=qqq2))
    # suite.addTest(TestByBilling("test_14_write_off_money_positive", _params=qqq2))
    # suite.addTest(TestByBilling("test_15_write_off_money_tender_is_null_negative", _params=qqq2))
    # suite.addTest(TestByBilling("test_16_write_off_money_site_type_not_found_negative", _params=qqq2))
    # suite.addTest(TestByBilling("test_17_write_off_money_error_negative", _params=qqq2))
    # suite.addTest(TestByBilling("test_18_cancel_reserve_money_positive", _params=qqq2))
    # suite.addTest(TestByBilling("test_19_cancel_reserve_money_tender_id_is_null_negative", _params=qqq2))
    # suite.addTest(TestByBilling("test_20_cancel_reserve_money_error_negative", _params=qqq2))
    #
    # qqq3 = {"query": {"q": {
    #     "name": "billing_metods",
    #     "version": "0.0.0.1",
    #     "group": g}
    # },
    #     'test_name': t,
    #     'wts': WebTestSession(useBrowser=False),
    #     "siteType": '2'
    # }
    #
    # suite.addTest(TestByBilling("test_14_write_off_money_positive", _params=qqq3))
    # suite.addTest(TestByBilling("test_15_write_off_money_tender_is_null_negative", _params=qqq3))
    # suite.addTest(TestByBilling("test_16_write_off_money_site_type_not_found_negative", _params=qqq3))
    # suite.addTest(TestByBilling("test_17_write_off_money_error_negative", _params=qqq3))


    # suite.addTest(Load_main_page("page_loaded", _params=qqq ))
    # suite.addTest(Load_main_page("menu_presented", _params=qqq))
    # suite.addTest(Load_main_page("set_lang", _params=qqq))
    #
    # suite.addTest(Tender_Tab("tab_visible", _params=qqq))
    # suite.addTest(Tender_Tab("tab_list", _params=qqq))
    # suite.addTest(Tender_Tab("tab_search", _params=qqq))
    # suite.addTest(Tender_Tab("tab_filters", _params=qqq))
    #
    # suite.addTest(Login_page("login_menu", _params=qqq))
    # suite.addTest(Login_page("open_login", _params=qqq))
    # suite.addTest(Login_page("check_lang", _params=qqq))
    # suite.addTest(Login_page("login_owner", _params=qqq))
    # suite.addTest(Login_page("login_provider", _params=qqq))
    #
    # suite.addTest(Login_page("open_register_form", _params=qqq))
    # suite.addTest(Login_page("open_restore_password", _params=qqq))
    #
    # suite.addTest(Test_Below("create_menu", _params=qqq))
    # suite.addTest(Test_Below("select_below_menu", _params=qqq))
    # suite.addTest(Test_Below("set_description", _params=qqq))
    # suite.addTest(Test_Below("set_curr", _params=qqq))
    # suite.addTest(Test_Below("set_multilot", _params=qqq))
    # suite.addTest(Test_Below("set_dates", _params=qqq))
    # suite.addTest(Test_Below("add_lot", _params=qqq))
    # suite.addTest(Test_Below("add_item", _params=qqq))
    # suite.addTest(Test_Below("add_features", _params=qqq))
    # suite.addTest(Test_Below("add_doc", _params=qqq))
    # suite.addTest(Test_Below("open_draft_by_url", _params=qqq))
    # suite.addTest(Test_Below("open_draft_by_url_edit", _params=qqq))
    # suite.addTest(Test_Below("open_draft_by_url_delete", _params=qqq))
    # suite.addTest(Test_Below("create_below_publish", _params=qqq))
    #
    # suite.addTest(Below_Bid("login_provider", _params=qqq))
    # suite.addTest(Below_Bid("select_below_type", _params=qqq))
    # suite.addTest(Below_Bid("select_tender_period", _params=qqq))
    # suite.addTest(Below_Bid("find_tender_for_bid", _params=qqq))
    # suite.addTest(Below_Bid("wait_for_tender_period", _params=qqq))
    # suite.addTest(Below_Bid("add_bid", _params=qqq))

    suite.addTest(Registartion("try_login", _params=qqq))
    suite.addTest(Registartion("open_register_form", _params=qqq))

    return suite

def runner(arg):
    parser = OptionParser()
    parser.add_option("-s", action="store", type="string")
    parser.add_option("-g", action="store", type="string")
    parser.add_option("-b", action="store", type="string")
    parser.add_option("--name", action="store", type="string")

    (options, args) = parser.parse_args(arg)

    # runner = unittest.TextTestRunner(verbosity=2)
    runner = xmlrunner.XMLTestRunner(output='test-reports',
                                     verbosity=2)
    opt = options.s
    bro = options.b
    tname =options.name
    if tname is None: tname=opt + " test development "+datetime.datetime.now().isoformat()

    if bro == "ch":
        bro = AvaliableBrowsers.Chrome
    elif bro == "f":
        bro = AvaliableBrowsers.Firefox
    else:
        bro = AvaliableBrowsers.Chrome

    ttt = None

    if opt == 'main_page':
        ttt = s_load_main_page(options.g, tname, bro)
    elif opt =='run_bil':
        ttt = s_run_bil(options.g,  # test group from D
                        tname,  # test name for report
                        bro)    # browser? default - Chrome
    elif opt == 'billing_metods':
        ttt = s_billing_metods(options.g,tname,  bro)
    elif opt == 'publish_test':
        ttt = s_publish_test(options.g,tname,  bro)


    if ttt is not None:
        try:
            runner.run(ttt)
        except:
            ttt.suite_params["DB"].test_result.update(
                {"_id": ttt.suite_params["result_id"]},
                {"$set": {"test_result": "FAILED"}})
        finally:
            if "DB" in ttt.suite_params:
                ttt.suite_params["DB"].test_result.update(
                    {"_id": ttt.suite_params["result_id"]},
                    {"$set": {"test_result": "PASSED"}})




if __name__ =='__main__':
    runner(None)
