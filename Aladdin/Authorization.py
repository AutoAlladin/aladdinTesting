import unittest

#https://identity.ald.in.ua/


def setUpModule():
    #createConnection()
    pass

def tearDownModule():
    #closeConnection()
    pass

class RegisterForm(unittest.TestCase):
    def test_OpenForm(self):
        print("openform")
        self.assertEqual(True, True,"страничка открыта")

    def test_isButton(self):
        print("isButto")
        self.assertEqual(True,True,"нопка для регистрации есть")

class MainPage(unittest.TestCase):
    def test_OpenPage(self):
        print("openpage")
        self.assertEqual(True, True,"страничка открыта")

    def test_isRegistration(self):
        print("ref=")
        self.assertEqual(True,True,"ссылка для регистрации есть")

def suite1():
    suite=unittest.TestSuite()
    suite.addTest(RegisterForm("test_OpenForm"))
    # suite.addTest(RegisterForm("test_isButton"))
    # suite.addTest(MainPage("test_OpenPage"))
    # suite.addTest(MainPage("test_isRegistration"))
    return suite


