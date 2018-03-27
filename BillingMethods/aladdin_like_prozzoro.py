import requests
import json
import unittest


from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from Aladdin.Accounting.decorators.StoreTestResult import add_res_to_DB


class TestAladdinLikeProzorro(ParamsTestCase):
    @add_res_to_DB(test_name='get_balance_positive')
    def test_01_get_balance_positive(self):
        par = self.parent_suite.suite_params["par"]["test_01"]
        req = requests.get(par["url"], params=par)
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

    @add_res_to_DB(test_name="reserve_balance_positive")
    def test_04_reserve_balance_positive(self):
        par = self.params["par"]["test_04"]
        #par["siteType"] = self.params["siteType"]
        req = requests.post(par["url"], data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertEqual(req.status_code, 200, "Метод Reserve не отработал. Средства не зарезервировались")

    @add_res_to_DB(test_name="reserve_balance_tender_id_is_null_negative")
    def test_05_reserve_balance_tender_id_is_null_negative(self):
        par = self.parent_suite.suite_params["par"]["test_05"]
        req = requests.post(par["url"], data=json.dumps(par), headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400, "Метод Reserve отработал с нулевым тендером. Ожидаемый статус-код - 400.")

    @add_res_to_DB(test_name="reserve_balance_total_money_is_zero_positive")
    def test_06_reserve_balance_total_money_is_zero_positive(self):
        par = self.parent_suite.suite_params["par"]["test_06"]
        req = requests.post(par["url"], data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertEqual(req.status_code, 200,
                         "Метод Reserve не отработал. Не прошло резервирование с нулевым балансом.")

    @add_res_to_DB(test_name="return_monies_positive")
    def test_07_return_monies_positive(self):
        # резервирование
        par = self.parent_suite.suite_params["par"]["test_07_1"]
        req_rez = requests.post(par["url"], data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertEqual(req_rez.status_code, 200, "Метод Reserve не отработал. Средства не зарезервировались")

        par = self.parent_suite.suite_params["par"]["test_07"]
        req = requests.post(par["url"], data=json.dumps(par), headers= {"content-type": "application/json"})
        self.assertEqual(req.status_code, 200, "Метод ReturnMonies не отработал. Средства не вернулись.")

    @add_res_to_DB(test_name="return_monies_without_reserve")
    #@unittest.skip("Без предварительного резерва отвечает 200, BUG 5603")
    def test_08_return_monies_without_reserve_negative(self):
        par = self.parent_suite.suite_params["par"]["test_08"]
        req = requests.post(par["url"], data=json.dumps(par), headers= {"content-type": "application/json"})
        self.assertEqual(req.status_code, 400, "Метод ReturnMonies не отработал. Средства не вернулись.")

    @add_res_to_DB(test_name="return_monies_tender_is_null_negative")
    def test_09_return_monies_tender_is_null_negative(self):
        # резервирование
        par = self.parent_suite.suite_params["par"]["test_09_1"]
        req_rez = requests.post(par["url"], data=json.dumps(par),
                                headers={"content-type": "application/json"})
        self.assertEqual(req_rez.status_code, 200, "Метод Reserve не отработал. Средства не зарезервировались")
        #Возврат
        par = self.parent_suite.suite_params["par"]["test_09"]
        req = requests.post(par["url"], data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400, "Метод ReturnMonies отработал с нулевым тендером. Ожидаемый статус-код - 400.")

    @add_res_to_DB(test_name="return_monies_error_negative")
    def test_10_return_monies_error_negative(self):  #передача json без lotId, tenderId
        #резервирование
        par = self.parent_suite.suite_params["par"]["test_10_1"]
        req_rez = requests.post(par["url"], data=json.dumps(par),
                                headers={"content-type": "application/json"})
        self.assertEqual(req_rez.status_code, 200, "Метод Reserve не отработал. Средства не зарезервировались")

        #возврат средств
        par = self.parent_suite.suite_params["par"]["test_10"]
        req = requests.post(par["url"], data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200)
        self.assertEqual(req.status_code, 400, "Метод ReturnMonies отработал без параметра \"tenderId\". Ожидаемый статус-код - 400")


    #@unittest.skip("Не работает метод WriteOffMoney после резервирования при siteType: 2, BUG 5701")
    @add_res_to_DB(test_name="return_monies_by_company_uuid_positive")
    def test_11_return_monies_by_company_uuid_positive(self):
        #резервирование
        par = self.parent_suite.suite_params["par"]["test_11_1"]
        req_rez = requests.post(par["url"], data=json.dumps(par),
                                headers={"content-type": "application/json"})
        self.assertEqual(req_rez.status_code, 200, "Метод Reserve не отработал. Средства не зарезервировались")

        #списание
        par = self.parent_suite.suite_params["par"]["test_11_2"]
        req_wr = requests.post(par["url"], data=json.dumps(par),
                               headers={"content-type": "application/json"})
        self.assertEqual(req_wr.status_code, 200, "Метод WriteOffMoney не отработал. Средства не списались")

        #возврат после списания
        par = self.parent_suite.suite_params["par"]["test_11"]
        req = requests.post(par["url"], data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertEqual(req.status_code, 200, "Метод WriteOffMoney не отработал. Средства не вернулись после списания")

    @add_res_to_DB(test_name="return_monies_by_company_uuid_tender_is_null_negative")
    def test_12_return_monies_by_company_uuid_tender_is_null_negative(self):
        # резервирование
        par = self.parent_suite.suite_params["par"]["test_12_1"]
        req_rez = requests.post(par["url"], data=json.dumps(par),
                                headers={"content-type": "application/json"})
        self.assertEqual(req_rez.status_code, 200, "Метод Reserve не отработал. Средства не зарезервировались")
        #возврат средств после списания
        par = self.parent_suite.suite_params["par"]["test_12"]
        req = requests.post(par["url"], data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

    @add_res_to_DB(test_name="return_monies_by_company_uuid_error_negative")
    def test_13_return_monies_by_company_uuid_error_negative(self):
        par = self.parent_suite.suite_params["par"]["test_13"]
        req = requests.post(par["url"], data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

    #@unittest.skip("Не работает метод WriteOffMoney после резервирования при siteType: 2, BUG 5701")
    @add_res_to_DB(test_name="write_off_money_positive")
    def test_14_write_off_money_positive(self):
        # резервирование
        par = self.parent_suite.suite_params["par"]["test_14_1"]
        req_rez = requests.post(par["url"], data=json.dumps(par),
                                headers={"content-type": "application/json"})
        self.assertEqual(req_rez.status_code, 200, "Метод Reserve не отработал. Средства не зарезервировались")

        #списание
        par = self.parent_suite.suite_params["par"]["test_14"]
        req = requests.post("http://192.168.95.153:91/api/balance/WriteOffMoney", data=json.dumps(par), headers={"content-type": "application/json"})
        self.assertEqual(req.status_code, 200)

    @add_res_to_DB(test_name="write_off_money_tender_is_null_negative")
    def test_15_write_off_money_tender_is_null_negative(self):
        #резервирование
        par = self.parent_suite.suite_params["par"]["test_15_1"]
        req_rez = requests.post("http://192.168.95.153:91/api/balance/Reserve", data=json.dumps(par),
                                headers={"content-type": "application/json"})
        self.assertEqual(req_rez.status_code, 200, "Метод Reserve не отработал. Средства не зарезервировались")
        #списание
        par = self.parent_suite.suite_params["par"]["test_15"]

        req = requests.post("http://192.168.95.153:91/api/balance/WriteOffMoney", data=json.dumps(par), headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

    @add_res_to_DB(test_name="write_off_money_site_type_not_found_negative")
    def test_16_write_off_money_site_type_not_found_negative(self):
        #резервирование
        par = self.parent_suite.suite_params["par"]["test_16_1"]
        req_rez = requests.post("http://192.168.95.153:91/api/balance/Reserve", data=json.dumps(par),
                                headers={"content-type": "application/json"})
        self.assertEqual(req_rez.status_code, 200, "Метод Reserve не отработал. Средства не зарезервировались")
        #списание
        par = self.parent_suite.suite_params["par"]["test_16"]
        req = requests.post("http://192.168.95.153:91/api/balance/WriteOffMoney", data=json.dumps(par), headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

    @add_res_to_DB(test_name="write_off_money_error_negative")
    def test_17_write_off_money_error_negative(self): #json without CompanyEdrpou
        #резервирование
        par = self.parent_suite.suite_params["par"]["test_17_1"]
        req_rez = requests.post("http://192.168.95.153:91/api/balance/Reserve", data=json.dumps(par),
                                headers={"content-type": "application/json"})
        self.assertEqual(req_rez.status_code, 200, "Метод Reserve не отработал. Средства не зарезервировались")
        #списание
        par = self.parent_suite.suite_params["par"]["test_17"]
        req = requests.post("http://192.168.95.153:91/api/balance/WriteOffMoney", data=json.dumps(par),
                            headers={"content-type": "application/json"})
        #self.assertNotEquals(req.status_code, 200)
        self.assertEqual(req.status_code, 400)

    @add_res_to_DB(test_name="cancel_reserve_money_positive")
    def test_18_cancel_reserve_money_positive(self):
        # резервирование
        par = self.parent_suite.suite_params["par"]["test_18_1"]
        req = requests.post("http://192.168.95.153:91/api/balance/Reserve", data=json.dumps(par), headers={"content-type": "application/json"})
        self.assertEqual(req.status_code, 200)
        # отмена резерва
        par = self.parent_suite.suite_params["par"]["test_18"]
        req = requests.post("http://192.168.95.153:91/api/balance/CancelReserve", data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertEqual(req.status_code, 200)

    @add_res_to_DB(test_name="cancel_reserve_money_tender_id_is_null_negative")
    def test_19_cancel_reserve_money_tender_id_is_null_negative(self):
        # резервирование
        par = self.parent_suite.suite_params["par"]["test_19_1"]
        req = requests.post("http://192.168.95.153:91/api/balance/Reserve", data=json.dumps(par), headers={"content-type": "application/json"})
        self.assertEqual(req.status_code, 200)
        #отмена резерва
        par = self.parent_suite.suite_params["par"]["test_19"]

        req = requests.post("http://192.168.95.153:91/api/balance/CancelReserve", data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

    @add_res_to_DB(test_name="cancel_reserve_money_error_negative")
    def test_20_cancel_reserve_money_error_negative(self):
        #резервирование
        par = self.parent_suite.suite_params["par"]["test_20_1"]
        req = requests.post("http://192.168.95.153:91/api/balance/Reserve", data=json.dumps(par), headers={"content-type": "application/json"})
        self.assertEqual(req.status_code, 200)
        #отмена резерва
        par = self.parent_suite.suite_params["par"]["test_20"]

        req = requests.post("http://192.168.95.153:91/api/balance/CancelReserve", data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)
