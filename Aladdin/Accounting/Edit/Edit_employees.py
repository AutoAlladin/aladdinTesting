from Aladdin.AladdinUtils import *

from Aladdin.Accounting.Registration.OpenMainPage import *
from Prozorro.Utils import *

publicWST = None;
def setUpModule():
    global publicWST
    publicWST = WebTestSession('https://192.168.80.169:44310/Account/Login')
    #publicWST = WebTestSession('https://identity.ald.in.ua/Account/Login')

def tearDownModule():
    publicWST.close()

class OpenMainPage(unittest.TestCase):
    wts=None
    @classmethod
    def setUpClass(cls):
        cls.wts = publicWST

class Edit_employees(OpenMainPage):
    query = {"input_val": None, "q": {"name": "EmployeeesInfo", "version": "0.0.0.1"}}
    test_params = {}

    def test_01_click_tab_employees(self):
        btn_tab_empl = self.wts.drv.find_element_by_id("profile_tab_employees")
        btn_tab_empl.click()
        time.sleep(10)
        click_edit = self.wts.drv.find_element_by_xpath(".//*[contains(@id,'edit_empoyee_')]")
        click_edit.click()
        time.sleep(10)

    def test__clear_name(self):
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "firstName_0")))
        cl_name = self.wts.drv.find_element_by_id("firstName_0")
        WebDriverWait(self.wts.drv, 20).until(EC.element_to_be_clickable((By.ID, "firstName_0")))
        time.sleep(5)
        cl_name.clear()
        time.sleep(15)

    def test_02_update_name(self):
        test_input(self, "firstName_0", "Редактирование-имени")


    def test_03_update_last_name_eu(self):
        test_input(self, "lastNameEn_0", "Edit-name")


    def test_04_update_position(self):
        test_input(self, "position_0", "Редактирование должности")


    def test_05_update_role(self):
        test_select(self, "role_0", "7")


    def test_06_save(self):
        btn_save = self.wts.drv.find_element_by_id("save_changes_0")
        btn_save.click()
        # wanted_email = None
        # email_list = self.wts.drv.find_elements_by_xpath(".//*[contains(@id, 'email_')]")
        # inp_email = self.test_params['email_0']
        # for email in email_list:
        #     if email.text == inp_email:
        #         wanted_email = inp_email
        #         print("Все ОК, email отображается")
        #         break
        #
        # if wanted_email == None:
        #     print("Сотрудник не добавлен")