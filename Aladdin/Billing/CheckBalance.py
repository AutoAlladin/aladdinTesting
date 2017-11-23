
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


