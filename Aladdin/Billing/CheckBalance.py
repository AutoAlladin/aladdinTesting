
import requests

from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from Aladdin.DB.billing import get_db_balance
import unittest

class CheckBalance(ParamsTestCase):


    def test_01_empty_acc(self):
        rq = requests.get(self.params["service"].format(self.params["empty_acc"]))
        amount = float(rq.text)
        amount_db = get_db_balance(self.params["empty_acc"])
        print("empty balance", amount, amount_db, amount == amount_db)

    def test_02_full_acc(self):
        rq = requests.get(self.params["service"].format(self.params["full_acc"]))
        amount = float(rq.text)
        amount_db = get_db_balance(self.params["full_acc"])
        print("positive balance", amount, amount_db, amount == amount_db)
