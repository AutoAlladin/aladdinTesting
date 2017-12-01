from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from Aladdin.Billing.CreateAccount import CreateAccount
from Aladdin.Billing.CheckBalance import CheckBalance

from Aladdin.Billing.CheckRezerv import CheckReserv


class full_billing(ParamsTestCase):
    def test_01_create_account(self):
        CreateAccount.test_01_new_UUID_new_EDR()

    def test_02_refill_balance(self):
        CheckBalance.test_02_refill_full()

    def test_03_checkBalance(self):
        CheckBalance.test_01_balance()

    def test_04_addReserve(self):
        CheckReserv.test_01_add_rezerv()

    def test_05_checkBalance(self):
        CheckBalance.test_01_balance()

    def test_06_fixReserve(self):
        CheckReserv.test_04_charge_off()

    def test_07_checkBalance(self):
        CheckBalance.test_01_balance()

    def test_08_addReserve(self):
        CheckReserv.test_01_add_rezerv()

    def test_09_cancelReserve(self):
        CheckReserv.test_02_cansel_rezerv()

    def test_10_checkBalance(self):
        CheckBalance.test_01_balance(self)







