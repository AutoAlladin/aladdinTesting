from optparse import make_option, OptionParser

import xmlrunner

from Aladdin.Accounting.AladdinUtils import WebTestSession, AvaliableBrowsers
from Aladdin.Accounting.decorators.StoreTestResult import create_result_DB
from Aladdin.Billing.CreateAccount import *
from OnPublish.MainPage.load_main_page import Load_main_page, Tender_Tab
from OnPublish.MainPage.registration import Registartion
from OnPublish.Procedures.below import Test_Below
from OnPublish.Procedures.bid import Below_Bid


def s_rialto_publish_prod(g, t, cmbro, registartion=0):
    @create_result_DB
    def s_publish_prod_init(bro):
        qa = {"query": {"q": {
            "name": "realto_publish_app",
            "version": "0.0.0.1",
            "group": g}
        },
            'test_name': t,
            'wts': WebTestSession()
        }
        #даные  для регистрации Dtcyzybq
        qa.update({"registartion_data": qa["wts"].__mongo__.get_params(30)["company"][0]})
        qa['wts'].set_main_page(qa['query'])
        return qa


    qqq = s_publish_prod_init(cmbro)
    t = qqq["wts"].__mongo__.get_params(31)
    td = qqq["wts"].__mongo__.get_params(32)

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
    suite.addTest(Load_main_page("menu_presented", _params=qqq))
    suite.addTest(Load_main_page("set_lang", _params=qqq))
    suite.addTest(Tender_Tab("tab_visible", _params=qqq))
    suite.addTest(Tender_Tab("tab_list", _params=qqq))
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

    if registartion > 0:
        # tender owner registartion
        suite.addTest(Registartion("try_login", _params=qqq))
        suite.addTest(Registartion("open_register_form", _params=qqq))
        suite.addTest(Registartion("reg_company", _params=qqq))
        suite.addTest(Registartion("profile_settings", _params=qqq))

        # provider registration
        q_provider = {"query": qqq["query"],
                      'test_name': t,
                      'wts': qqq["wts"],
                      "registartion_data": qqq["wts"].__mongo__.get_params(30)["company"][1]
                      }
        suite.addTest(Registartion("try_login", _params=q_provider))
        suite.addTest(Registartion("open_register_form", _params=q_provider))
        suite.addTest(Registartion("reg_company", _params=q_provider))
        suite.addTest(Registartion("profile_settings", _params=q_provider))

    # tender draft Dtcyzybq
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
    suite.addTest(Below_Bid("login_provider", _params=qqq))
    suite.addTest(Below_Bid("select_below_type", _params=qqq))
    suite.addTest(Below_Bid("select_tender_period", _params=qqq))
    suite.addTest(Below_Bid("find_tender_for_bid", _params=qqq))
    suite.addTest(Below_Bid("wait_for_tender_period", _params=qqq))
    suite.addTest(Below_Bid("add_bid", _params=qqq))

    return suite


def runner(arg):
    parser = OptionParser()
    parser.add_option("-s", action="store", type="string")  # test name
    parser.add_option("-g", action="store", type="string")  # group test / prod
    parser.add_option("-b", action="store", type="string")  # browser Chrome default
    parser.add_option("-r", action="store", type="int")  # registration on/off
    parser.add_option("--name", action="store", type="string")

    (options, args) = parser.parse_args(arg)

    # runner = unittest.TextTestRunner(verbosity=2)
    runner = xmlrunner.XMLTestRunner(output='test-reports',
                                     verbosity=2)
    opt = options.s
    bro = options.b
    tname = options.name
    if tname is None: tname = opt + " test development " + datetime.datetime.now().isoformat()

    if bro == "ch":
        bro = AvaliableBrowsers.Chrome
    elif bro == "f":
        bro = AvaliableBrowsers.Firefox
    else:
        bro = AvaliableBrowsers.Chrome

    ttt = None


    if opt == 'publish_prod':
        ttt = s_publish_prod(options.g, tname, bro, options.r)

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


if __name__ == '__main__':
    runner(None)
