import unittest
from Prozorro.Pages.MainPage import MainPage
from Prozorro.Pages.LoginPage import LoginPage
from Prozorro.Procedures.Tenders import init_driver
from Prozorro.Procedures.Tenders import create_below
from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from Prozorro.ProzorroCheck import init_driver
from Prozorro.ProzorroCheck import create_below


class BalanceAfterBid(ParamsTestCase):
    def open_main_page(self):
        #MainPage.__init__()
        init_driver()
        create_below()

    def login_owner(self):
        pass


    def create_tender(self):
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

