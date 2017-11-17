import time

from Aladdin.Accounting.Authorization.Login import Login
from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase

from Aladdin.Accounting.AladdinUtils import *

publicWST = None;

class Docs(ParamsTestCase):


    def test_1_Login(self):
        l = Login()
        l.test_01_email()
        l.test_02_pswd()
        l.test_03_btn()

    def test_3_add_doc(self):

        self.wts.drv.execute_script("window.scrollTo(0, 0);")
        btn_tab_documents = self.wts.drv.find_element_by_id("profile_tab_documents")
        btn_tab_documents.click()
        WebDriverWait(self.wts.drv, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ui-datatable")))

        taxpayerCertificateINN = self.wts.drv.find_element_by_id("load_TaxpayerCertificateINN")
        file_name = self.wts.__mongo__.get_file(doc_name="TaxpayerCertificateINN")
        taxpayerCertificateINN.send_keys(file_name)
        time.sleep(10)


    #def test_4_doc_view(self):
        # btn_eye = self.wts.drv.find_element_by_id("show_TaxpayerCertificateINN")
        # btn_eye.click()
        # time.sleep(10)
        # #self.wts.drv.execute_script("window.scrollTo(0, 0);")
        # WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "modal_close")))
        # btn_close = self.wts.drv.find_element_by_id("modal_close")
        # btn_close.click()
        # time.sleep(20)

    def test_5_doc_delete(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "delete_TaxpayerCertificateINN")))
        btn_delete_doc = self.wts.drv.find_element_by_id("delete_TaxpayerCertificateINN")
        btn_delete_doc.click()

    def test_6_doc2_add(self):
        License = self.wts.drv.find_element_by_id("load_License")
        file_name = self.wts.__mongo__.get_file(doc_name="License")
        License.send_keys(file_name)
        time.sleep(10)
        # self.wts.drv.refresh()


        self.wts.drv.refresh()



