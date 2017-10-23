import unittest

from Aladdin.AladdinUtils import *
from tkinter import filedialog
from tkinter import *
import os
from urllib.parse import urlparse
from Prozorro.Utils import scroll_to_element
from selenium.webdriver.support import expected_conditions as EC
from Prozorro.Utils import *
from Aladdin.Registration.OpenMainPage import *

publicWST = None;
def setUpModule():
    global publicWST
    publicWST = WebTestSession()

def tearDownModule():
    publicWST.close()


class UserRegistration_FOP(UserRegistration):
    def test_03_check_ownership(self):
        test_select("ownership_type", "11")

    def test_04_code_edrpou(self):
        test_input("company_code_USREOUFop", "1234567897897")

