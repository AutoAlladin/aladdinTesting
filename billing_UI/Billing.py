import unittest

from Aladdin.Accounting.decorators.StoreTestResult import add_res_to_DB
from Prozorro.Pages.MainPage import MainPage
from Prozorro.Pages.LoginPage import LoginPage
from Prozorro.Procedures.Tenders import init_driver
from Prozorro.Procedures.Tenders import create_below
from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from Prozorro.ProzorroCheck import init_driver
from Prozorro.ProzorroCheck import create_below
from Prozorro.ProzorroCheck import create_bids
from Prozorro.ProzorroCheck import open_tender


class BalanceAfterBid(ParamsTestCase):
    @add_res_to_DB()
    def create_below(self):
        uaid = create_below(tender_dict=self.parent_suite.suite_params["dic_params"])
        self.parent_suite.suite_params.update({"uaid": uaid[0][0]})
        self.tlog.append("create_below OK - " + str(uaid[0][0]))
        print(uaid[0][0])
        open_tender(uaid, role="provider")
        #create_bids(uaid)

    @add_res_to_DB()
    def creare_bids(self):
        pass



    def logout(self):
        pass

    def login_provider(self):
        pass

class ViewBalance(ParamsTestCase):
    def view_balance(self):
        pass

class SearchTender(ParamsTestCase):
    def search_tender(self):
        pass

class Bids(ParamsTestCase):
    def bids(self):
        pass

    def view_statistic(self):
        pass

    def logout(self):
        pass

class BalanceAfterCancelBid(ParamsTestCase):
    def login_owner(self):
        pass

    def create_tender(self):
        pass

