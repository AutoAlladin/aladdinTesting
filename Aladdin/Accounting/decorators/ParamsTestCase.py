import unittest

#__metaclass__ = type


class ParamsTestCase(unittest.TestCase):
    params={}

    tlog = [{}]
    wts = None


    def __init__(self, name='runTest', _params=None):
        super().__init__(methodName=name)
        self.params=_params
        if 'wts' in self.params:
            self.wts = self.params["wts"]


