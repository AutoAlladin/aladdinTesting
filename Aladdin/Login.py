import unittest
from selenium import webdriver

from Aladdin.AladdinUtils import *
from Aladdin  import Authorization

# browser = None;
# def setUpModule():
#     global browser
#     browser = openChrome()

publicWST = None;
def setUpModule():
    global publicWST
    publicWST = WebTestSession()


def tearDownModule():
    publicWST.drv.close()

#
# def field_input(_id, val):
#     field_input=browser.drv.find_element_by_id("_id")
#     field_input.send_keys("val")
#     return field_input.get_attribute('value')
#
# def text_input(_id, val, input_val=None):
#     try:
#         if input_val is None:
#             input_val = field_input(_id, val)
#         browser.drv.assertEqual(
#             input_val,
#             browser.drv.field_input
#         )
#     except Exception as e:
#         browser.assertTrue(False, "Ошибка при вводе текста\n" + e.__str__())




#
#
# class openChrome(unittest.TestCase):
#     def __init__(self):
#         try:
#             self.drv = webdriver.Chrome()
#             self.drv.maximize_window()
#             self.drv.implicitly_wait(10)
#             #self.drv.get('https://192.168.80.169:44310/Account/Login')
#             self.drv.get('https://identity.ald.in.ua/Account/Login')
#             self.assertTrue(True)
#         except Exception as e:
#             self.assertTrue(False, 'Не открывается форма логина\n' + e.__str__())
#
#



class Login(unittest.TestCase):
    wts = None

    @classmethod
    def setUpClass(cls):
        cls.wts = publicWST
        cls.wts.url = 'https://identity.ald.in.ua/Account/Login'

    def test_01_email(self):
        #text_input("exampleInputEmail1", "envarra@gmail.com")
        # email = browser.drv.find_element_by_id("exampleInputEmail1")
        # email.send_keys("envarra@gmail.com")
        test_input(self, "exampleInputEmail1", "envarra@gmail.com")


    def test_02_pswd(self):
        # pswd = browser.drv.find_element_by_id("pswd")
        # pswd.send_keys("qwerty1234")
        # time.sleep(10)
        test_input(self, "pswd", "qwerty1234")

    def test_03_btn(self):
        btn = self.wts.drv.find_element_by_id("submitLogin")
        btn.click()
        #WebDriverWait(browser.drv, 10).until(EC._find_element(By.XPATH), "html/body")
        time.sleep(10)

class EditInfo(OpenMainPage):
    def test_01_go_to_user_profile(self):
        user_prof = self.wts.drv.find_element_by_id("link_about")
        time.sleep(5)
        user_prof.click()

    def test_02_click_tab_company(self):

        btn_tab_company = self.wts.drv.find_element_by_id("profile_tab_company")
        time.sleep(10)
        btn_tab_company.click()
        self.wts.drv.execute_script("window.scrollTo(0, 2500);")


    def test_03_ownership_tax(self, r, id_field, input_val=None, q=None):
        select_ownership = browser.drv.find_element_by_id("ownership_type")
        select_ownership.send_keys("0")
        time.sleep(10)
        code = browser.drv.find_element_by_id("company_code_USREOU")
        return code.get_attribute("id")
        self.assertTrue("id" == code)


        # try:
        #     if input_val is None:
        #         input_val = r.wts.__mongo__.get_input_val(id_field, q)
        #
        #     select_ownership = browser.drv.find_element_by_id("ownership_type")
        #     select_ownership.send_keys("0")
        #     time.sleep(10)
        #     code = browser.drv.find_element_by_id("company_code_USREOU")
        #     return code.get_attribute("id")
        #
        #     r.assertTrue("id" == code)
        #
        # except Expection as e:
        #     r.assertTrue(False, "При редактировании формы собственности - код не изменился\n" + e.__str__())



    def test_03_click_btn_edit(self):
        btn_edit = self.wts.drv.find_element_by_id("btn_edit")
        time.sleep(10)
        btn_edit.click()

    def test_04_update_comp_name(self):
        test_input()
        time.sleep(5)
        comp_name = self.wts.drv.find_element_by_id("nameUA")
        comp_name.send_keys("SunnyBunny")
        time.sleep(10)

    def test_06_contract_offer(self):
        contract_offer_check = browser.drv.find_element_by_xpath(".//*[@id='contract_offer_container']/label")
        contract_offer_check.click()



    def test_05_click_btn_save_changes(self):
        self.wts.drv.execute_script("window.scrollTo(0, 2500);")
        btn_s_changes = self.wts.drv.find_element_by_id("btn_save_changes")
        time.sleep(5)
        btn_s_changes.click()
