import json

import requests

from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from Aladdin.DB.billing import get_db_balance
import unittest

class CheckBalance(ParamsTestCase):

    def test_01_balance(self):
        rq = requests.get(self.params["service"].format(self.params["empty_acc"]))
        amount = float(rq.text)
        amount_db = get_db_balance(self.params["empty_acc"])
        print("balance", amount, amount_db, amount == amount_db)

        if amount_db is None:
            amount_db = 0.0

        self.assertEqual(rq.status_code, 200)
        self.assertEqual(amount, amount_db)

    def test_02_refill(self):

        # URl: http: // localhost: 54680 / api / Private24 / test
        # Request: POST
        # JSON: [{"TransactionGuid": "3420E605-ADFA-4FBC-8B7C-588222EA45B2", "CompanyEdrpoSender": "19039522",
        #         "CompanyEdrpoReceiver": "414771",
        #         "AccountNumberSender": "5454523",
        #         "Amount": "3131", "Currency": "UAH"}]

        rq = requests.post(self.params["service_refill"],
                           data=json.dumps(self.params["refill"]),
                           headers={'content-type': 'application/json'})
        amount = float(rq.text)
        amount_db = get_db_balance(self.params["empty_acc"])
        print("balance", amount, amount_db, amount == amount_db)

        if amount_db is None:
            amount_db = 0.0

        self.assertEqual(rq.status_code, 200)
        self.assertEqual(amount, amount_db)
