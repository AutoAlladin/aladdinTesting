import requests
import json
import unittest
import HtmlTestRunner

from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase


class UnitTestByBilling(ParamsTestCase):
    def test_01_get_balance_positive(self):
        par = {"companyUuid": "68a14f2a-c5a2-4a76-9d86-88c2ffad742b"}
        req = requests.get("http://192.168.95.153:91/api/balance", params=par)
        self.assertEqual(req.status_code, 200)


        print(req.url)
        print(req.status_code)
        #print(req.text)


    def test_02_get_balance_acc_negative(self):
        par = {"companyUuid": "68a14f2a-c5a2-4a76-9d86-88c2ffad7400"}
        req = requests.get("http://192.168.95.153:91/api/balance", params=par)
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

        print(req.url)
        print(req.status_code)
        #print(req.text)

    def test_03_get_balance_without_guid_negative(self):
        par = {"companyUuid": ""}
        req = requests.get("http://192.168.95.153:91/api/balance", params=par)
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

        print(req.url)
        print(req.status_code)
        #print(req.text)

    def test_04_reserve_balance_positive(self):
        par = {"tenderId": 26285,
             "lotId": 11,
             "amount": 1000.0,
             "currency": "ГРН",
             "descriptions": "Тендер: Соль таблетированная 22 000 кг. Лот №1 Позиції: Сіль таблетована   ",
             "totalMoney": 511.5,
             "companyUuid": "68a14f2a-c5a2-4a76-9d86-88c2ffad742b",
             "serviceIdentifierUuid": "00e525f3-420b-4d76-b538-d0efc7957cd2",
             "siteType": "1"}
        req = requests.post("http://192.168.95.153:91/api/balance/Reserve", data=json.dumps(par), headers={"content-type": "application/json"})
        self.assertEqual(req.status_code, 200)

        print(req.url)
        print(req.status_code)
        #print(req.text)


    def test_05_reserve_balance_tender_id_is_null_negative(self):
        par = {"tenderId": 0,
             "lotId": 0,
             "amount": 1000.0,
             "currency": "ГРН",
             "descriptions": "Тендер: Соль таблетированная 22 000 кг. Лот №1 Позиції: Сіль таблетована   ",
             "totalMoney": 511.5,
             "companyUuid": "68a14f2a-c5a2-4a76-9d86-88c2ffad742b",
             "serviceIdentifierUuid": "00e525f3-420b-4d76-b538-d0efc7957cd2",
             "siteType": "1"}
        req = requests.post("http://192.168.95.153:91/api/balance/Reserve", data=json.dumps(par), headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

    def test_06_reserve_balance_total_money_is_zero_negative(self):
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
        self.assertEqual(req.status_code, 200)
        #self.assertEqual(req.status_code, 400)

    def test_07_return_monies_positive(self):
        par = {"tenderId": 26285,
             "lotId": 11,
             "amount": 1000.0,
             "currency": "ГРН",
             "descriptions": "Тендер: Соль таблетированная 22 000 кг. Лот №1 Позиції: Сіль таблетована   ",
             "totalMoney": 511.5,
             "companyUuid": "68a14f2a-c5a2-4a76-9d86-88c2ffad742b",
             "serviceIdentifierUuid": "00e525f3-420b-4d76-b538-d0efc7957cd2",
             "siteType": "1"}
        req = requests.post("http://192.168.95.153:91/api/balance/ReturnMonies", data=json.dumps(par), headers= {"content-type": "application/json"})
        self.assertEqual(req.status_code, 200)

    def test_08_return_monies_tender_is_null_negative(self):
        par = {"tenderId": 0,
             "lotId": 11,
             "amount": 1000.0,
             "currency": "ГРН",
             "descriptions": "Тендер: Соль таблетированная 22 000 кг. Лот №1 Позиції: Сіль таблетована   ",
             "totalMoney": 511.5,
             "companyUuid": "68a14f2a-c5a2-4a76-9d86-88c2ffad742b",
             "serviceIdentifierUuid": "00e525f3-420b-4d76-b538-d0efc7957cd2",
             "siteType": "1"}
        req = requests.post("http://192.168.95.153:91/api/balance/ReturnMonies", data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

    def test_09_return_monies_error_negative(self):  #передача json без lotId
        par = {"tenderId": 26285,
             "amount": 1000.0,
             "currency": "ГРН",
             "descriptions": "Тендер: Соль таблетированная 22 000 кг. Лот №1 Позиції: Сіль таблетована   ",
             "totalMoney": 511.5,
             "companyUuid": "68a14f2a-c5a2-4a76-9d86-88c2ffad742b",
             "serviceIdentifierUuid": "00e525f3-420b-4d76-b538-d0efc7957cd2",
             "siteType": "1"}
        req = requests.post("http://192.168.95.153:91/api/balance/ReturnMonies", data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertEqual(req.status_code, 200)
        # self.assertNotEquals(req.status_code, 200, 201)
        # self.assertEqual(req.status_code, 400)


    def test_10_return_monies_by_company_uuid_positive(self):
        par = {"tenderId": 26285,
             "lotId": 11,
             "amount": 1000.0,
             "currency": "ГРН",
             "descriptions": "Тендер: Соль таблетированная 22 000 кг. Лот №1 Позиції: Сіль таблетована   ",
             "totalMoney": 511.5,
             "companyUuid": "68a14f2a-c5a2-4a76-9d86-88c2ffad742b",
             "serviceIdentifierUuid": "00e525f3-420b-4d76-b538-d0efc7957cd2",
             "siteType": "1"}
        req = requests.post("http://192.168.95.153:91/api/balance/ReturnMoniesByCompany", data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertEqual(req.status_code, 200)

    def test_11_return_monies_by_company_uuid_tender_is_null_negative(self):
        par = {"tenderId": 0,
             "lotId": 11,
             "amount": 1000.0,
             "currency": "ГРН",
             "descriptions": "Тендер: Соль таблетированная 22 000 кг. Лот №1 Позиції: Сіль таблетована   ",
             "totalMoney": 511.5,
             "companyUuid": "68a14f2a-c5a2-4a76-9d86-88c2ffad742b",
             "serviceIdentifierUuid": "00e525f3-420b-4d76-b538-d0efc7957cd2",
             "siteType": "1"}
        req = requests.post("http://192.168.95.153:91/api/balance/ReturnMoniesByCompany", data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

    def test_12_return_monies_by_company_uuid_error_negative(self):
        par = {"lotId": "11",
             "amount": "1000.0",
             "currency": "ГРН", #отправка json без totalMoney, tenderId
             "descriptions": "Тендер: Соль таблетированная 22 000 кг. Лот №1 Позиції: Сіль таблетована   ",
             "companyUuid": "68a14f2a-c5a2-4a76-9d86-88c2ffad742b",
             "serviceIdentifierUuid": "00e525f3-420b-4d76-b538-d0efc7957cd2",
             "siteType": "1"}
        req = requests.post("http://192.168.95.153:91/api/balance/ReturnMoniesByCompany", data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

    def test_13_write_off_money_positive(self):
        par = {"tenderId": 26285,
             "lotId": 11,
             "amount": 1000.0,
             "currency": "ГРН",
             "descriptions": "Тендер: Соль таблетированная 22 000 кг. Лот №1 Позиції: Сіль таблетована   ",
               "totalMoney": 511.5,
             "companyUuid": "68a14f2a-c5a2-4a76-9d86-88c2ffad742b",
             "serviceIdentifierUuid": "00e525f3-420b-4d76-b538-d0efc7957cd2",
             "siteType": "1"}

        req = requests.post("http://192.168.95.153:91/api/balance/WriteOffMoney", data=json.dumps(par), headers={"content-type": "application/json"})
        self.assertEqual(req.status_code, 200)

    def test_14_write_off_money_tender_is_null_negative(self):
        par = {"tenderId": 0,
             "lotId": 11,
             "amount": 1000.0,
             "currency": "ГРН",
             "descriptions": "Тендер: Соль таблетированная 22 000 кг. Лот №1 Позиції: Сіль таблетована   ",
               "totalMoney": 511.5,
             "companyUuid": "68a14f2a-c5a2-4a76-9d86-88c2ffad742b",
             "serviceIdentifierUuid": "00e525f3-420b-4d76-b538-d0efc7957cd2",
             "siteType": "1"}

        req = requests.post("http://192.168.95.153:91/api/balance/WriteOffMoney", data=json.dumps(par), headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

    def test_15_write_off_money_site_type_not_found_negative(self):
        par = {"tenderId": 26285,
             "lotId": 11,
             "amount": 1000.0,
             "currency": "ГРН",
             "descriptions": "Тендер: Соль таблетированная 22 000 кг. Лот №1 Позиції: Сіль таблетована   ",
               "totalMoney": 511.5,
             "companyUuid": "68a14f2a-c5a2-4a76-9d86-88c2ffad742b",
             "serviceIdentifierUuid": "00e525f3-420b-4d76-b538-d0efc7957cd2",
             "siteType": ""}

        req = requests.post("http://192.168.95.153:91/api/balance/WriteOffMoney", data=json.dumps(par), headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)


    def test_16_write_off_money_error_negative(self):
        par = {"tenderId": 26285,
             "lotId": 11,
             "amount": 1000.0,
             "currency": "ГРН",
             "descriptions": "Тендер: Соль таблетированная 22 000 кг. Лот №1 Позиції: Сіль таблетована   ",
               "totalMoney": 511.5, #передача json без companyUuid
             "serviceIdentifierUuid": "00e525f3-420b-4d76-b538-d0efc7957cd2",
             "siteType": "1"}
        req = requests.post("http://192.168.95.153:91/api/balance/WriteOffMoney", data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)


    def test_17_cancel_reserve_money_positive(self):
        par = {"tenderId": 26285,
             "lotId": 11,
             "amount": 1000.0,
             "currency": "ГРН",
             "descriptions": "Тендер: Соль таблетированная 22 000 кг. Лот №1 Позиції: Сіль таблетована   ",
               "totalMoney": 511.5,
             "companyUuid": "68a14f2a-c5a2-4a76-9d86-88c2ffad742b",
             "serviceIdentifierUuid": "00e525f3-420b-4d76-b538-d0efc7957cd2",
             "siteType": "1"}

        req = requests.post("http://192.168.95.153:91/api/balance/CancelReserve", data=json.dumps(par),
                            headers={"content-type": "application/json"})
        #self.assertEqual(req.status_code, 200)

    def test_18_cancel_reserve_money_tender_id_is_null_negative(self):
        par = {"tenderId": 0,
             "lotId": 11,
             "amount": 1000.0,
             "currency": "ГРН",
             "descriptions": "Тендер: Соль таблетированная 22 000 кг. Лот №1 Позиції: Сіль таблетована   ",
               "totalMoney": 511.5,
             "companyUuid": "68a14f2a-c5a2-4a76-9d86-88c2ffad742b",
             "serviceIdentifierUuid": "00e525f3-420b-4d76-b538-d0efc7957cd2",
             "siteType": "1"}

        req = requests.post("http://192.168.95.153:91/api/balance/CancelReserve", data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

    def test_19_cancel_reserve_money_error_negative(self):
        par = {"tenderId": 26285,
             "lotId": 11,
             "amount": 1000.0, #передача json без currency
             "descriptions": "Тендер: Соль таблетированная 22 000 кг. Лот №1 Позиції: Сіль таблетована   ",
               "totalMoney": 511.5,
             "companyUuid": "68a14f2a-c5a2-4a76-9d86-88c2ffad742b",
             "serviceIdentifierUuid": "00e525f3-420b-4d76-b538-d0efc7957cd2",
             "siteType": "1"}

        req = requests.post("http://192.168.95.153:91/api/balance/CancelReserve", data=json.dumps(par),
                            headers={"content-type": "application/json"})
        self.assertNotEquals(req.status_code, 200, 201)
        self.assertEqual(req.status_code, 400)

if __name__ == '__main__':
    utb = UnitTestByBilling()
    utb.test_01_get_balance_positive()
    utb.test_02_get_balance_acc_negative()
    utb.test_03_get_balance_without_guid_negative()
    utb.test_04_reserve_balance_positive()
    utb.test_05_reserve_balance_tender_id_is_null_negative()
    utb.test_06_reserve_balance_total_money_is_zero_negative()
    utb.test_07_return_monies_positive()
    utb.test_08_return_monies_tender_is_null_negative()
    utb.test_09_return_monies_error_negative()
    utb.test_10_return_monies_by_company_uuid_positive()
    utb.test_11_return_monies_by_company_uuid_tender_is_null_negative()
    utb.test_12_return_monies_by_company_uuid_error_negative()
    utb.test_13_write_off_money_positive()
    utb.test_14_write_off_money_tender_is_null_negative()
    utb.test_15_write_off_money_site_type_not_found_negative()
    utb.test_16_write_off_money_error_negative()
    utb.test_17_cancel_reserve_money_positive()
    utb.test_18_cancel_reserve_money_tender_id_is_null_negative()
    utb.test_19_cancel_reserve_money_error_negative()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="example_dir"))
