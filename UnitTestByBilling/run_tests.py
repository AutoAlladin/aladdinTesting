import unittest
import sys
from optparse import make_option, OptionParser

import xmlrunner

from Aladdin.Accounting.AladdinUtils import WebTestSession, AvaliableBrowsers
from Aladdin.Accounting.decorators.StoreTestResult import create_result_DB
from Aladdin.Billing.CreateAccount import *
from OnPublish.MainPage.load_main_page import Load_main_page, Tender_Tab
from UnitTestByBilling.UnitTestByBilling import UnitTestByBilling
from billing_UI.Billing import BalanceAfterBid






def s_billing_metods(g, t, cmbro):

    json={   "tenderId": 26285,
             "lotId": 11,
             "amount": 1000.0,
             "currency": "ГРН",
             "descriptions": "Тендер: Соль таблетированная 22 000 кг. Лот №1 Позиції: Сіль таблетована   ",
             "totalMoney": 511.5,
             "companyUuid": "68A14F2A-C5A2-4A76-9D86-88C2FFAD742B",
             "serviceIdentifierUuid": "00e525f3-420b-4d76-b538-d0efc7957cd2",
             "siteType": 2
             }
    @create_result_DB
    def s_load_main_page_init(bro):
        qa = {"query": { "q": {
                        "name": "billing_metods",
                        "version": "0.0.0.1",
                        "group": g}
                },
              'test_name': t,
              'wts': WebTestSession(),
              'par': json
              }
        qa['wts'].set_main_page(qa['query'])
        return qa

    #dbid = 18
    qqq = s_load_main_page_init(cmbro)
    suite = ParamsTestSuite(_params={"result_id": qqq["wts"].result_id, "DB": qqq["wts"].__mongo__})

    suite.addTest( UnitTestByBilling("test_01_get_balance_positive", _params=qqq))
    suite.addTest(UnitTestByBilling("test_02_get_balance_acc_negative", _params=qqq))
    suite.addTest(UnitTestByBilling("test_03_get_balance_without_guid_negative", _params=qqq))
    suite.addTest(UnitTestByBilling("test_04_reserve_balance_positive", _params=qqq))
    suite.addTest(UnitTestByBilling("test_05_reserve_balance_tender_id_is_null_negative", _params=qqq))
    suite.addTest(UnitTestByBilling("test_06_reserve_balance_total_money_is_zero_negative", _params=qqq))
    suite.addTest(UnitTestByBilling("test_07_return_monies_positive", _params=qqq))
    suite.addTest(UnitTestByBilling("test_08_return_monies_tender_is_null_negative", _params=qqq))
    suite.addTest(UnitTestByBilling("test_09_return_monies_error_negative", _params=qqq))
    suite.addTest(UnitTestByBilling("test_10_return_monies_by_company_uuid_positive", _params=qqq))
    suite.addTest(UnitTestByBilling("test_11_return_monies_by_company_uuid_tender_is_null_negative", _params=qqq))
    suite.addTest(UnitTestByBilling("test_12_return_monies_by_company_uuid_error_negative", _params=qqq))
    suite.addTest(UnitTestByBilling("test_13_write_off_money_positive", _params=qqq))
    suite.addTest(UnitTestByBilling("test_14_write_off_money_tender_is_null_negative", _params=qqq))
    suite.addTest(UnitTestByBilling("test_15_write_off_money_site_type_not_found_negative", _params=qqq))
    suite.addTest(UnitTestByBilling("test_16_write_off_money_error_negative", _params=qqq))
    suite.addTest(UnitTestByBilling("test_17_cancel_reserve_money_positive", _params=qqq))
    suite.addTest(UnitTestByBilling("test_18_cancel_reserve_money_tender_id_is_null_negative", _params=qqq))
    suite.addTest(UnitTestByBilling("test_19_cancel_reserve_money_error_negative", _params=qqq))

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
        ttt = s_billing_metods(options.g, tname, bro)
#    elif opt =='run_bil':
 #       ttt = s_run_bil(options.g,  # test group from D
  #                      tname,  # test name for report
   #                     bro)    # browser? default - Chrome


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