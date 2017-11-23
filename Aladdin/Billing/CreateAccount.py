import datetime
import json
import os
import time
import uuid
import unittest
from unittest import TestCase

from Aladdin.Accounting.decorators.ParamsTestSuite import ParamsTestSuite
from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from Aladdin.DB.billing import check_new_account
#from Aladdin.TestList import *
from Aladdin.Rabbit.sender import send_simple



def new_account(que, str_json, dic):
    send_simple(que,str_json)
    res=""
    try:
        time.sleep(7)
        # выполняем запрос на проверку наличия счета запрошеного через шину
        res= check_new_account(dic["new_account"]["uuid"], dic["new_account"]["edrpou"])

        if res.startswith("PASS"):
            dic["used_data"]["accounts"].append(dict(uuid=dic["new_account"]["uuid"],
                                                     edrpou=dic["new_account"]["edrpou"],
                                                     status="PASS"
                                                     )
                                                )
        elif res.startswith("FAIL"):
            dic["used_data"]["accounts"].append(dict(uuid=dic["new_account"]["uuid"],
                                                     edrpou=dic["new_account"]["edrpou"],
                                                     status="FAIL"))

    except Exception as e:
        dic["used_data"]["accounts"].append(dict(uuid=dic["new_account"]["uuid"],
                                                 edrpou=dic["new_account"]["edrpou"],
                                                 status="FAIL",
                                                 error_msg=e.__str__()))
        raise Exception("DB " + e.__str__())
    finally:
        #  влюбом случае сохраняем попытку
        with(open(os.path.dirname(os.path.abspath(__file__)) + '\\input.json', 'w', encoding="UTF-8")) as out_dic:
            json.dump(dic, out_dic, indent=4, separators=(',', ': '))

    return res



class CreateAccount(ParamsTestCase):
    #@classmethod
    #def setUpClass(cls):
    def test_01_new_UUID_new_EDR(self):
        self.start_test_method = datetime.datetime.now()
        res = new_account(que='need_create_company_account',
                          str_json=self.params["msg_create_company_account"],
                          dic=self.params["in_dic"])

        print("duration", (datetime.datetime.now() - self.start_test_method).total_seconds())
        self.assertEqual(res[0:4], "PASS")


    def test_02_new_UUID_old_EDR(self):
        self.start_test_method = datetime.datetime.now()
        self.params["in_dic"]["new_account"]["uuid"] = str(uuid.uuid4())
        self.params["in_dic"]["new_account"]["edrpou"] = self.params["old_edr"]
        self.params["msg_create_company_account"] = json.dumps({'companyAccount': self.params["in_dic"]["new_account"]})

        res = new_account(que='need_create_company_account',
                          str_json=self.params["msg_create_company_account"],
                          dic=self.params["in_dic"])

        print("duration", (datetime.datetime.now() - self.start_test_method).total_seconds())
        self.assertEqual(res[0:6], "FAILED")


    def test_03_old_UUID_old_EDR(self):
        self.start_test_method = datetime.datetime.now()
        self.params["in_dic"]["new_account"]["uuid"] = self.params["old_id"]
        self.params["in_dic"]["new_account"]["edrpou"] = self.params["old_edr"]
        self.params["msg_create_company_account"] = json.dumps({'companyAccount': self.params["in_dic"]["new_account"]})

        res = new_account(que='need_create_company_account',
                          str_json=self.params["msg_create_company_account"],
                          dic=self.params["in_dic"])

        print("duration", (datetime.datetime.now() - self.start_test_method).total_seconds())
        self.assertEqual(res[0:4], "PASS")


    def test_04_fail_UUID_new_EDR(self):
        self.start_test_method = datetime.datetime.now()
        self.params["in_dic"]["new_account"]["uuid"] = '000000000'
        self.params["in_dic"]["new_account"]["edrpou"]=self.params["old_edr"]
        self.params["msg_create_company_account"] = json.dumps({'companyAccount': self.params["in_dic"]["new_account"]})


        res = new_account(que='need_create_company_account',
                          str_json=self.params["msg_create_company_account"],
                          dic=self.params["in_dic"])

        print("duration", (datetime.datetime.now() - self.start_test_method).total_seconds())
        self.assertEqual(res[0:6], "FAILED")

    def test_05_new_UUID_less_EDR(self):
        start_test_method = datetime.datetime.now()
        self.params["in_dic"]["new_account"]["uuid"] = str(uuid.uuid4())
        self.params["msg_create_company_account"] = json.dumps({'companyAccount': {"uuid": self.params["old_id"], "edrpou": "123456"}})

        res = new_account(que='need_create_company_account',
                          str_json=self.params["msg_create_company_account"],
                          dic=self.params["in_dic"])

        print("duration", (datetime.datetime.now() - start_test_method).total_seconds())
        self.assertEqual(res[0:6], "FAILED")

    def test_06_new_UUID_more_EDR(self):
        start_test_method = datetime.datetime.now()
        self.params["in_dic"]["new_account"]["uuid"] = str(uuid.uuid4())
        self.params["msg_create_company_account"] = json.dumps({'companyAccount': {"uuid": self.params["old_id"], "edrpou": "123456789012345678"}})

        res = new_account(que='need_create_company_account',
                          str_json=self.params["msg_create_company_account"],
                          dic=self.params["in_dic"])

        print("duration", (datetime.datetime.now() - start_test_method).total_seconds())
        self.assertEqual(res[0:6], "FAILED")


