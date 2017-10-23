import unittest

class OpenMainPage(unittest.TestCase):
    wts=None
    @classmethod
    def setUpClass(cls):
        cls.wts = publicWST
        cls.wts.url= 'https://identity.ald.in.ua/i_uk/registration/user'