import unittest

#__metaclass__ = type
from Aladdin.AladdinUtils import WebTestSession
from Aladdin.decorators.StoreTestResult import create_result_DB


class ParamsTestSuite(unittest.TestSuite):
    params= {}

    def __init__(self,  _params=None):
        super().__init__()
        self.params=_params