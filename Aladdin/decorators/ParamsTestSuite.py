import unittest

#__metaclass__ = type
from Aladdin.AladdinUtils import WebTestSession
from Aladdin.decorators.StoreTestResult import create_result_DB


class ParamsTestSuite(unittest.TestSuite):
    params= dict()

    def __init__(self, tests=(),  _params=None):
        super().__init__(self)
        self.params=_params