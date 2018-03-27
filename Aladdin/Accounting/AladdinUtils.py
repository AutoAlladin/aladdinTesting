import os

from pymongo import MongoClient
import gridfs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from bson.objectid import ObjectId
from enum import Enum



class AvaliableBrowsers(Enum):
    Chrome=1,
    Firefox=2

def test_select(cls, id_field, input_val=None, q=None):
    try:
        if input_val is None:
            input_val = cls.wts.__mongo__.get_ID("select",id_field, q)

        cls.assertEqual(
            input_val,
            cls.wts.select_value(id_field, input_val),
            "Не совпадают исходные даные и то что оказалось в поле браузера")
    except Exception as e:
        cls.wts.drv.get_screenshot_as_file("output\\"+id_field+"_ERROR.png")

def test_input(cls, id_field, input_val=None, q=None):
    try:
        if input_val is None:
            input_val = cls.wts.__mongo__.get_ID("inputs",id_field, q)
        cls.assertEqual(
            input_val,
            cls.wts.input_text_field(id_field, input_val),
            "Не совпадают исходные даные и то что оказалось в поле браузера")
    except Exception as e:
        cls.wts.drv.get_screenshot_as_file("output\\"+id_field+"_ERROR.png")
        raise e

def test_click(cls, id_field, input_val=None, q=None):
    try:
        if input_val is None:
            input_val = cls.wts.__mongo__.get_ID("buttons",id_field, q)
        cls.wts.click_element( input_val),
        cls.assertTrue(True)
    except Exception as e:
        cls.wts.drv.get_screenshot_as_file("output\\"+id_field+"_ERROR.png")
        raise e


class MdbUtils():

    def __init__(self):
        self.client = MongoClient('192.168.80.121', 27017)
        self.db = self.client['aladdin_tests']
        self.test_params = self.db["test_params"]
        self.test_result = self.db["test_results"]
        self.fs = gridfs.GridFS(self.db)

    def create_result(self):
        self.test_res= {
            "test_name": "",
            "test_timestamp": "",
            "test_result": "STARTED",
            "run_info": {
                "user": "",
                "ip": ""
            }
        }
        return self.test_result.insert_one(self.test_res).inserted_id


    def get_ID(self, tag, _id, query):
        doc = self.test_params.find_one(query)
        if doc is None:
            return "test {0} is None".format(_id)
        elif doc[tag] is None:
            return "element {0} is None".format(_id)
        elif doc[tag][_id]  is None:
            return "value {0} is None".format(_id)
        else:
            return doc[tag][_id]

    def get_file(self, doc_name, query=None):
        query = {"name": "RegistartionDocs", "version": "0.0.0.1"}
        docs = self.test_params.find_one(query)["docs"]
        name = docs[doc_name]["name"]
        file_id =  docs[doc_name]["file_id"]
        f_data = self.fs.get( ObjectId(file_id))

        with(open(os.path.dirname(os.path.abspath(__file__)) + '\\dir\\' + name, 'wb')) as f:
            f.write(f_data.read())
        return os.path.dirname(os.path.abspath(__file__)) + '\\dir\\'+name

    def get_params(self, id):
        return self.test_params.find_one({"_id":id})

class WebTestSession:
    def __init__(self, url=None, browser=None, useBrowser=True):
        self.url = url
        self.result_id = None
        self.test_name = None
        self.group = None
        self.drv = None
        self.__mongo__ = MdbUtils()

        if useBrowser:
            if browser is None:
                browser = AvaliableBrowsers.Chrome

            if browser == AvaliableBrowsers.Chrome:
                self.drv = webdriver.Chrome()
            else:
                self.drv = webdriver.Firefox()

            self.drv.set_window_size(1900, 1050)
            self.drv.set_window_position(2, 2)
            self.drv.implicitly_wait(5)

    def set_main_page(self,q):
        if q is not None:
            r= self.__mongo__.test_params.find_one(q["q"])
            self.url = r["start_url"]

        self.drv.get(self.url)

    def click_element(self, _id):
        WebDriverWait(self.drv, 5).until(EC.visibility_of_element_located((By.ID, _id)))
        field = self.drv.find_element_by_id(_id)
        field.click()

    def input_text_field(self,_id,val):
        try:
            WebDriverWait(self.drv, 1).until(EC.visibility_of_element_located((By.ID, _id)))
        except:
            self.set_main_page()

        text_field = self.drv.find_element_by_id(_id)
        text_field.send_keys(val)
        #self.drv.get_screenshot_as_file("output\\"+_id + ".png")
        return text_field.get_attribute('value')

    def select_value(self, _id, val):
        try:
            WebDriverWait(self.drv, 1).until(EC.visibility_of_element_located((By.ID, _id)))
        except:
            self.set_main_page()

        field = self.drv.find_element_by_id(_id)
        Select(field).select_by_value(val)
        #self.drv.get_screenshot_as_file("output\\" + _id + ".png")
        return field.get_attribute('value')

    def w_xpath(self, xpath, timeout=5):
        element = WebDriverWait(self.drv, timeout).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, xpath)))
        return element

    def w_id(self, id, timeout=5):
        element = WebDriverWait(self.drv, timeout).until(
            expected_conditions.presence_of_element_located(
                (By.ID, id)))
        return element

    def close(self):
        self.drv.close()
        self.__mongo__.client.close()
        pass