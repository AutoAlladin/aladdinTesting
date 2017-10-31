import os
from pymongo import MongoClient
import gridfs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bson.objectid import ObjectId
import time


def test_select(cls, id_field, input_val=None, q=None):
    try:
        if input_val is None:
            input_val = cls.wts.__mongo__.get_select_val(id_field, q)

        cls.assertEqual(
            input_val,
            cls.wts.select_value(id_field, input_val),
            "Не совпадают исходные даные и то что оказалось в поле браузера")
    except Exception as e:
        cls.wts.drv.get_screenshot_as_file("output\\"+id_field+"_ERROR.png")
        cls.assertTrue(False, "Ошибка при выборе значения\n" + e.__str__())

def test_input(cls, id_field, input_val=None, q=None):
    try:
        if input_val is None:
            input_val = cls.wts.__mongo__.get_input_val(id_field, q)

        cls.assertEqual(
            input_val,
            cls.wts.input_text_field(id_field, input_val),
            "Не совпадают исходные даные и то что оказалось в поле браузера")
    except Exception as e:
        cls.wts.drv.get_screenshot_as_file("output\\"+id_field+"_ERROR.png")
        cls.assertTrue(False, "Ошибка при вводе текста\n" + e.__str__())

class MdbUtils():
    def __init__(self):
        self.client = MongoClient('192.168.80.121', 27017)
        self.db = self.client['aladdin_tests']
        self.test_params = self.db["test_params"]
        self.fs = gridfs.GridFS(self.db)

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

    def get_file(self, doc_name, query=None):
        query = {"name": "RegistartionDocs", "version": "0.0.0.1"}
        docs = self.test_params.find_one(query)["docs"]
        name = docs[doc_name]["name"]
        file_id =  docs[doc_name]["file_id"]
        f_data = self.fs.get( ObjectId(file_id))

        with(open(os.path.dirname(os.path.abspath(__file__)) + '\\dir\\' + name, 'wb')) as f:
            f.write(f_data.read())
        return os.path.dirname(os.path.abspath(__file__)) + '\\dir\\'+name

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
    def __init__(self, url):
        self.url = url
        self.drv = webdriver.Chrome()
        #self.drv.find_elements_by_xpath()
        #  = webdriver.Chrome(chrm)
        self.drv.maximize_window()
        self.drv.implicitly_wait(5)
        self.__mongo__=MdbUtils()

    def set_main_page(self):
        #self.drv.get('https://192.168.80.169:44310/i_uk/registration/user')
        self.drv.get(self.url)
        # btn_registration = self.drv.find_element_by_xpath(".//*[@id='navbarCollapse']/div[2]/div[1]/a[2]")
        # btn_registration.click()
        # WebDriverWait(self.drv, 15).until(
        #     EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "РЕЄСТРАЦІЯ ПІДПРИЄМСТВА"))

    def input_text_field(self,_id,val):
        try:
            WebDriverWait(self.drv, 1).until(EC.visibility_of_element_located((By.ID, _id)))
        except:
            self.set_main_page()

        text_field = self.drv.find_element_by_id(_id)
        text_field.send_keys(val)
        self.drv.get_screenshot_as_file("output\\"+_id + ".png")
        return text_field.get_attribute('value')

    def select_value(self, _id, val):
        try:
            WebDriverWait(self.drv, 1).until(EC.visibility_of_element_located((By.ID, _id)))
        except:
            self.set_main_page()

        field = self.drv.find_element_by_id(_id)
        Select(field).select_by_value(val)
        self.drv.get_screenshot_as_file("output\\" + _id + ".png")
        return field.get_attribute('value')

    def close(self):
        self.drv.close()
        self.__mongo__.client.close()
        pass