import unittest

from Aladdin.AladdinUtils import *
from Aladdin.Authorization.Login import Login
from Aladdin.Edit.Edit import Edit

publicWST = None;
def setUpModule():
    global publicWST
    #publicWST = WebTestSession('https://identity.ald.in.ua/Account/Login')
    publicWST = WebTestSession('https://192.168.80.169:44310/Account/Login')


def tearDownModule():
    publicWST.close()


class Docs(unittest.TestCase):
    wts=None

    @classmethod
    def setUpClass(cls):
        cls.wts = publicWST

    def test_1_Login(self):
        l = Login()
        l.wts = self.wts
        l.wts.set_main_page()
        l.test_01_email()
        l.test_02_pswd()
        l.test_03_btn()

    def test_2_User_profile(self):
        ed = Edit()
        ed.wts = self.wts
        ed.test_01_go_to_user_profile()

        btn_tab_documents = self.wts.drv.find_element_by_id("profile_tab_documents")
        btn_tab_documents.click()
        WebDriverWait(self.wts.drv, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ui-datatable")))


        taxpayerCertificateINN = self.wts.drv.find_element_by_id("load_TaxpayerCertificateINN")
        file_name = self.wts.__mongo__.get_file(doc_name="TaxpayerCertificateINN")
        taxpayerCertificateINN.send_keys(file_name)



        self.wts.drv.refresh()

