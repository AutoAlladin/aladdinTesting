import requests
import json
import unittest
import HtmlTestRunner


class UnitTestByBilling(unittest.TestCase):
    def test_1_get_balance_positive(self):
        par = {"companyUuid": "68a14f2a-c5a2-4a76-9d86-88c2ffad742b"}
        req = requests.get("http://192.168.95.153:91/api/balance", params=par)
        self.assertEqual(req.status_code, 200)


        print(req.url)
        print(req.status_code)
        #print(req.text)


    def test_2_get_balance_acc_negative(self):
        par = {"companyUuid": "68a14f2a-c5a2-4a76-9d86-88c2ffad7400"}
        req = requests.get("http://192.168.95.153:91/api/balance", params=par)
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

        print(req.url)
        print(req.status_code)
        #print(req.text)

    def test_3_get_balance_without_guid_negative(self):
        par = {"companyUuid": ""}
        req = requests.get("http://192.168.95.153:91/api/balance", params=par)
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

        print(req.url)
        print(req.status_code)
        #print(req.text)

    def test_4_reserve_balance_positive(self):
        par = {"tenderId": 26285,
             "lotId": 11,
             "amount": 1000.0,
             "currency": "ГРН",
             "descriptions": "Тендер: Соль таблетированная 22 000 кг. Лот №1 Позиції: Сіль таблетована   ",
             "totalMoney": 511.5,
             "companyUuid": "68A14F2A-C5A2-4A76-9D86-88C2FFAD742B",
             "serviceIdentifierUuid": "00e525f3-420b-4d76-b538-d0efc7957cd2",
             "siteType": "1"}
        req = requests.post("http://192.168.95.153:91/api/balance/Reserve", data=json.dumps(par), headers={"content-type": "application/json"})
        self.assertEqual(req.status_code, 200)

        print(req.url)
        print(req.status_code)
        #print(req.text)


    def test_5_reserve_balance_tender_id_is_null_negative(self):
        par = {"tenderId": 0,
             "lotId": 0,
             "amount": 1000.0,
             "currency": "ГРН",
             "descriptions": "Тендер: Соль таблетированная 22 000 кг. Лот №1 Позиції: Сіль таблетована   ",
             "totalMoney": 511.5,
             "companyUuid": "68A14F2A-C5A2-4A76-9D86-88C2FFAD742B",
             "serviceIdentifierUuid": "00e525f3-420b-4d76-b538-d0efc7957cd2",
             "siteType": "1"}
        req = requests.post("http://192.168.95.153:91/api/balance/Reserve", data=json.dumps(par), headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

    def test_6_reserve_balance_total_money_is_zero_negative(self):
        par = {"tenderId": 26285,
             "lotId": 11,
             "amount": 1000.0,
             "currency": "ГРН",
             "descriptions": "Тендер: Соль таблетированная 22 000 кг. Лот №1 Позиції: Сіль таблетована   ",
             "totalMoney": 511.5,
             "companyUuid": "0bc3cdd5-11c7-4aa6-a249-591c0b197f24",  #учетка с нулевым балансом
             "serviceIdentifierUuid": "00e525f3-420b-4d76-b538-d0efc7957cd2",
             "siteType": "1"}
        req = requests.post("http://192.168.95.153:91/api/balance/Reserve", data=json.dumps(par), headers= {"content-type": "application/json"})
        self.assertNotEqual(req.status_code, 200)
        #self.assertEqual(req.status_code, 400)

    def test_7_return_monies_positive(self):
        par = {"tenderId": 26285,
             "lotId": 11,
             "amount": 1000.0,
             "currency": "ГРН",
             "descriptions": "Тендер: Соль таблетированная 22 000 кг. Лот №1 Позиції: Сіль таблетована   ",
             "totalMoney": 511.5,
             "companyUuid": "0bc3cdd5-11c7-4aa6-a249-591c0b197f24",  #учетка с нулевым балансом
             "serviceIdentifierUuid": "00e525f3-420b-4d76-b538-d0efc7957cd2",
             "siteType": "1"}
        req = requests.post("http://192.168.95.153:91/api/balance/ReturnMonies", data=json.dumps(par), headers= {"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)




    def return_monies_by_company_uuid(self):
        pass

    def write_off_money(self):
        pass

    def cancel_reserve_money(self):
        pass


if __name__ == '__main__':
    utb = UnitTestByBilling()
    utb.test_1_get_balance_positive()
    utb.test_2_get_balance_acc_negative()
    utb.test_3_get_balance_without_guid_negative()
    utb.test_4_reserve_balance_positive()
    utb.test_5_reserve_balance_tender_id_is_null_negative()
    utb.test_6_reserve_balance_total_money_is_zero_negative()
    utb.test_7_return_monies_positive()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="example_dir"))
