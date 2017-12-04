import json
from functools import reduce

import requests

from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from Aladdin.DB.billing import get_db_balance
import unittest

class CheckBalance(ParamsTestCase):

    def test_01_balance(self):
        rq = requests.get(self.params["service"].format(self.params["acc"]))
        self.assertEqual(rq.status_code, 200)

        amount = float(rq.text)
        amount_db = get_db_balance(self.params["acc"])
        print("balance", amount, amount_db, amount == amount_db)

        if amount_db is None:
            amount_db = 0.0


        self.assertEqual(amount, amount_db)

    def test_02_refill_full(self):

        list_db_amount=[]
        for refill in self.params["refill"]:
            key=refill["CompanyEdrpoReceiver"]
            val=get_db_balance(edr=refill["CompanyEdrpoReceiver"])
            list_db_amount.append({key:val})

        rq = requests.post(self.params["service_refill"],
                           data=json.dumps(self.params["refill"]),
                           headers={'content-type': 'application/json'})
        self.assertEqual(rq.status_code, 200)
        self.assertIsNotNone(rq.json())

        for response in rq.json():
            inpAmount=0.0
            for inp in self.params["refill"]:
                if inp["CompanyEdrpoReceiver"] == response["companyEdrpoReceiver"]:
                    inpAmount = float(inp["Amount"])
                    break

            for dba in list_db_amount:
                if list(dba.keys())[0] == response["companyEdrpoReceiver"]:
                    prev_db_amount = list(dba.values())[0]
                    break

            outAmount=float(response["amount"])
            self.assertEqual(inpAmount, outAmount, "FAIL method "+response["companyEdrpoReceiver"])

            dbAmount = get_db_balance(edr=response["companyEdrpoReceiver"])
            self.assertEqual(inpAmount, dbAmount-prev_db_amount, "FAIL db balance" + response["companyEdrpoReceiver"])

            print("PASS", response["companyEdrpoReceiver"])


    def test_02_refill_partial(self):
        rq = requests.post(self.params["service_refill"],
                           data=json.dumps(self.params["refill"]),
                           headers={'content-type': 'application/json'})
        self.assertEqual(rq.status_code, 200)
        self.assertIsNotNone(rq.json())
        full_in = full_out = full_db = 0


        for response in rq.json():
            inpAmount=0.0
            for inp in self.params["refill"]:
                if inp["CompanyEdrpoReceiver"] == response["CompanyEdrpoReceiver"]:
                    inpAmount = inp["Amount"]
                    break

            outAmount=float(response["amount"])
            if inpAmount != outAmount:
                print("FAIL metod"+response["CompanyEdrpoReceiver"],inpAmount, outAmount)

            dbAmount = get_db_balance(edr=response["CompanyEdrpoReceiver"])
            if inpAmount != dbAmount:
                print("FAIL dbAmount "+response["CompanyEdrpoReceiver"],inpAmount, dbAmount )

            full_in+=inpAmount
            full_out+=outAmount
            full_db+=dbAmount

        self.assertEqual(full_in, full_out, "Суммы metod не совпадают")
        self.assertEqual(full_in, full_db, "Суммы db не совпадают")