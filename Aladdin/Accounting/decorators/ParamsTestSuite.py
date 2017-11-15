import unittest

#__metaclass__ = type


class ParamsTestSuite(unittest.TestSuite):
    params= dict()

    def __init__(self, tests=(),  _params=None):
        super().__init__(self)
        self.params=_params