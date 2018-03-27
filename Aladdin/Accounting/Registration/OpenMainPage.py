import unittest

from Aladdin.Accounting.AladdinUtils import WebTestSession

publicWST = None;
def setUpModule():
    global publicWST
    #publicWST = WebTestSession('https://identity.ald.in.ua/i_uk/registration/user')
    # publicWST = WebTestSession('https://192.168.80.169:44310/i_uk/registration/user')
    publicWST = WebTestSession('https://win-net-core:44340/uk/registration')

def tearDownModule():
    publicWST.close()

class OpenMainPage(unittest.TestCase):
    wts=None
    @classmethod
    def setUpClass(cls):
        cls.wts = publicWST
