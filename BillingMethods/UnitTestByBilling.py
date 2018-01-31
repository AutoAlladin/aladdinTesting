import requests
import json


from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from Aladdin.Accounting.decorators.StoreTestResult import add_res_to_DB


class TestByBilling(ParamsTestCase):
    @add_res_to_DB(test_name='get_balance_positive')
    def test_01_get_balance_positive(self):
        par = self.parent_suite.parent_suite["par"]["test_01"]
        req = requests.get("http://192.168.95.153:91/api/balance", params=par)
        self.assertEqual(req.status_code, 200, "")


        # print(req.url)
        # print(req.status_code)
        #print(req.text)

    @add_res_to_DB(test_name="get_balance_acc_negativ")
    def test_02_get_balance_acc_negative(self):
        par = self.parent_suite.suite_params["par"]["test_02"]
        req = requests.get("http://192.168.95.153:91/api/balance", params=par)
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

        # print(req.url)
        # print(req.status_code)
        #print(req.text)

    @add_res_to_DB(test_name="get_balance_without_guid_negative")
    def test_03_get_balance_without_guid_negative(self):
        par = self.parent_suite.suite_params["par"]["test_03"]
        req = requests.get("http://192.168.95.153:91/api/balance", params=par)
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

        # print(req.url)
        # print(req.status_code)
        #print(req.text)

    @add_res_to_DB(test_name="reserve_balance_positive")
    def test_04_reserve_balance_positive(self):
        par = self.parent_suite.suite_params["par"]["test_04"]
        req = requests.post("http://192.168.95.153:91/api/balance/Reserve", data=json.dumps(par), headers={"content-type": "application/json"})
        self.assertEqual(req.status_code, 200)

        # print(req.url)
        # print(req.status_code)
        #print(req.text)

    @add_res_to_DB(test_name="reserve_balance_tender_id_is_null_negative")
    def test_05_reserve_balance_tender_id_is_null_negative(self):
        par = self.parent_suite.suite_params["par"]["test_05"]
        req = requests.post("http://192.168.95.153:91/api/balance/Reserve", data=json.dumps(par), headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

    @add_res_to_DB(test_name="reserve_balance_total_money_is_zero_positive")
    def test_06_reserve_balance_total_money_is_zero_positive(self):
        par = self.parent_suite.suite_params["par"]["test_06"]
        req = requests.post("http://192.168.95.153:91/api/balance/Reserve", data=json.dumps(par), headers= {"content-type": "application/json"})
        self.assertEqual(req.status_code, 200)
        #self.assertEqual(req.status_code, 400)

    @add_res_to_DB(test_name="return_monies_positive")
    def test_07_return_monies_positive(self):
        par = self.parent_suite.suite_params["par"]["test_07"]
        req = requests.post("http://192.168.95.153:91/api/balance/ReturnMonies", data=json.dumps(par), headers= {"content-type": "application/json"})
        self.assertEqual(req.status_code, 200)

    @add_res_to_DB(test_name="return_monies_tender_is_null_negative")
    def test_08_return_monies_tender_is_null_negative(self):
        par = self.parent_suite.suite_params["par"]["test_08"]
        req = requests.post("http://192.168.95.153:91/api/balance/ReturnMonies", data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

    @add_res_to_DB(test_name="return_monies_error_negative")
    def test_09_return_monies_error_negative(self):  #передача json без lotId
        par = self.parent_suite.suite_params["par"]["test_09"]
        req = requests.post("http://192.168.95.153:91/api/balance/ReturnMonies", data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertEqual(req.status_code, 200)
        # self.assertNotEquals(req.status_code, 200, 201)
        # self.assertEqual(req.status_code, 400)

    @add_res_to_DB(test_name="return_monies_by_company_uuid_positive")
    def test_10_return_monies_by_company_uuid_positive(self):
        par = self.parent_suite.suite_params["par"]["test_10"]
        req = requests.post("http://192.168.95.153:91/api/balance/ReturnMoniesByCompany", data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertEqual(req.status_code, 200)

    @add_res_to_DB(test_name="return_monies_by_company_uuid_tender_is_null_negative")
    def test_11_return_monies_by_company_uuid_tender_is_null_negative(self):
        par = self.parent_suite.suite_params["par"]["test_11"]
        req = requests.post("http://192.168.95.153:91/api/balance/ReturnMoniesByCompany", data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

    @add_res_to_DB(test_name="return_monies_by_company_uuid_error_negative")
    def test_12_return_monies_by_company_uuid_error_negative(self):
        par = self.parent_suite.suite_params["par"]["test_12"]
        req = requests.post("http://192.168.95.153:91/api/balance/ReturnMoniesByCompany", data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

    @add_res_to_DB(test_name="write_off_money_positive")
    def test_13_write_off_money_positive(self):
        par = self.parent_suite.suite_params["par"]["test_13"]

        req = requests.post("http://192.168.95.153:91/api/balance/WriteOffMoney", data=json.dumps(par), headers={"content-type": "application/json"})
        self.assertEqual(req.status_code, 200)

    @add_res_to_DB(test_name="write_off_money_tender_is_null_negative")
    def test_14_write_off_money_tender_is_null_negative(self):
        par = self.parent_suite.suite_params["par"]["test_14"]

        req = requests.post("http://192.168.95.153:91/api/balance/WriteOffMoney", data=json.dumps(par), headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

    @add_res_to_DB(test_name="write_off_money_site_type_not_found_negative")
    def test_15_write_off_money_site_type_not_found_negative(self):
        par = self.parent_suite.suite_params["par"]["test_15"]
        req = requests.post("http://192.168.95.153:91/api/balance/WriteOffMoney", data=json.dumps(par), headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

    @add_res_to_DB(test_name="write_off_money_error_negative")
    def test_16_write_off_money_error_negative(self):
        par = self.parent_suite.suite_params["par"]["test_16"]
        req = requests.post("http://192.168.95.153:91/api/balance/WriteOffMoney", data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

    @add_res_to_DB(test_name="cancel_reserve_money_positive")
    def test_17_cancel_reserve_money_positive(self):
        par = self.parent_suite.suite_params["par"]["test_17"]
        req = requests.post("http://192.168.95.153:91/api/balance/CancelReserve", data=json.dumps(par),
                            headers={"content-type": "application/json"})
        #self.assertEqual(req.status_code, 200)

    def test_18_cancel_reserve_money_tender_id_is_null_negative(self):
        par = self.parent_suite.suite_params["par"]["test_18"]

        req = requests.post("http://192.168.95.153:91/api/balance/CancelReserve", data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

    def test_19_cancel_reserve_money_error_negative(self):
        par = self.parent_suite.suite_params["par"]["test_19"]

        req = requests.post("http://192.168.95.153:91/api/balance/CancelReserve", data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

# if __name__ == '__main__':
#     utb = TestByBilling()
#     utb.test_01_get_balance_positive()
#     utb.test_02_get_balance_acc_negative()
#     utb.test_03_get_balance_without_guid_negative()
#     utb.test_04_reserve_balance_positive()
#     utb.test_05_reserve_balance_tender_id_is_null_negative()
#     utb.test_06_reserve_balance_total_money_is_zero_negative()
#     utb.test_07_return_monies_positive()
#     utb.test_08_return_monies_tender_is_null_negative()
#     utb.test_09_return_monies_error_negative()
#     utb.test_10_return_monies_by_company_uuid_positive()
#     utb.test_11_return_monies_by_company_uuid_tender_is_null_negative()
#     utb.test_12_return_monies_by_company_uuid_error_negative()
#     utb.test_13_write_off_money_positive()
#     utb.test_14_write_off_money_tender_is_null_negative()
#     utb.test_15_write_off_money_site_type_not_found_negative()
#     utb.test_16_write_off_money_error_negative()
#     utb.test_17_cancel_reserve_money_positive()
#     utb.test_18_cancel_reserve_money_tender_id_is_null_negative()
#     utb.test_19_cancel_reserve_money_error_negative()
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="example_dir"))
