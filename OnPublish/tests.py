import unittest
import sys
from copy import deepcopy
from optparse import make_option, OptionParser

import xmlrunner
from bson import ObjectId

from Aladdin.Accounting.AladdinUtils import WebTestSession, AvaliableBrowsers
from Aladdin.Accounting.Authorization.LoginAfterRegistration import LoginAfterRegistrationCompany
from Aladdin.Accounting.decorators.StoreTestResult import create_result_DB
from Aladdin.Billing.CreateAccount import *
from BillingMethods.UnitTestByBilling import TestByBilling
from BillingMethods.aladdin_like_prozzoro import TestAladdinLikeProzorro
from BillingMethods.prozorro import TestProzorro
from BillingMethods.aladdin_pure import TestAladdinPure
from OnPublish.MainPage.load_main_page import Load_main_page, Tender_Tab
from OnPublish.MainPage.login_page import Login_page
from OnPublish.MainPage.registration import Registartion
from OnPublish.Procedures.below import Test_Below
from OnPublish.Procedures.bid import Below_Bid
from OnPublish.Procedures.qualification import Qualification
from OnPublish.rialto_tests import s_rialto_publish_prod
from billing_UI.Billing import BalanceAfterBid


def s_aladdin_like_prozorro(pure_json, t, cmbro):
    @create_result_DB
    def s_aladdin_like_prozorro_init(bro):
        qa = {"query": { "q": {
                        "name": "aladdin_like_prozorro",
                        "version": "0.0.0.1",
                        "group": 'pure_json'}
                },
              'test_name': t,
              'wts': WebTestSession(useBrowser=False),
              'auction_par.json': qqq["wts"].__mongo__.get_params(25)["auction_par.json"]
              }
        return qa

    #dbid = 19
    qqq = s_aladdin_like_prozorro_init(cmbro)

    par = qqq["auction_par.json"]
    suite = ParamsTestSuite(_params={"result_id": qqq["wts"].result_id,
                                     "DB": qqq["wts"].__mongo__                                
                                     })

    pre_par_alddin_like_prozorro(par, qqq["wts"].__mongo__.test_params )
    atos_aladin_like_prozorro(qqq, suite)

    return suite
def atos_aladin_like_prozorro(qqq, suite):
    suite.addTest(TestAladdinLikeProzorro("test_01_get_balance_positive", _params=qqq))
    suite.addTest(TestAladdinLikeProzorro("test_02_get_balance_acc_negative", _params=qqq))
    suite.addTest(TestAladdinLikeProzorro("test_03_get_balance_without_guid_negative", _params=qqq))
    suite.addTest(TestAladdinLikeProzorro("test_04_reserve_balance_positive", _params=qqq))
    suite.addTest(TestAladdinLikeProzorro("test_05_reserve_balance_tender_id_is_null_negative", _params=qqq))
    suite.addTest(TestAladdinLikeProzorro("test_06_reserve_balance_total_money_is_zero_positive", _params=qqq))
    suite.addTest(TestAladdinLikeProzorro("test_07_return_monies_positive", _params=qqq))
    suite.addTest(TestAladdinLikeProzorro("test_08_return_monies_without_reserve_negative", _params=qqq))
    suite.addTest(TestAladdinLikeProzorro("test_09_return_monies_tender_is_null_negative", _params=qqq))
    suite.addTest(TestAladdinLikeProzorro("test_10_return_monies_error_negative", _params=qqq))
    suite.addTest(TestAladdinLikeProzorro("test_11_return_monies_by_company_uuid_positive", _params=qqq))
    suite.addTest(TestAladdinLikeProzorro("test_12_return_monies_by_company_uuid_tender_is_null_negative", _params=qqq))
    suite.addTest(TestAladdinLikeProzorro("test_13_return_monies_by_company_uuid_error_negative", _params=qqq))
    suite.addTest(TestAladdinLikeProzorro("test_14_write_off_money_positive", _params=qqq))
    suite.addTest(TestAladdinLikeProzorro("test_15_write_off_money_tender_is_null_negative", _params=qqq))
    suite.addTest(TestAladdinLikeProzorro("test_16_write_off_money_site_type_not_found_negative", _params=qqq))
    suite.addTest(TestAladdinLikeProzorro("test_17_write_off_money_error_negative", _params=qqq))
    suite.addTest(TestAladdinLikeProzorro("test_18_cancel_reserve_money_positive", _params=qqq))
    suite.addTest(TestAladdinLikeProzorro("test_19_cancel_reserve_money_tender_id_is_null_negative", _params=qqq))
    suite.addTest(TestAladdinLikeProzorro("test_20_cancel_reserve_money_error_negative", _params=qqq))
    # suite.addTest(TestByBilling("test_21_reserve_balance_positive_sitetype_2_suite_2", _params=qqq))
    # suite.addTest(TestByBilling("test_22_reserve_balance_tender_id_is_null_negative_sitetype_2_suite_2", _params=qqq))
    # suite.addTest(TestByBilling("test_23_reserve_balance_total_money_is_zero_positive_sitetype_2_suite_2", _params=qqq))
    # suite.addTest(TestByBilling("test_24_return_monies_positive_sitetype_2_suite_2", _params=qqq))
    # suite.addTest(TestByBilling("test_25_return_monies_without_reserve_negative_sitetype_2_suite_2", _params=qqq))
    # suite.addTest(TestByBilling("test_26_return_monies_tender_is_null_negative_sitetype_2_suite_2", _params=qqq))
    # suite.addTest(TestByBilling("test_27_return_monies_error_negative_sitetype_2_suite_2", _params=qqq))
def pre_par_alddin_like_prozorro(par, db_test_params):
    tenderId_04 = par["test_04"]["tenderId"]
    tenderId_04 += 1
    par["tenderId"] = tenderId_04
    db_test_params.update_one({"_id": 25}, {"$set": {"auction_par.json.test_04.tenderId": tenderId_04}})
    tenderId_06 = par["test_06"]["tenderId"]
    tenderId_06 += 1
    par["tenderId"] = tenderId_06
    db_test_params.update_one({"_id": 25}, {"$set": {"auction_par.json.test_06.tenderId": tenderId_06}})
    tenderId_07 = par["test_07"]["tenderId"]
    tenderId_07 += 1
    par["tenderId"] = tenderId_07
    db_test_params.update_one({"_id": 25}, {"$set": {"auction_par.json.test_07.tenderId": tenderId_07}})
    db_test_params.update_one({"_id": 25}, {"$set": {"auction_par.json.test_07_1.tenderId": tenderId_07}})
    tenderId_08 = par["test_08"]["tenderId"]
    tenderId_08 += 1
    par["tenderId"] = tenderId_08
    db_test_params.update_one({"_id": 25}, {"$set": {"auction_par.json.test_08.tenderId": tenderId_08}})
    tenderId_09 = par["test_09_1"]["tenderId"]
    tenderId_09 += 1
    par["tenderId"] = tenderId_09
    db_test_params.update_one({"_id": 25}, {"$set": {"auction_par.json.test_09_1.tenderId": tenderId_09}})
    tenderId_10 = par["test_10_1"]["tenderId"]
    tenderId_10 += 1
    par["tenderId"] = tenderId_10
    db_test_params.update_one({"_id": 25}, {"$set": {"auction_par.json.test_10_1.tenderId": tenderId_10}})
    tenderId_11 = par["test_11"]["tenderId"]
    tenderId_11 += 1
    par["tenderId"] = tenderId_11
    db_test_params.update_one({"_id": 25}, {"$set": {"auction_par.json.test_11.tenderId": tenderId_11}})
    db_test_params.update_one({"_id": 25}, {"$set": {"auction_par.json.test_11_1.tenderId": tenderId_11}})
    db_test_params.update_one({"_id": 25}, {"$set": {"auction_par.json.test_11_2.tenderId": tenderId_11}})
    tenderId_12 = par["test_12_1"]["tenderId"]
    tenderId_12 += 1
    par["tenderId"] = tenderId_12
    db_test_params.update_one({"_id": 25}, {"$set": {"auction_par.json.test_12_1.tenderId": tenderId_12}})
    tenderId_14 = par["test_14_1"]["tenderId"]
    tenderId_14 += 1
    par["tenderId"] = tenderId_14
    db_test_params.update_one({"_id": 25}, {"$set": {"auction_par.json.test_14.tenderId": tenderId_14}})
    db_test_params.update_one({"_id": 25}, {"$set": {"auction_par.json.test_14_1.tenderId": tenderId_14}})
    tenderId_15 = par["test_15_1"]["tenderId"]
    tenderId_15 += 1
    par["tenderId"] = tenderId_15
    db_test_params.update_one({"_id": 25}, {"$set": {"auction_par.json.test_15_1.tenderId": tenderId_15}})
    tenderId_16 = par["test_16_1"]["tenderId"]
    tenderId_16 += 1
    par["tenderId"] = tenderId_16
    db_test_params.update_one({"_id": 25}, {"$set": {"auction_par.json.test_16_1.tenderId": tenderId_16}})
    db_test_params.update_one({"_id": 26}, {"$set": {"auction_par.json.test_16.tenderId": tenderId_16}})
    tenderId_17 = par["test_17_1"]["tenderId"]
    tenderId_17 += 1
    par["tenderId"] = tenderId_17
    db_test_params.update_one({"_id": 25}, {"$set": {"auction_par.json.test_17_1.tenderId": tenderId_17}})
    tenderId_18 = par["test_18_1"]["tenderId"]
    tenderId_18 += 1
    par["tenderId"] = tenderId_18
    db_test_params.update_one({"_id": 25}, {"$set": {"auction_par.json.test_18.tenderId": tenderId_18}})
    db_test_params.update_one({"_id": 25}, {"$set": {"auction_par.json.test_18_1.tenderId": tenderId_18}})
    tenderId_19_1 = par["test_19_1"]["tenderId"]
    tenderId_19_1 += 1
    par["tenderId"] = tenderId_19_1
    db_test_params.update_one({"_id": 25}, {"$set": {"auction_par.json.test_19_1.tenderId": tenderId_19_1}})
    tenderId_20_1 = par["test_20_1"]["tenderId"]
    tenderId_20_1 += 1
    par["tenderId"] = tenderId_20_1
    db_test_params.update_one({"_id": 25}, {"$set": {"auction_par.json.test_20_1.tenderId": tenderId_20_1}})

def s_prozorro(pure_json, t, cmbro):
    @create_result_DB
    def s_prozorro_init(bro):
        qa = {"query": { "q": {
                        "name": "prozorro",
                        "version": "0.0.0.1",
                        "group": 'pure_json'}
                },
              'test_name': t,
              'wts': WebTestSession(useBrowser=False),
              "auction_par.json": qqq["wts"].__mongo__.get_params(27)["auction_par.json"]
              }
        return qa

    qqq = s_prozorro_init(cmbro)

    par = qqq["auction_par.json"]
    suite = ParamsTestSuite(_params={"result_id": qqq["wts"].result_id,
                                     "DB": qqq["wts"].__mongo__
                                     })

    pre_par_prozorro(par, qqq["wts"].__mongo__.test_params)
    atos_prozorro(qqq, suite)

    return suite
def atos_prozorro(qqq, suite):
    suite.addTest(TestProzorro("test_01_get_balance_positive", _params=qqq))
    suite.addTest(TestProzorro("test_02_get_balance_acc_negative", _params=qqq))
    suite.addTest(TestProzorro("test_03_get_balance_without_guid_negative", _params=qqq))
    suite.addTest(TestProzorro("test_04_reserve_balance_positive", _params=qqq))
    suite.addTest(TestProzorro("test_05_reserve_balance_tender_id_is_null_negative", _params=qqq))
    suite.addTest(TestProzorro("test_06_reserve_balance_total_money_is_zero_positive", _params=qqq))
    suite.addTest(TestProzorro("test_07_return_monies_positive", _params=qqq))
    suite.addTest(TestProzorro("test_08_return_monies_without_reserve_negative", _params=qqq))
    suite.addTest(TestProzorro("test_09_return_monies_tender_is_null_negative", _params=qqq))
    suite.addTest(TestProzorro("test_10_return_monies_error_negative", _params=qqq))
    suite.addTest(TestProzorro("test_11_return_monies_by_company_uuid_positive", _params=qqq))
    suite.addTest(TestProzorro("test_12_return_monies_by_company_uuid_tender_is_null_negative", _params=qqq))
    suite.addTest(TestProzorro("test_13_return_monies_by_company_uuid_error_negative", _params=qqq))
    suite.addTest(TestProzorro("test_14_write_off_money_positive", _params=qqq))
    suite.addTest(TestProzorro("test_15_write_off_money_tender_is_null_negative", _params=qqq))
    suite.addTest(TestProzorro("test_16_write_off_money_site_type_not_found_negative", _params=qqq))
    suite.addTest(TestProzorro("test_17_write_off_money_error_negative", _params=qqq))
    suite.addTest(TestProzorro("test_18_cancel_reserve_money_positive", _params=qqq))
    suite.addTest(TestProzorro("test_19_cancel_reserve_money_tender_id_is_null_negative", _params=qqq))
    suite.addTest(TestProzorro("test_20_cancel_reserve_money_error_negative", _params=qqq))
def pre_par_prozorro(par, db_test_params):
    tenderId_04 = par["test_04"]["tenderId"]
    tenderId_04 += 1
    par["tenderId"] = tenderId_04
    db_test_params.update_one({"_id": 27}, {"$set": {"auction_par.json.test_04.tenderId": tenderId_04}})
    tenderId_06 = par["test_06"]["tenderId"]
    tenderId_06 += 1
    par["tenderId"] = tenderId_06
    db_test_params.update_one({"_id": 27}, {"$set": {"auction_par.json.test_06.tenderId": tenderId_06}})
    tenderId_07 = par["test_07"]["tenderId"]
    tenderId_07 += 1
    par["tenderId"] = tenderId_07
    db_test_params.update_one({"_id": 27}, {"$set": {"auction_par.json.test_07.tenderId": tenderId_07}})
    db_test_params.update_one({"_id": 27}, {"$set": {"auction_par.json.test_07_1.tenderId": tenderId_07}})
    tenderId_08 = par["test_08"]["tenderId"]
    tenderId_08 += 1
    par["tenderId"] = tenderId_08
    db_test_params.update_one({"_id": 27}, {"$set": {"auction_par.json.test_08.tenderId": tenderId_08}})
    tenderId_09 = par["test_09_1"]["tenderId"]
    tenderId_09 += 1
    par["tenderId"] = tenderId_09
    db_test_params.update_one({"_id": 27}, {"$set": {"auction_par.json.test_09_1.tenderId": tenderId_09}})
    tenderId_10 = par["test_10_1"]["tenderId"]
    tenderId_10 += 1
    par["tenderId"] = tenderId_10
    db_test_params.update_one({"_id": 27}, {"$set": {"auction_par.json.test_10_1.tenderId": tenderId_10}})
    tenderId_11 = par["test_11"]["tenderId"]
    tenderId_11 += 1
    par["tenderId"] = tenderId_11
    db_test_params.update_one({"_id": 27}, {"$set": {"auction_par.json.test_11.tenderId": tenderId_11}})
    db_test_params.update_one({"_id": 27}, {"$set": {"auction_par.json.test_11_1.tenderId": tenderId_11}})
    db_test_params.update_one({"_id": 27}, {"$set": {"auction_par.json.test_11_2.tenderId": tenderId_11}})
    tenderId_12 = par["test_12"]["tenderId"]
    tenderId_12 += 1
    par["tenderId"] = tenderId_12
    db_test_params.update_one({"_id": 27}, {"$set": {"auction_par.json.test_12_1.tenderId": tenderId_12}})
    tenderId_14 = par["test_14_1"]["tenderId"]
    tenderId_14 += 1
    par["tenderId"] = tenderId_14
    db_test_params.update_one({"_id": 27}, {"$set": {"auction_par.json.test_14.tenderId": tenderId_14}})
    db_test_params.update_one({"_id": 27}, {"$set": {"auction_par.json.test_14_1.tenderId": tenderId_14}})
    tenderId_15 = par["test_15_1"]["tenderId"]
    tenderId_15 += 1
    par["tenderId"] = tenderId_15
    db_test_params.update_one({"_id": 27}, {"$set": {"auction_par.json.test_15_1.tenderId": tenderId_15}})
    tenderId_16 = par["test_16_1"]["tenderId"]
    tenderId_16 += 1
    par["tenderId"] = tenderId_16
    db_test_params.update_one({"_id": 27}, {"$set": {"auction_par.json.test_16_1.tenderId": tenderId_16}})
    db_test_params.update_one({"_id": 27}, {"$set": {"auction_par.json.test_16.tenderId": tenderId_16}})
    tenderId_17 = par["test_17_1"]["tenderId"]
    tenderId_17 += 1
    par["tenderId"] = tenderId_17
    db_test_params.update_one({"_id": 27}, {"$set": {"auction_par.json.test_17_1.tenderId": tenderId_17}})
    # db_test_params.update_one({"_id": 27}, {"$set": {"auction_par.json.test_17.tenderId": tenderId_17}})
    tenderId_18 = par["test_18_1"]["tenderId"]
    tenderId_18 += 1
    par["tenderId"] = tenderId_18
    db_test_params.update_one({"_id": 27}, {"$set": {"auction_par.json.test_18.tenderId": tenderId_18}})
    db_test_params.update_one({"_id": 27}, {"$set": {"auction_par.json.test_18_1.tenderId": tenderId_18}})
    tenderId_19_1 = par["test_19_1"]["tenderId"]
    tenderId_19_1 += 1
    par["tenderId"] = tenderId_19_1
    db_test_params.update_one({"_id": 27}, {"$set": {"auction_par.json.test_19_1.tenderId": tenderId_19_1}})
    tenderId_20_1 = par["test_20_1"]["tenderId"]
    tenderId_20_1 += 1
    par["tenderId"] = tenderId_20_1
    db_test_params.update_one({"_id": 27}, {"$set": {"auction_par.json.test_20_1.tenderId": tenderId_20_1}})

def s_aladdin_pure(pure_json, t, cmbro):
    @create_result_DB
    def s_aladdin_pure_init(bro):
        qa = {"query": { "q": {
                        "name": "aladdin_like_prozorro",
                        "version": "0.0.0.1",
                        "group": 'pure_json'}
                },
              'test_name': t,
              'wts': WebTestSession(useBrowser=False)
              }
        return qa

    #dbid = 19
    qqq = s_aladdin_pure_init(cmbro)

    par = qqq["wts"].__mongo__.get_params(26)["auction_par.json"]
    suite = ParamsTestSuite(_params={"result_id": qqq["wts"].result_id,
                                     "DB": qqq["wts"].__mongo__,
                                     "auction_par.json": par
                                     })
    pre_par_AlladinPure(par, qqq["wts"].__mongo__.test_params)
    atos_AlladinPure(qqq, suite)

    return suite
def atos_AlladinPure(qqq, suite):
    suite.addTest(TestAladdinPure("test_01_get_balance_positive", _params=qqq))
    suite.addTest(TestAladdinPure("test_02_get_balance_acc_negative", _params=qqq))
    suite.addTest(TestAladdinPure("test_03_get_balance_without_guid_negative", _params=qqq))
    suite.addTest(TestAladdinPure("test_14_write_off_money_positive", _params=qqq))
    suite.addTest(TestAladdinPure("test_15_write_off_money_tender_is_null_negative", _params=qqq))
    suite.addTest(TestAladdinPure("test_16_write_off_money_site_type_not_found_negative", _params=qqq))
    suite.addTest(TestAladdinPure("test_17_write_off_money_error_negative", _params=qqq))
def pre_par_AlladinPure(par, db_test_params):
    tenderId_14 = par["test_14"]["tenderId"]
    tenderId_14 += 1
    par["tenderId"] = tenderId_14
    db_test_params.update_one({"_id": 26}, {"$set": {"auction_par.json.test_14.tenderId": tenderId_14}})
    tenderId_15 = par["test_15_1"]["tenderId"]
    tenderId_15 += 1
    par["tenderId"] = tenderId_15
    db_test_params.update_one({"_id": 26}, {"$set": {"auction_par.json.test_15_1.tenderId": tenderId_15}})
    tenderId_16 = par["test_16_1"]["tenderId"]
    tenderId_16 += 1
    par["tenderId"] = tenderId_16
    db_test_params.update_one({"_id": 26}, {"$set": {"auction_par.json.test_16_1.tenderId": tenderId_16}})
    db_test_params.update_one({"_id": 26}, {"$set": {"auction_par.json.test_16.tenderId": tenderId_16}})
    tenderId_17 = par["test_17_1"]["tenderId"]
    tenderId_17 += 1
    par["tenderId"] = tenderId_17
    db_test_params.update_one({"_id": 26}, {"$set": {"auction_par.json.test_17_1.tenderId": tenderId_17}})
    tenderId_18 = par["test_18_1"]["tenderId"]
    tenderId_18 += 1
    par["tenderId"] = tenderId_18
    db_test_params.update_one({"_id": 26}, {"$set": {"auction_par.json.test_18.tenderId": tenderId_18}})
    db_test_params.update_one({"_id": 26}, {"$set": {"auction_par.json.test_18_1.tenderId": tenderId_18}})
    tenderId_19_1 = par["test_19_1"]["tenderId"]
    tenderId_19_1 += 1
    par["tenderId"] = tenderId_19_1
    db_test_params.update_one({"_id": 26}, {"$set": {"auction_par.json.test_19_1.tenderId": tenderId_19_1}})
    tenderId_20_1 = par["test_20_1"]["tenderId"]
    tenderId_20_1 += 1
    par["tenderId"] = tenderId_20_1
    db_test_params.update_one({"_id": 26}, {"$set": {"auction_par.json.test_20_1.tenderId": tenderId_20_1}})

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

    par = qqq["wts"].__mongo__.get_params(24)["auction_par.json"]
    # tenderId = auction_par.json["tenderId"]
    # tenderId += 1
    # auction_par.json["tenderId"] = tenderId

    tenderId_04 = par["test_04"]["tenderId"]
    tenderId_04 += 1
    par["tenderId"] = tenderId_04


    qqq["wts"].__mongo__.\
        test_params.\
        update_one({"_id": 24},
                   {"$set": {"auction_par.json.test_04.tenderId": tenderId_04}})

    tenderId_04_st_2 = par["test_04_siteType_2"]["tenderId"]
    tenderId_04_st_2 +=1
    par["tenderId"] = tenderId_04_st_2
    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"auction_par.json.test_04_siteType_2.tenderId": tenderId_04_st_2}})




    tenderId_06 = par["test_06"]["tenderId"]
    tenderId_06 +=1
    par["tenderId"] = tenderId_06
    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"auction_par.json.test_06.tenderId": tenderId_06}})


    tenderId_06_siteType_2 = par["test_06_siteType_2"]["tenderId"]
    tenderId_06_siteType_2 += 1
    par["tenderId"] = tenderId_06_siteType_2
    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"auction_par.json.test_06_siteType_2.tenderId": tenderId_06_siteType_2}})



    tenderId_07 = par["test_07"]["tenderId"]
    tenderId_07 += 1
    par["tenderId"] = tenderId_07

    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"auction_par.json.test_07.tenderId": tenderId_07}})
    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"auction_par.json.test_07_1.tenderId": tenderId_07}})



    tenderId_07_sitetype_2_suite_2 = par["test_07_siteType_2"]["tenderId"]
    tenderId_07_sitetype_2_suite_2 += 1
    par["tenderId"] = tenderId_07_sitetype_2_suite_2

    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"auction_par.json.test_07_siteType_2.tenderId": tenderId_07_sitetype_2_suite_2}})
    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"auction_par.json.test_07_1_siteType_2.tenderId": tenderId_07_sitetype_2_suite_2}})


    tenderId_08 = par["test_08"]["tenderId"]
    tenderId_08 += 1
    par["tenderId"] = tenderId_08

    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"auction_par.json.test_08.tenderId": tenderId_08}})





    tenderId_08_sitetype_2_suite_2 = par["test_08_siteType_2"]["tenderId"]
    tenderId_08_sitetype_2_suite_2 += 1
    par["tenderId"] = tenderId_08_sitetype_2_suite_2

    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"auction_par.json.test_08_siteType_2.tenderId": tenderId_08_sitetype_2_suite_2}})


    tenderId_09 = par["test_09_1"]["tenderId"]
    tenderId_09 += 1
    par["tenderId"] = tenderId_09

    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"auction_par.json.test_09_1.tenderId": tenderId_09}})


    tenderId_09_sitetype_2_suite_2 = par["test_09_siteType_2"]["tenderId"]
    tenderId_09_sitetype_2_suite_2 += 1
    par["tenderId"] = tenderId_09_sitetype_2_suite_2

    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"auction_par.json.test_09_1_siteType_2.tenderId": tenderId_09_sitetype_2_suite_2}})



    tenderId_10 = par["test_10_1"]["tenderId"]
    tenderId_10 +=1
    par["tenderId"] = tenderId_10

    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"auction_par.json.test_10_1.tenderId": tenderId_10}})


    tenderId_10_1_siteType_2 = par["test_10_1_siteType_2"]["tenderId"]
    tenderId_10_1_siteType_2 += 1
    par["tenderId"] = tenderId_10_1_siteType_2

    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"auction_par.json.test_10_1_siteType_2.tenderId": tenderId_10_1_siteType_2}})


    tenderId_11 = par["test_11"]["tenderId"]
    tenderId_11 += 1
    par["tenderId"] = tenderId_11
    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"auction_par.json.test_11.tenderId": tenderId_11}})
    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"auction_par.json.test_11_1.tenderId": tenderId_11}})
    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"auction_par.json.test_11_2.tenderId": tenderId_11}})



    tenderId_12_1 = par["test_12_1"]["tenderId"]
    tenderId_12_1 += 1
    par["tenderId"] = tenderId_12_1
    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"auction_par.json.test_12_1.tenderId": tenderId_12_1}})


    #создание уникального tenderId для test_14
    tenderId_14 = par["test_14_1"]["tenderId"]
    tenderId_14 += 1
    par["tenderId"] = tenderId_14
    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"auction_par.json.test_14.tenderId": tenderId_14}})
    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"auction_par.json.test_14_1.tenderId": tenderId_14}})




    tenderId_18 = par["test_18_1"]["tenderId"]
    tenderId_18 += 1
    par["tenderId"] = tenderId_18

    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"auction_par.json.test_18.tenderId": tenderId_18}})
    qqq["wts"].__mongo__.test_params.update_one({"_id": 24}, {"$set": {"auction_par.json.test_18_1.tenderId": tenderId_18}})





    suite = ParamsTestSuite(
                _params={"result_id": qqq["wts"].result_id,
                         "DB": qqq["wts"].__mongo__,
                         "auction_par.json":par
                         }
    )

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
    # suite.addTest(TestByBilling("test_21_reserve_balance_positive_sitetype_2_suite_2", _params=qqq))
    # suite.addTest(TestByBilling("test_22_reserve_balance_tender_id_is_null_negative_sitetype_2_suite_2", _params=qqq))
    # suite.addTest(TestByBilling("test_23_reserve_balance_total_money_is_zero_positive_sitetype_2_suite_2", _params=qqq))
    # suite.addTest(TestByBilling("test_24_return_monies_positive_sitetype_2_suite_2", _params=qqq))
    # suite.addTest(TestByBilling("test_25_return_monies_without_reserve_negative_sitetype_2_suite_2", _params=qqq))
    # suite.addTest(TestByBilling("test_26_return_monies_tender_is_null_negative_sitetype_2_suite_2", _params=qqq))
    # suite.addTest(TestByBilling("test_27_return_monies_error_negative_sitetype_2_suite_2", _params=qqq))


    qqq2={"query": { "q": {
                        "name": "billing_metods",
                        "version": "0.0.0.1",
                        "group": g}
                },
                'test_name': t,
                'wts': WebTestSession(useBrowser=False),
                "siteType": '2'
              }

    #suite.addTest(TestByBilling("test_21_reserve_balance_positive_sitetype_2_suite_2", _params=qqq2))
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


    qqq3={"query": { "q": {
                        "name": "billing_metods",
                        "version": "0.0.0.1",
                        "group": g}
                },
                'test_name': t,
                'wts': WebTestSession(useBrowser=False),
                "siteType": '2'
              }

    # suite.addTest(TestByBilling("test_14_write_off_money_positive", _params=qqq3))
    # suite.addTest(TestByBilling("test_15_write_off_money_tender_is_null_negative", _params=qqq3))
    # suite.addTest(TestByBilling("test_16_write_off_money_site_type_not_found_negative", _params=qqq3))
    # suite.addTest(TestByBilling("test_17_write_off_money_error_negative", _params=qqq3))


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
              'wts': WebTestSession()
              }
        qa.update({"registartion_data":qa["wts"].__mongo__.get_params(23)["company"][0]})
        qa['wts'].set_main_page(qa['query'])
        return qa

    #dbid = 20
    qqq = s_publish_test_init(cmbro)

    par = qqq["wts"].__mongo__.get_params(26)["par"]
    par1 = qqq["wts"].__mongo__.get_params(27)["par"]
    par2 = qqq["wts"].__mongo__.get_params(25)["par"]

    pre_par_AlladinPure(par, qqq["wts"].__mongo__.test_params)
    pre_par_prozorro(par1, qqq["wts"].__mongo__.test_params)
    pre_par_alddin_like_prozorro(par2, qqq["wts"].__mongo__.test_params)
    
    t = qqq["wts"].__mongo__.get_params(21)

    suite = ParamsTestSuite(_params={
                "result_id": qqq["wts"].result_id,
                "DB": qqq["wts"].__mongo__,
                "tender_json": qqq["wts"].__mongo__.get_params(22),
                "start_url": t["start_url"],
                "login_url": t["login_url"],
                "authorization": t["authorization"],
                "lang": t["lang"],
                "par":par
    })
    
    #billing metods
    # atos_AlladinPure(qqq, suite)
    #
    # qqq_prozorro={"query": qqq["query"],
    #       'test_name': t,
    #       'wts': qqq["wts"],
    #       "auction_par.json":par1
    #       }
    # atos_prozorro(qqq_prozorro, suite)
    #
    # qqq_alddin_like_prozorro = {"query": qqq["query"],
    #                 'test_name': t,
    #                 'wts': qqq["wts"],
    #                 "auction_par.json": par2
    #                 }
    # atos_aladin_like_prozorro(qqq_alddin_like_prozorro, suite)
    #
    # # main page interface not authorization
    suite.addTest(Load_main_page("page_loaded", _params=qqq))
    suite.addTest(Load_main_page("menu_presented", _params=qqq))
    suite.addTest(Load_main_page("set_lang", _params=qqq))
    suite.addTest(Tender_Tab("tab_visible", _params=qqq))
    suite.addTest(Tender_Tab("tab_list", _params=qqq))
    suite.addTest(Tender_Tab("tab_search", _params=qqq))
    suite.addTest(Tender_Tab("tab_filters", _params=qqq))

    # login page inteface
    suite.addTest(Login_page("login_menu", _params=qqq))
    suite.addTest(Login_page("open_login", _params=qqq))
    suite.addTest(Login_page("check_lang", _params=qqq))
    suite.addTest(Login_page("login_owner", _params=qqq))
    suite.addTest(Login_page("login_provider", _params=qqq))
    suite.addTest(Login_page("open_register_form", _params=qqq))
    #suite.addTest(Login_page("open_restore_password", _params=qqq))


    # #tender owner registartion
    # suite.addTest(Registartion("try_login", _params=qqq))
    # suite.addTest(Registartion("open_register_form", _params=qqq))
    # suite.addTest(Registartion("reg_company", _params=qqq))
    # suite.addTest(Registartion("profile_settings", _params=qqq))
    #
    # #provider registration
    # q_provider={"query": qqq["query"],
    #       'test_name': t,
    #       'wts': qqq["wts"],
    #       "registartion_data":qqq["wts"].__mongo__.get_params(23)["company"][1]
    #       }
    #
    # suite.addTest(Registartion("try_login961891", _params=q_provider))
    # suite.addTest(Registartion("open_register_form", _params=q_provider))
    # suite.addTest(Registartion("reg_company", _params=q_provider))
    # suite.addTest(Registartion("profile_settings", _params=qqq))

    suite.addTest(Test_Below("create_menu", _params=qqq))
    suite.addTest(Test_Below("select_below_menu", _params=qqq))
    suite.addTest(Test_Below("set_description", _params=qqq))
    suite.addTest(Test_Below("set_curr", _params=qqq))
    suite.addTest(Test_Below("set_multilot", _params=qqq))
    suite.addTest(Test_Below("set_dates", _params=qqq))
    suite.addTest(Test_Below("add_lot", _params=qqq))
    suite.addTest(Test_Below("add_item", _params=qqq))
    suite.addTest(Test_Below("add_features", _params=qqq))
    suite.addTest(Test_Below("add_doc", _params=qqq))
    suite.addTest(Test_Below("open_draft_by_url", _params=qqq))
    suite.addTest(Test_Below("open_draft_by_url_edit", _params=qqq))
    suite.addTest(Test_Below("open_draft_by_url_delete", _params=qqq))

    suite.addTest(Test_Below("create_below_publish", _params=qqq))


    q_provider1={"query": qqq["query"],'test_name': t,'wts': qqq["wts"],
          "bid_json": qqq["wts"].__mongo__.get_params(22)["bids"][0]
          }
    suite.addTest(Below_Bid("login_provider", _params=q_provider1))
    suite.addTest(Below_Bid("select_below_type", _params=q_provider1))
    suite.addTest(Below_Bid("select_tender_period", _params=q_provider1))
    suite.addTest(Below_Bid("find_tender", _params=q_provider1))
    suite.addTest(Below_Bid("wait_for_tender_period", _params=q_provider1))
    suite.addTest(Below_Bid("add_bid", _params=q_provider1))


    q_provider2 = {"query": qqq["query"], 'test_name': t,  'wts': qqq["wts"],
                   "bid_json": qqq["wts"].__mongo__.get_params(22)["bids"][1]
                   }
    suite.addTest(Below_Bid("login_provider", _params=q_provider2))
    suite.addTest(Below_Bid("find_tender", _params=q_provider2))
    suite.addTest(Below_Bid("add_bid", _params=q_provider2))

    #suite.suite_params.update({"ProzorroId":"UA-2018-03-26-000076-a"})

    suite.addTest(Qualification("login_owner", _params=qqq))
    suite.addTest(Below_Bid("find_tender", _params=qqq))
    suite.addTest(Qualification("wait_for_status",
                                _params={"query": qqq["query"], 'test_name': t,  'wts': qqq["wts"],
                                "wait_status": 5}))

    suite.addTest(Qualification("q_tabs", _params=q_provider1))
    suite.addTest(Qualification("q_tab_result_award_1", _params=q_provider1))

    return suite

def s_publish_prod(g, t, cmbro, registartion=0):
    @create_result_DB
    def s_publish_prod_init(bro):
        qa = {"query": {"q": {
            "name": "publish_app",
            "version": "0.0.0.1",
            "group": g}
        },
            'test_name': t,
            'wts': WebTestSession()
        }
        qa.update({"registartion_data": qa["wts"].__mongo__.get_params(23)["company"][0]})
        qa['wts'].set_main_page(qa['query'])
        return qa

    # dbid = 20
    qqq = s_publish_prod_init(cmbro)
    t = qqq["wts"].__mongo__.get_params(28)
    td = qqq["wts"].__mongo__.get_params(29)

    suite = ParamsTestSuite(_params={
        "result_id": qqq["wts"].result_id,
        "DB": qqq["wts"].__mongo__,
        "tender_json": td,
        "start_url": t["start_url"],
        "login_url": t["login_url"],
        "authorization": t["authorization"],
        "lang": t["lang"]
    })

    # # main page interface not authorization
    suite.addTest(Load_main_page("page_loaded", _params=qqq))
    # suite.addTest(Load_main_page("menu_presented", _params=qqq))
    # suite.addTest(Load_main_page("set_lang", _params=qqq))
    # suite.addTest(Tender_Tab("tab_visible", _params=qqq))
    # suite.addTest(Tender_Tab("tab_list", _params=qqq))
    # # suite.addTest(Tender_Tab("tab_search", _params=qqq))
    # suite.addTest(Tender_Tab("tab_filters", _params=qqq))
    #
    # # login page inteface
    # suite.addTest(Login_page("login_menu", _params=qqq))
    # suite.addTest(Login_page("open_login", _params=qqq))
    # suite.addTest(Login_page("check_lang", _params=qqq))
    # suite.addTest(Login_page("login_owner", _params=qqq))
    # suite.addTest(Login_page("login_provider", _params=qqq))
    # suite.addTest(Login_page("open_register_form", _params=qqq))
    # suite.addTest(Login_page("open_restore_password", _params=qqq))

    if registartion>0:
        # tender owner registartion
        suite.addTest(Registartion("try_login", _params=qqq))
        suite.addTest(Registartion("open_register_form", _params=qqq))
        suite.addTest(Registartion("reg_company", _params=qqq))
        suite.addTest(Registartion("profile_settings", _params=qqq))

        #provider registration test00134
        q_provider={"query": qqq["query"],
              'test_name': t,
              'wts': qqq["wts"],
              "registartion_data":qqq["wts"].__mongo__.get_params(23)["company"][1]
              }
        suite.addTest(Registartion("try_login", _params=q_provider))
        suite.addTest(Registartion("open_register_form", _params=q_provider))
        suite.addTest(Registartion("reg_company", _params=q_provider))
        suite.addTest(Registartion("profile_settings", _params=q_provider))

    # tender draft
    suite.addTest(Test_Below("create_menu", _params=qqq))
    suite.addTest(Test_Below("select_below_menu", _params=qqq))
    suite.addTest(Test_Below("set_description", _params=qqq))
    suite.addTest(Test_Below("set_curr", _params=qqq))
    suite.addTest(Test_Below("set_multilot", _params=qqq))
    suite.addTest(Test_Below("set_dates", _params=qqq))
    suite.addTest(Test_Below("add_lot", _params=qqq))
    suite.addTest(Test_Below("add_item", _params=qqq))
    suite.addTest(Test_Below("add_features", _params=qqq))
    suite.addTest(Test_Below("add_doc", _params=qqq))
    suite.addTest(Test_Below("open_draft_by_url", _params=qqq))
    suite.addTest(Test_Below("open_draft_by_url_edit", _params=qqq))
    suite.addTest(Test_Below("open_draft_by_url_delete", _params=qqq))

    # tender publish
    suite.addTest(Test_Below("create_below_publish", _params=qqq))

    #add bid
    qqq.update({"bid_json": qqq["wts"].__mongo__.get_params(29)["bids"][0]})
    suite.addTest(Below_Bid("login_provider", _params=qqq))
    suite.addTest(Below_Bid("select_below_type", _params=qqq))
    suite.addTest(Below_Bid("select_tender_period", _params=qqq))
    suite.addTest(Below_Bid("find_tender", _params=qqq))
    suite.addTest(Below_Bid("wait_for_tender_period", _params=qqq))
    suite.addTest(Below_Bid("add_bid", _params=qqq))

    # provider registration test00134
    qqq2 = {"query": qqq["query"],
                  'test_name': t,
                  'wts': qqq["wts"],
                  "bid_json":  qqq["wts"].__mongo__.get_params(29)["bids"][1]
                  }

    suite.addTest(Below_Bid("login_provider", _params=qqq2))
    suite.addTest(Below_Bid("find_tender", _params=qqq2))
    suite.addTest(Below_Bid("add_bid", _params=qqq2))

    return suite

def s_login_after_full_registration(g, cmd_bro):
    @create_result_DB
    def s_login_after_full_registration_init(bro):
        qa = {"query": {"q": {"name": "UserRegistrationForm", "version": "0.0.0.3"}},
              'test_name': 'UserRegistrationFormTest',
              'login_url': 'https://win-net-core:44320/account/login',
              'wts': WebTestSession(browser=bro)
              }
        if g is not None:
            qa["query"]["q"].update({'group': g})
        qa['wts'].set_main_page(qa['query'])
        return qa

    qqq = s_login_after_full_registration_init(cmd_bro)
    suite = ParamsTestSuite(_params={"result_id": qqq["wts"].result_id, "DB": qqq["wts"].__mongo__})
    suite.addTest(LoginAfterRegistrationCompany("test_01", _params=qqq, _parent_suite= suite))
    #suite.addTest(LoginAfterRegistrationCompany("test_02_exit", _params=qqq, _parent_suite= suite))
    #suite.addTest(LoginAfterRegistrationCompany("test_03_login", _params=qqq, _parent_suite= suite))
    suite.addTest(LoginAfterRegistrationCompany("test_04_edit", _params=qqq, _parent_suite= suite))
    suite.addTest(LoginAfterRegistrationCompany("test_05_add_view_delete_docs", _params=qqq, _parent_suite= suite))
    suite.addTest(LoginAfterRegistrationCompany("test_06_add_employees", _params=qqq, _parent_suite= suite))
    # suite.addTest(LoginAfterRegistrationCompany("test_07_edit_employees"))

    return suite



def runner(arg):
    parser = OptionParser()
    parser.add_option("-s", action="store", type="string") # test name
    parser.add_option("-g", action="store", type="string") # group test / prod
    parser.add_option("-b", action="store", type="string") # browser Chrome default
    parser.add_option("-r", action="store", type="int")  # registration on/off
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
    elif opt == 'aladdin_like_prozorro':
        ttt = s_aladdin_like_prozorro(options.g, tname,  bro)
    elif opt == 'aladdin_pure':
        ttt = s_aladdin_pure(options.g, tname,  bro)
    elif opt == 'prozorro':
        ttt = s_prozorro(options.g, tname,  bro)
    elif opt == 'publish_test':
        ttt = s_publish_test(options.g,tname,  bro)
    elif opt == 'publish_prod':
        ttt = s_publish_prod(options.g,tname,  bro, options.r)
    elif opt == 'rialto_publish_prod':
        ttt = s_rialto_publish_prod(options.g,tname,  bro, options.r)
    elif opt == 'Login_after_full_registration':
        ttt = s_login_after_full_registration(options.g, bro)

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
