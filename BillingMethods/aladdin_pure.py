import requests
import json
import unittest


from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from Aladdin.Accounting.decorators.StoreTestResult import add_res_to_DB


class TestAladdinPure(ParamsTestCase):
    @add_res_to_DB(test_name='get_balance_positive')
    def test_01_get_balance_positive(self):
        par = self.parent_suite.suite_params["par"]["test_01"]
        url = par.pop("url")
        req = requests.get(url, params=par)
        self.assertEqual(req.status_code, 200, "Метод balance не отработал")

    @add_res_to_DB(test_name="get_balance_acc_negativ")
    def test_02_get_balance_acc_negative(self):
        par = self.parent_suite.suite_params["par"]["test_02"]
        req = requests.get(par["url"], params=par)
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400, "Метод balance отработал с несуществующим гуидом. Ожидаемый статус-код - 400.")

    @add_res_to_DB(test_name="get_balance_without_guid_negative")
    def test_03_get_balance_without_guid_negative(self):
        par = self.parent_suite.suite_params["par"]["test_03"]
        req = requests.get(par["url"], params=par)
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400, "Метод balance отработал без гуида. Ожидаемый статус-код - 400.")

    @add_res_to_DB(test_name="write_off_money_positive")
    def test_14_write_off_money_positive(self):
        # резервирование
        # par = self.parent_suite.suite_params["par"]["test_14_1"]
        # req_rez = requests.post("http://192.168.95.153:91/api/balance/Reserve", data=json.dumps(par),
        #                         headers={"content-type": "application/json"})
        # self.assertEqual(req_rez.status_code, 200, "Метод Reserve не отработал. Средства не зарезервировались")

        #списание
        par = self.parent_suite.suite_params["par"]["test_14"]
        req = requests.post(par["url"], data=json.dumps(par), headers={"content-type": "application/json"})
        self.assertEqual(req.status_code, 200)

    @add_res_to_DB(test_name="write_off_money_tender_is_null_negative")
    def test_15_write_off_money_tender_is_null_negative(self):
        #резервирование
        # par = self.parent_suite.suite_params["par"]["test_15_1"]
        # req_rez = requests.post("http://192.168.95.153:91/api/balance/Reserve", data=json.dumps(par),
        #                         headers={"content-type": "application/json"})
        # self.assertEqual(req_rez.status_code, 200, "Метод Reserve не отработал. Средства не зарезервировались")
        #списание
        par = self.parent_suite.suite_params["par"]["test_15"]

        req = requests.post(par["url"], data=json.dumps(par), headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

    @add_res_to_DB(test_name="write_off_money_site_type_not_found_negative")
    def test_16_write_off_money_site_type_not_found_negative(self):
        #резервирование
        # par = self.parent_suite.suite_params["par"]["test_16_1"]
        # req_rez = requests.post("http://192.168.95.153:91/api/balance/Reserve", data=json.dumps(par),
        #                         headers={"content-type": "application/json"})
        # self.assertEqual(req_rez.status_code, 200, "Метод Reserve не отработал. Средства не зарезервировались")
        #списание
        par = self.parent_suite.suite_params["par"]["test_16"]
        req = requests.post(par["url"], data=json.dumps(par), headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)


    @add_res_to_DB(test_name="write_off_money_error_negative")
    def test_17_write_off_money_error_negative(self):
        # json without CompanyEdrpou
        # резервирование
        # par = self.parent_suite.suite_params["par"]["test_17_1"]
        # req_rez = requests.post("http://192.168.95.153:91/api/balance/Reserve", data=json.dumps(par),
        #                         headers={"content-type": "application/json"})
        # self.assertEqual(req_rez.status_code, 200, "Метод Reserve не отработал. Средства не зарезервировались")
        # списание
        par = self.parent_suite.suite_params["par"]["test_17"]
        req = requests.post(par["url"], data=json.dumps(par),
                            headers={"content-type": "application/json"})
        # self.assertNotEquals(req.status_code, 200)
        self.assertEqual(req.status_code, 400)

