
import requests

from Aladdin.DB.billing import get_db_balance
import unittest

class CheckBalance(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service= "http://192.168.95.153:91/api/balance?companyUuid={0}"
        cls.empty_acc="2F6D3BCD-8898-44EB-9C0D-9969E5776C66"
        cls.full_acc="28DAE9EC-6D86-417C-AC22-46F73EC1EB44"

    def test_01_empty_acc(self):
        rq = requests.get(self.service.format(self.empty_acc))
        amount = float(rq.text)
        amount_db = get_db_balance(self.empty_acc)
        print("empty", amount, amount_db, amount == amount_db)

    def test_02_full_acc(self):
        rq = requests.get(self.service.format(self.full_acc))
        amount = float(rq.text)
        amount_db = get_db_balance(self.full_acc)
        print("positive", amount, amount_db, amount == amount_db)


# if __name__ == "__main__":
#     amount=0.0

    # for new empty accout
    # try:
    #     rq = requests.get(service.format(empty_acc))
    #     amount = float(rq.text)
    #     amount_db = get_db_balance(empty_acc)
    #     print("empty", amount, amount_db, amount == amount_db)
    # except Exception as e:
    #     print(e.__str__())
    #
    # # for ready account
    # try:
    #     rq = requests.get(service.format(full_acc))
    #     amount = float(rq.text)
    #     amount_db = get_db_balance(full_acc)
    #     print("positive", amount, amount_db, amount == amount_db)
    # except Exception as e:
    #     print(e.__str__())


