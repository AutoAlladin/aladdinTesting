import unittest

#__metaclass__ = type


class ParamsTestCase(unittest.TestCase):
    params={}

    tlog = [{}]
    wts = None
    parent_suite = None

    def log(self,msg):
        self.tlog.append(msg)
        print(msg)

    def __init__(self, name='runTest', _params=None, _parent_suite=None):
        super().__init__(methodName=name)
        self.params=_params
        self.parent_suite=_parent_suite
        if 'wts' in self.params:
            self.wts = self.params["wts"]


