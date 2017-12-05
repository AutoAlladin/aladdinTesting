import json
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Prozorro.Pages.UserRegForm import UserRegForm
from Prozorro.Procedures.Tenders import init_driver


def registerUserCompany(filename):
    chrm, tp, mpg = init_driver()
    with open(os.path.dirname(os.path.abspath(__file__)) + '\\..\\'+filename, 'r',
              encoding="UTF-8") as company_file:
        cmp = json.load(company_file)

    lf=mpg.open_login_form()
    lf.login(cmp["Company"][0]["Users"][0]["login"], "123456")
    try:
        WebDriverWait(lf.drv, 1).until(
            expected_conditions.visibility_of_element_located(
                (By.ID, "error")))
        error = lf.drv.find_element_by_id("error")

        #если есть ошибка с таким текстом - регистрирумеся
        if error.text == "Невірна спроба входу в систему":
            lf.drv.find_element_by_id("btnRegister")
            WebDriverWait(lf.drv, 5).until(
                expected_conditions.visibility_of_element_located(
                    (By.CLASS_NAME, "btn-success")))
            print("START USER registartion", cmp["Company"][0]["Users"][0]["login"])
            rf= UserRegForm(lf.drv)
            rf.set_from_dic(cmp["Company"][0])
    except:
        print("USER registered", cmp["Company"][0]["Users"][0]["login"])
        pass

    try:
        danger =lf.drv.find_element_by_xpath("//span[@class='label label-danger']")
        lf.drv.find_element_by_xpath("//a[@ng-click=\"userMenuClick('/Profile#/company')\"]/../../..").click()
        butCabinet  = lf.drv.find_element_by_xpath("//a[@ng-click=\"userMenuClick('/Profile#/company')\"]")
        butCabinet.click()
        WebDriverWait(lf.drv, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.ID, "save_changes")))
        print("START COMPANY registartion", cmp["Company"][0]["Users"][0]["login"])
    except:
        print("COMPANY registard", cmp["Company"][0]["Users"][0]["login"])
        pass







