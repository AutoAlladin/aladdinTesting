import unittest
from billing_UI.billing_UI import BalanceAfterBid

def s_balance_after_bid():
    suite = unittest.TestSuite

    suite.addTest(BalanceAfterBid("open_main_page"))
    suite.addTest(BalanceAfterBid("login_owner"))




    return suite





