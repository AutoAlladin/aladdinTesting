import unittest
import sys
from optparse import make_option, OptionParser

from copy import deepcopy

from Aladdin.Accounting.AladdinUtils import WebTestSession, AvaliableBrowsers
from Aladdin.Accounting.Docs import Docs
from Aladdin.Accounting.Registration.UserRegistrationEDRPOU import UserRegistrationEDRPOU
from Aladdin.Accounting.Registration.UserRegistration_FOP import UserRegistration_FOP
from Aladdin.Accounting.Registration.RegistrationCompanyEDRPOU import RegistrationCompany
from Aladdin.Accounting.Registration.RegistrationCompanyFOP import RegistrationCompanyFop
from Aladdin.Accounting.Authorization.Login import Login
from Aladdin.Accounting.Edit.Edit import Edit
from Aladdin.Accounting.Registration.Employees import Employees
from Aladdin.Accounting.Authorization.LoginAfterRegistration import LoginAfterRegistrationCompany
from Aladdin.Accounting.decorators.ParamsTestSuite import ParamsTestSuite
from Aladdin.Accounting.decorators.StoreTestResult import create_result_DB
from Aladdin.Billing.CreateAccount import *
from Aladdin.Billing.CreateAccount import CreateAccount
from Aladdin.Billing.CheckRezerv import CheckReserv
from Aladdin.Billing.CheckBalance import CheckBalance
from Aladdin.Billing.full_billing import full_billing

def s_user_registration():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(UserRegistrationEDRPOU)
    return suite


def s_user_registration_FOP():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(UserRegistration_FOP)
    return suite


def s_company_fop():
    suite = unittest.TestSuite()

    suite.addTest(RegistrationCompanyFop("test_01_registration_userFOP"))
    suite.addTest(RegistrationCompanyFop("test_02_tax_system"))
    suite.addTest(RegistrationCompanyFop("test_03_phone_company"))
    suite.addTest(RegistrationCompanyFop("test_04_email_company"))
    suite.addTest(RegistrationCompanyFop("test_05_country_legal"))
    suite.addTest(RegistrationCompanyFop("test_06_region_legal"))
    suite.addTest(RegistrationCompanyFop("test_07_city_legal"))
    suite.addTest(RegistrationCompanyFop("test_08_legal_address"))
    suite.addTest(RegistrationCompanyFop("test_09_legal_index"))
    suite.addTest(RegistrationCompanyFop("test_10_real_country"))
    suite.addTest(RegistrationCompanyFop("test_11_real_region"))
    suite.addTest(RegistrationCompanyFop("test_12_real_city"))
    suite.addTest(RegistrationCompanyFop("test_13_real_address"))
    suite.addTest(RegistrationCompanyFop("test_14_real_index"))
    suite.addTest(RegistrationCompanyFop("test_15_bank_name"))
    suite.addTest(RegistrationCompanyFop("test_16_bank_mfo"))
    suite.addTest(RegistrationCompanyFop("test_17_bank_account"))
    suite.addTest(RegistrationCompanyFop("test_18_lead_first_name"))
    suite.addTest(RegistrationCompanyFop("test_19_lead_last_name"))
    suite.addTest(RegistrationCompanyFop("test_20_lead_email"))
    suite.addTest(RegistrationCompanyFop("test_21_lead_phone"))
    suite.addTest(RegistrationCompanyFop("test_22_confidant_first_name"))
    suite.addTest(RegistrationCompanyFop("test_23_confidant_last_name"))
    suite.addTest(RegistrationCompanyFop("test_24_confidant_position"))
    suite.addTest(RegistrationCompanyFop("test_25_confidant_email"))
    suite.addTest(RegistrationCompanyFop("test_26_confidant_phone"))
    suite.addTest(RegistrationCompanyFop("test_27_contract_offer"))
    suite.addTest(RegistrationCompanyFop("test_28_save"))
    return suite


def s_company_reg():
    suite = unittest.TestSuite()

    suite.addTest(RegistrationCompany("test_01_registration_user"))
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


def s_login(g):
    @create_result_DB
    def s_login_init():
        qa = {"query": {"q": {"name": "Login", "version": "0.0.0.2", 'group': g}},
              'test_name': 'LOLOLO',
              'wts': WebTestSession()
              }
        qa['wts'].set_main_page(qa['query'])
        return qa

    qqq = s_login_init
    suite = ParamsTestSuite(_params={"result_id": qqq["wts"].result_id, "DB": qqq["wts"].__mongo__})
    suite.addTest(Login("test_01_email", _params=qqq))
    suite.addTest(Login("test_02_pswd", _params=qqq))
    suite.addTest(Login("test_03_btn", _params=qqq))

    return suite


def s_edit_information():
    suite = unittest.TestSuite()

    suite.addTest(Edit("test_01_go_to_user_profile"))
    suite.addTest(Edit("test_02_click_tab_company"))
    suite.addTest(Edit("test_03_click_btn_edit"))
    suite.addTest(Edit("test_04_clear_field_comp_name"))
    suite.addTest(Edit("test_05_update_comp_name"))
    # suite.addTest(Edit("test_06_ownership_type"))
    # suite.addTest(Edit("test_06_company_taxSystem"))
    suite.addTest(Edit("test_08_clear_email"))
    suite.addTest(Edit("test_09_update_email"))
    # suite.addTest(Edit("test_08_select_real_address_city"))
    suite.addTest(Edit("test_10_legal_address_country"))
    suite.addTest(Edit("test_11_clear_field_real_add_str"))
    suite.addTest(Edit("test_12_real_address_street"))
    suite.addTest(Edit("test_13_clear_add_index"))
    suite.addTest(Edit("test_14_real_address_index"))
    suite.addTest(Edit("test_15_clear_comp_bank_acc_mfo"))
    suite.addTest(Edit("test_16_comp_bank_acc_mfo"))
    suite.addTest(Edit("test_17_clear_lead_phone"))
    suite.addTest(Edit("test_18_lead_phone"))
    suite.addTest(Edit("test_19_clear_confidant_first_name"))
    suite.addTest(Edit("test_20_confidant_first_name"))
    suite.addTest(Edit("test_21_clear_confidant_position"))
    suite.addTest(Edit("test_22_confidant_position"))
    suite.addTest(Edit("test_23_click_btn_save_changes"))
    suite.addTest(Edit("test_24_click_tab_profile_tab_about"))
    suite.addTest(Edit("test_25_name_clear"))
    suite.addTest(Edit("test_26_name_change"))
    suite.addTest(Edit("test_27_eng_surname_clear"))
    suite.addTest(Edit("test_28_eng_surname_change"))
    suite.addTest(Edit("test_29_clear_phone"))
    suite.addTest(Edit("test_30_change_u_phone"))
    suite.addTest(Edit("test_31_clear_u_position"))
    suite.addTest(Edit("test_32_change_u_position"))
    suite.addTest(Edit("test_33_click_btnSaveUser"))

    return suite


def s_docs():
    # suite = unittest.defaultTestLoader.loadTestsFromTestCase(Docs)
    suite = unittest.TestSuite()
    suite.addTest(Docs("test_1_Login"))
    suite.addTest(Docs("test_2_User_profile"))
    return suite


def s_Employees():
    suite = unittest.TestSuite()

    suite.addTest(Employees("test_01_go_to_user_profile"))
    suite.addTest(Employees("test_02_tab_empl"))
    suite.addTest(Employees("test_03_add_user"))
    suite.addTest(Employees("test_04_name"))
    suite.addTest(Employees("test_05_name_eu"))
    suite.addTest(Employees("test_06_last_name"))
    suite.addTest(Employees("test_07_last_name_eu"))
    suite.addTest(Employees("test_08_position"))
    suite.addTest(Employees("test_09_email"))
    suite.addTest(Employees("test_10_phone"))
    suite.addTest(Employees("test_11_save"))
    return suite


def s_login_after_full_registration(g, cmd_bro):
    @create_result_DB
    def s_login_after_full_registration_init(bro):
        qa = {"query": {"q": {"name": "UserRegistrationForm", "version": "0.0.0.3"}},
              'test_name': 'UserRegistrationFormTest',
              'login_url': 'https://192.168.80.169:44310/Account/Login',
              'wts': WebTestSession(browser=bro)
              }
        if g is not None:
            qa["query"]["q"].update({'group': g})
        qa['wts'].set_main_page(qa['query'])
        return qa

    qqq = s_login_after_full_registration_init(cmd_bro)
    suite = ParamsTestSuite(_params={"result_id": qqq["wts"].result_id, "DB": qqq["wts"].__mongo__})
    suite.addTest(LoginAfterRegistrationCompany("test_01", _params=qqq))
    suite.addTest(LoginAfterRegistrationCompany("test_02_exit", _params=qqq))
    suite.addTest(LoginAfterRegistrationCompany("test_03_login", _params=qqq))
    suite.addTest(LoginAfterRegistrationCompany("test_04_edit", _params=qqq))
    suite.addTest(LoginAfterRegistrationCompany("test_05_add_view_delete_docs", _params=qqq))
    suite.addTest(LoginAfterRegistrationCompany("test_06_add_employees", _params=qqq))
    # suite.addTest(LoginAfterRegistrationCompany("test_07_edit_employees"))

    return suite

def s_createAccount_billing():
    """
        по быстрому тестируем создание счетов от фонаря
        без параметров:
        test_01_new_UUID_new_EDR  - новый ид, едр из файла з претензией на не использованность
        test_02_new_UUID_old_EDR  - новый ид, тот же едр
        test_03_old_UUID_old_EDR  - попытка еще раз создать такой же счет
        test_04_fail_UUID_new_EDR - заведомо неправильный ИД, новый едр
        test_05_new_UUID_less_EDR - новый ИД, заведомо неправильный короткий ЕДР
        test_06_new_UUID_more_EDR - новый ИД, заведомо неправильный длинный ЕДР
        :return: ParamsTestSuite
    """

    in_dic = dict()
    with open(os.path.dirname(os.path.abspath(__file__)) + '\\Billing\\input.json', 'r',
              encoding="UTF-8") as test_params_file:
        in_dic = json.load(test_params_file)

    in_dic["new_account"]["uuid"] = str(uuid.uuid4())

    q = dict(in_dic=in_dic,
             msg_create_company_account=json.dumps({'companyAccount': in_dic["new_account"]}),
             old_id=in_dic["new_account"]["uuid"],
             old_edr=in_dic["new_account"]["edrpou"]
            )

    suite = ParamsTestSuite(_params={})
    suite.addTest(CreateAccount("test_01_new_UUID_new_EDR", _params=q))
    #suite.addTest(CreateAccount("test_02_new_UUID_old_EDR", _params=q))
    #suite.addTest(CreateAccount("test_03_old_UUID_old_EDR", _params=q))
    #suite.addTest(CreateAccount("test_04_fail_UUID_new_EDR", _params=q))
    #suite.addTest(CreateAccount("test_05_new_UUID_less_EDR", _params=q))
    #suite.addTest(CreateAccount("test_06_new_UUID_more_EDR", _params=q))

    return suite

def s_checkBalance():
    """
        test_01_empty_acc - для нового счета пустого, None
        test_02_full_acc - ля счета с позитивным остатком
    :return:
    """

    q = dict(service="http://192.168.95.153:91/api/balance?companyUuid={0}",
             #service_refill = "http://192.168.80.198:54685/api/Private24/test",
             service_refill="http://192.168.95.153:121/api/Private24/test",
             acc="9DA86558-58C3-4089-8C43-216160F444BA",
             refill=[{"TransactionGuid":"3420E605-ADFA-4FBC-8B7C-588222EA45B2",
                     "CompanyEdrpoSender": "30000061",
                     "CompanyEdrpoReceiver": "30000061",
                     "Amount": "20000",
                     "Currency": "UAH"
                }]
             )

    suite = ParamsTestSuite(_params={})
    #suite.addTest(CheckBalance("test_01_balance", _params=q))
    suite.addTest(CheckBalance("test_02_refill_full", _params=q))
    #несколько счетов в одном запросе
    q1= deepcopy(q)
    q1["refill"].append(
                {"TransactionGuid":"3420E605-ADFA-4FBC-8B7C-588222EA45B2",
                     "CompanyEdrpoSender": "30000061",
                     "CompanyEdrpoReceiver": "30000061",
                     "Amount": "30000",
                     "Currency": "UAH"
                })

    #suite.addTest(CheckBalance("test_02_refill_full", _params=q1))


    return suite

def s_checkRezerv():

    q = {
        "services": {
            "service_fix_money": "http://192.168.95.153:91/api/balance/WriteOffMoney",
            "service_add_reserv": "http://192.168.95.153:91/api/balance/reserve",
            "service_cansel_reserv": "http://192.168.95.153:91/api/balance/CancelReserve",
            "service_return_money": "http://192.168.95.153:91/api/balance/ReturnMonies"
        },
        "rezerv": {
            "TenderId": 506,
            "LotId": 1,
            "Amount": 4000.0,
            "Currency": "UAH",
            "Descriptions": "chupakabra",
            "TotalMoney": 5000.0,
            "CompanyUuid": "960B972C-3106-4FC5-AB0B-DFA2EBF46837"
        },
        "cansel_reserv": {
            "TenderId": 506,
            "LotId": 1,
            "CompanyUuid": "D9B92253-6275-42D8-9D04-7A3258DD9728"
        },
        "return_money": {
            "CompanyUuid": "2C6A97A8-4BDE-48BE-A3BB-A4BDA2DEF043"
        },
        "fix_money": {
            "TenderId": 506,
            "SiteType": 1,
            "CompanyUuid": "960B972C-3106-4FC5-AB0B-DFA2EBF46837",
        }
    }

    suite = ParamsTestSuite(_params={})
    #suite.addTest(CheckReserv("test_01_add_rezerv", _params=q))
    #suite.addTest(CheckReserv("test_02_cansel_rezerv", _params=q))
    #suite.addTest(CheckReserv("test_03_return_money", _params=q))
    suite.addTest(CheckReserv("test_04_charge_off", _params=q))
    return suite


def s_full_billinig():
    """
    params for create account:

    """
    in_dic = dict()
    with open(os.path.dirname(os.path.abspath(__file__)) + '\\Billing\\input.json', 'r',
              encoding="UTF-8") as test_params_file:
        in_dic = json.load(test_params_file)

    in_dic["new_account"]["uuid"] = str(uuid.uuid4())

    q = dict(in_dic=in_dic,
             msg_create_company_account=json.dumps({'companyAccount': in_dic["new_account"]}),
             old_id=in_dic["new_account"]["uuid"],
             old_edr=in_dic["new_account"]["edrpou"]
             )


    """
    params for refill balance:
    
    """
    q1 = dict(service="http://192.168.95.153:91/api/balance?companyUuid={0}",
             # service_refill = "http://192.168.80.198:54685/api/Private24/test",
             service_refill="http://192.168.95.153:121/api/Private24/test",
             acc=in_dic["new_account"]["TenderId"],
             #acc="9DA86558-58C3-4089-8C43-216160F444BA",
              edr=in_dic["new_account"]["edrpou"],
             refill=[{"TransactionGuid": "3420E605-ADFA-4FBC-8B7C-588222EA45B2",
                      "CompanyEdrpoSender": in_dic["new_account"]["edrpou"],
                      "CompanyEdrpoReceiver": in_dic["new_account"]["edrpou"],
                      "Amount": "1000",
                      "Currency": "UAH"
                      }]
             )

    """
    params for add reserve:
    
    """
    q2 = {
        "services": {
            "service_fix_money": "http://192.168.95.153:91/api/balance/WriteOffMoney",
            "service_add_reserv": "http://192.168.95.153:91/api/balance/reserve",
            "service_cansel_reserv": "http://192.168.95.153:91/api/balance/CancelReserve",
            "service_return_money": "http://192.168.95.153:91/api/balance/ReturnMonies"
        },
        "rezerv": {
            "TenderId": in_dic["new_account"]["TenderId"],
            "LotId": in_dic["new_account"]["LotId"],
            "Amount": 4000.0,
            "Currency": "UAH",
            "Descriptions": "chupakabra",
            "TotalMoney": in_dic["new_account"]["TotalMoney"],
            "CompanyUuid": in_dic["new_account"]["uuid"]
        },
        "cansel_reserv": {
            "TenderId": in_dic["new_account"]["TenderId"],
            "LotId": in_dic["new_account"]["LotId"],
            "CompanyUuid": in_dic["new_account"]["uuid"]
        },
        "return_money": {
            "CompanyUuid": in_dic["new_account"]["uuid"]
        },
        "fix_money": {
            "TenderId": in_dic["new_account"]["TenderId"],
            "SiteType": 1,
            "CompanyUuid": in_dic["new_account"]["uuid"]
        }
        }


    suite = ParamsTestSuite(_params={})
    suite.addTest(CreateAccount("test_01_new_UUID_new_EDR", _params=q))
    suite.addTest(CheckBalance("test_02_refill_full", _params=q1))
    suite.addTest(CheckBalance("test_01_balance", _params=q1))
    suite.addTest(CheckReserv("test_01_add_rezerv", _params=q2))
    suite.addTest(CheckBalance("test_01_balance", _params=q1))
    suite.addTest(CheckReserv("test_04_charge_off", _params=q2))
    suite.addTest(CheckBalance("test_01_balance", _params=q1))
    suite.addTest(CheckReserv("test_01_add_rezerv", _params=q2))
    suite.addTest(CheckReserv("test_02_cansel_rezerv", _params=q2))
    suite.addTest(CheckBalance("test_01_balance", _params=q1))
    return suite

def s_checkBilling():


if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option("-s", action="store", type="string")
    parser.add_option("-g", action="store", type="string")
    parser.add_option("-b", action="store", type="string")

    (options, args) = parser.parse_args()

    runner = unittest.TextTestRunner(verbosity=2)
    opt = options.s
    bro = options.b

    if bro == "ch":
        bro = AvaliableBrowsers.Chrome
    elif bro == "f":
        bro = AvaliableBrowsers.Firefox

    ttt = None

    if opt == 'UserRegistration':
        ttt = s_user_registration()
    elif opt == 'UserRegistration_FOP':
        ttt = s_user_registration_FOP()
    elif opt == 'Login':
        ttt = s_login(options.g)
    elif opt == 'UserRegistration_Company':
        ttt = s_company_reg()
    elif opt == 'edit_information':
        ttt = s_edit_information()
    elif opt == 'docs':
        ttt = s_docs()
    elif opt == 'Employees':
        ttt = s_Employees()
    elif opt == 'UserRegistration_Company_Fop':
        ttt = s_company_fop()
    elif opt == 'Login_after_full_registration':
        ttt = s_login_after_full_registration(options.g, bro)
    elif opt == 'CreateAccount':
        ttt = s_createAccount_billing()
    elif opt == 'CheckReserv':
        ttt = s_checkRezerv()
    elif opt == 'CheckBalance':
        ttt = s_checkBalance()
    elif opt == 'full_billinig':
        ttt = s_full_billinig()

    if ttt is not None:
        try:
            runner.run(ttt)
        except:
            ttt.params["DB"].test_result.update(
                {"_id": ttt.params["result_id"]},
                {"$set": {"test_result": "FAILED"}})
        finally:
            if "DB" in ttt.params:
                ttt.params["DB"].test_result.update(
                    {"_id": ttt.params["result_id"]},
                    {"$set": {"test_result": "PASSED"}})