import unittest
from Prozorro.Pages.MainPage import MainPage
from Prozorro.Pages.LoginPage import LoginPage
from Prozorro.Procedures.Tenders import init_driver
from Prozorro.Procedures.Tenders import create_below
from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase


class BalanceAfterBid(ParamsTestCase):
    def open_main_page(self):
        MainPage.__init__()


    def login_owner(self):
        LoginPage.__init__()
        LoginPage.login()

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

class BalanceAfterCancelBid():
    def login_owner(self):
        pass

    def create_tender(self):
        pass

