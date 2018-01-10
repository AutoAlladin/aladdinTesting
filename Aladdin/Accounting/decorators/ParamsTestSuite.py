import unittest

#__metaclass__ = type


class ParamsTestSuite(unittest.TestSuite):
    suite_params = dict()

    def __init__(self, tests=(),  _params=None):
        super().__init__(self)
        self.suite_params=_params