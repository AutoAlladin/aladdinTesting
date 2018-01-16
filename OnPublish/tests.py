import unittest
import sys
from optparse import make_option, OptionParser

from copy import deepcopy

import xmlrunner

from Aladdin.Accounting.AladdinUtils import WebTestSession, AvaliableBrowsers
from Aladdin.Accounting.Authorization.Login import Login
from Aladdin.Accounting.decorators.StoreTestResult import create_result_DB
from Aladdin.Billing.CreateAccount import *
from OnPublish.MainPage.load_main_page import Load_main_page


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
    return suite





if __name__ == '__main__':

    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    subdirs= [x[0] for x in os.walk(os.path.dirname(os.path.abspath(__file__))) if not x[0].startswith("_") and not x[0].startswith(".")]
    sys.path.extend(subdirs)

    parser = OptionParser()
    parser.add_option("-s", action="store", type="string")
    parser.add_option("-g", action="store", type="string")
    parser.add_option("-b", action="store", type="string")

    (options, args) = parser.parse_args()

    #runner = unittest.TextTestRunner(verbosity=2)
    runner = xmlrunner.XMLTestRunner(output='test-reports',
                                         verbosity=2)
    opt = options.s
    bro = options.b

    if bro == "ch":
        bro = AvaliableBrowsers.Chrome
    elif bro == "f":
        bro = AvaliableBrowsers.Firefox
    else:
        bro = AvaliableBrowsers.Chrome

    ttt = None

    if opt == 'main_page':
        ttt = s_load_main_page(options.g,"xxx",bro)


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