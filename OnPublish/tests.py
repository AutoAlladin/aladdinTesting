import unittest
import sys
from optparse import make_option, OptionParser

import xmlrunner

from Aladdin.Accounting.AladdinUtils import WebTestSession, AvaliableBrowsers
from Aladdin.Accounting.decorators.StoreTestResult import create_result_DB
from Aladdin.Billing.CreateAccount import *
from OnPublish.MainPage.load_main_page import Load_main_page, Tender_Tab
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

    suite.addTest(Load_main_page("page_loaded", _params=qqq))
    suite.addTest(Load_main_page("menu_presented", _params=qqq))
    suite.addTest(Load_main_page("set_lang", _params=qqq))

    suite.addTest(Tender_Tab("tab_visible", _params=qqq))
    suite.addTest(Tender_Tab("tab_list", _params=qqq))
    suite.addTest(Tender_Tab("tab_filters", _params=qqq))
    suite.addTest(Tender_Tab("tab_search", _params=qqq))

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