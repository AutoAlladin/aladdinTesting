from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class MdbUtils():
    def __init__(self):
        self.client = MongoClient()
        #self.client = MongoClient('192.168.95.156',27017)
        self.db = self.client['aladdin_tests']
        self.test_params = self.db["test_params"]

    def get_input_val(self,_id, query):
        doc = self.test_params.find_one(query)
        if doc is None:
            return "test {0} is None".format(_id)
        elif doc["inputs"] is None:
            return "element {0} is None".format(_id)
        elif doc["inputs"][_id]  is None:
            return "value {0} is None".format(_id)
        else:
            return doc["inputs"][_id]

    def get_select_val(self,_id, query):
        doc = self.test_params.find_one(query)
        if doc is None:
            return "test {0} is None".format(_id)
        elif doc["select"] is None:
            return "element {0} is None".format(_id)
        elif doc["select"][_id]  is None:
            return "value {0} is None".format(_id)
        else:
            return doc["select"][_id]

class WebTestSession():
    def __init__(self):
        self.drv = webdriver.Chrome()
        #chrm = webdriver.Chrome(chrm)
        self.drv.maximize_window()
        self.drv.implicitly_wait(5)
        self.__mongo__=MdbUtils()

    def click_reg_btn(self):
        self.drv.get('https://192.168.80.169:44310/i_uk/registration/user')
        # btn_registration = self.drv.find_element_by_xpath(".//*[@id='navbarCollapse']/div[2]/div[1]/a[2]")
        # btn_registration.click()
        # WebDriverWait(self.drv, 15).until(
        #     EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "РЕЄСТРАЦІЯ ПІДПРИЄМСТВА"))

    def input_text_field(self,_id,val):
        try:
            WebDriverWait(self.drv, 1).until(EC.visibility_of_element_located((By.ID, _id)))
        except:
            self.click_reg_btn()

        text_field = self.drv.find_element_by_id(_id)
        text_field.send_keys(val)
        self.drv.get_screenshot_as_file("output\\"+_id + ".png")
        return text_field.get_attribute('value')

    def select_value(self, _id, val):
        try:
            WebDriverWait(self.drv, 1).until(EC.visibility_of_element_located((By.ID, _id)))
        except:
            self.click_reg_btn()

        field = self.drv.find_element_by_id(_id)
        Select(field).select_by_value(val)
        self.drv.get_screenshot_as_file("output\\" + _id + ".png")
        return field.get_attribute('value')

    def close(self):
        self.drv.close()
        pass