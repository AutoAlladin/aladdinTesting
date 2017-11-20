import datetime
import json
import os
import time
import uuid
import unittest
from unittest import TestCase

from Aladdin.DB.billing import check_new_account

from Aladdin.Rabbit.sender import send_simple



def new_account(que, str_json,in_dic):
    send_simple(que,str_json)
    res=""
    try:
        time.sleep(7)
        # выполняем запрос на проверку наличия счета запрошеного через шину
        res= check_new_account(in_dic["new_account"]["uuid"], in_dic["new_account"]["edrpou"])

        if res.startswith("PASS"):
            in_dic["used_data"]["accounts"].append(dict(uuid=in_dic["new_account"]["uuid"],
                                                edrpou=in_dic["new_account"]["edrpou"],
                                                status="PASS"
                                                )
                                           )
        elif res.startswith("FAIL"):
            in_dic["used_data"]["accounts"].append(dict(uuid=in_dic["new_account"]["uuid"],
                                                    edrpou=in_dic["new_account"]["edrpou"],
                                                    status="FAIL"))

    except Exception as e:
        in_dic["used_data"]["accounts"].append(dict(uuid=in_dic["new_account"]["uuid"],
                                                    edrpou=in_dic["new_account"]["edrpou"],
                                                    status="FAIL",
                                                    error_msg=e.__str__()))
        raise Exception("DB " + e.__str__())
    finally:
        #  влюбом случае сохраняем попытку
        with(open(os.path.dirname(os.path.abspath(__file__)) + '\\input.json', 'w', encoding="UTF-8")) as out_dic:
            json.dump(in_dic, out_dic, indent=4, separators=(',', ': '))

    return res



#if __name__ == "__main__":
    # #  входные парамеры для теста
    # in_dic = dict()
    # with open(os.path.dirname(os.path.abspath(__file__)) + '\\input.json', 'r',
    #           encoding="UTF-8") as test_params_file:
    #     in_dic = json.load(test_params_file)
    #
    # in_dic["new_account"]["uuid"] = str(uuid.uuid4())
    # msg_create_company_account = json.dumps({'companyAccount': in_dic["new_account"] })
    # old_id = in_dic["new_account"]["uuid"]
    # old_edr = in_dic["new_account"]["edrpou"]
    #
    # try:
    #     print("new ACC, new EDR")
    #     start_test_method = datetime.datetime.now()
    #     print(new_account(que='need_create_company_account',
    #                 str_json=msg_create_company_account,
    #                 in_dic=in_dic), end='\n')
    #     final_test_method = datetime.datetime.now()
    #     print("duration",(final_test_method - start_test_method).total_seconds())
    #     print()
    # except Exception as e:
    #     print(e.__str__())
    #
    # try:
    #     in_dic["new_account"]["uuid"] = str(uuid.uuid4())
    #     in_dic["new_account"]["edrpou"] = old_edr
    #     msg_create_company_account = json.dumps({'companyAccount': in_dic["new_account"]})
    #     print("new ACC, old EDR")
    #     print(new_account(que='need_create_company_account',
    #                 str_json=msg_create_company_account,
    #                 in_dic=in_dic), end='\n\r')
    #     print()
    # except Exception as e:
    #     print(e.__str__())
    #
    # try:
    #     in_dic["new_account"]["uuid"] = old_id
    #     in_dic["new_account"]["edrpou"] =str(int(old_edr)+1)
    #     msg_create_company_account = json.dumps({'companyAccount': in_dic["new_account"]})
    #     print("old ACC, new EDR")
    #     print(new_account(que='need_create_company_account',
    #                       str_json=msg_create_company_account,
    #                       in_dic=in_dic), end='\n\r')
    #     print()
    # except Exception as e:
    #     print(e.__str__())
    #
    # try:
    #     in_dic["new_account"]["uuid"] = old_id
    #     in_dic["new_account"]["edrpou"]=old_edr
    #     msg_create_company_account = json.dumps({'companyAccount': in_dic["new_account"]})
    #     print("old ACC, old EDR")
    #     print(new_account(que='need_create_company_account',
    #                 str_json=msg_create_company_account,
    #                 in_dic=in_dic), end='\n\r')
    #     print()
    # except Exception as e:
    #     print(e.__str__())
    #
    # try:
    #     in_dic["new_account"]["uuid"] = '000000000'
    #     in_dic["new_account"]["edrpou"]= old_edr =str(int(old_edr)+1)
    #     msg_create_company_account = json.dumps({'companyAccount': in_dic["new_account"]})
    #     print("fail ACC, new EDR")
    #     print(new_account(que='need_create_company_account',
    #                 str_json=msg_create_company_account,
    #                 in_dic=in_dic), end='\n')
    #     print()
    # except Exception as e:
    #     print(e.__str__())
    #
    # try:
    #     in_dic["new_account"]["uuid"] = old_id = str(uuid.uuid4())
    #     msg_create_company_account = json.dumps({'companyAccount': {"uuid": old_id, "edrpou": "123456"}})
    #     print("new ACC, fail EDR < 8")
    #     print(new_account(que='need_create_company_account',
    #                 str_json=msg_create_company_account,
    #                 in_dic=in_dic), end='\n')
    #     print()
    # except Exception as e:
    #     print(e.__str__())
    #
    # try:
    #     msg_create_company_account = json.dumps({'companyAccount': {"uuid": old_id, "edrpou": "123456789012345678"}})
    #     print("new ACC, fail EDR >10")
    #     print(new_account(que='need_create_company_account',
    #                 str_json=msg_create_company_account,
    #                 in_dic=in_dic), end='\n')
    #     print()
    # except Exception as e:
    #     print(e.__str__())



class CreateAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.in_dic = dict()
        with open(os.path.dirname(os.path.abspath(__file__)) + '\\input.json', 'r',
                encoding="UTF-8") as test_params_file:
            cls.in_dic = json.load(test_params_file)

        cls.in_dic["new_account"]["uuid"] = str(uuid.uuid4())
        cls.msg_create_company_account = json.dumps({'companyAccount': cls.in_dic["new_account"]})
        cls.old_id = cls.in_dic["new_account"]["uuid"]
        cls.old_edr = cls.in_dic["new_account"]["edrpou"]



    def test_01_new_UUID_new_EDR(self):
        res = new_account(que='need_create_company_account',
                    str_json=self.msg_create_company_account,
                    in_dic=self.in_dic)

        self.start_test_method = datetime.datetime.now()
        self.final_test_method = datetime.datetime.now()
        print("duration", (self.final_test_method - self.start_test_method).total_seconds())
        print(res)

        self.assertEqual(res[0:4], "PASS")


    def test_02_new_UUID_old_EDR(self):
        self.in_dic["new_account"]["uuid"] = str(uuid.uuid4())
        self.in_dic["new_account"]["edrpou"] = self.old_edr
        self.msg_create_company_account = json.dumps({'companyAccount': self.in_dic["new_account"]})

        res = new_account(que='need_create_company_account',
                    str_json=self.msg_create_company_account,
                    in_dic=self.in_dic)

        self.start_test_method = datetime.datetime.now()
        self.final_test_method = datetime.datetime.now()
        print("duration", (self.final_test_method - self.start_test_method).total_seconds())
        print(res)

        self.assertEqual(res[0:4], "PASS")


    def test_03_old_UUID_old_EDR(self):
        self.in_dic["new_account"]["uuid"] = self.old_id
        self.in_dic["new_account"]["edrpou"]=self.old_edr
        self.msg_create_company_account = json.dumps({'companyAccount': self.in_dic["new_account"]})

        res = new_account(que='need_create_company_account',
                    str_json=self.msg_create_company_account,
                    in_dic=self.in_dic)
        self.start_test_method = datetime.datetime.now()
        self.final_test_method = datetime.datetime.now()
        print("duration", (self.final_test_method - self.start_test_method).total_seconds())
        print(res)

        self.assertEqual(res[0:4], "PASS")

    def test_04_fail_UUID_new_EDR(self):
        self.in_dic["new_account"]["uuid"] = '000000000'
        self.in_dic["new_account"]["edrpou"]=self.old_edr

        self.msg_create_company_account = json.dumps({'companyAccount': self.in_dic["new_account"]})


        res = new_account(que='need_create_company_account',
                    str_json=self.msg_create_company_account,
                    in_dic=self.in_dic)
        self.start_test_method = datetime.datetime.now()
        self.final_test_method = datetime.datetime.now()
        print("duration", (self.final_test_method - self.start_test_method).total_seconds())
        print(res)

        self.assertEqual(res[0:4], "PASS")

    def test_05_new_UUID_less_EDR(self):
        self.in_dic["new_account"]["uuid"] = str(uuid.uuid4())
        self.msg_create_company_account = json.dumps({'companyAccount': {"uuid": self.old_id, "edrpou": "123456"}})

        res = new_account(que='need_create_company_account',
                    str_json=self.msg_create_company_account,
                    in_dic=self.in_dic)
        self.start_test_method = datetime.datetime.now()
        self.final_test_method = datetime.datetime.now()
        print("duration", (self.final_test_method - self.start_test_method).total_seconds())
        print(res)

        TestCase.assertEqual(res[0:4], "PASS")

    def test_06_new_UUID_more_EDR(self):
        self.in_dic["new_account"]["uuid"] = str(uuid.uuid4())
        self.msg_create_company_account = json.dumps({'companyAccount': {"uuid": self.old_id, "edrpou": "123456789012345678"}})

        res = new_account(que='need_create_company_account',
                    str_json=self.msg_create_company_account,
                    in_dic=self.in_dic)
        self.start_test_method = datetime.datetime.now()
        self.final_test_method = datetime.datetime.now()
        print("duration", (self.final_test_method - self.start_test_method).total_seconds())
        print(res)

        self.assertEqual(res[0:4], "PASS")


