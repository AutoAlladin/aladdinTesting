import json
import os

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Prozorro.Pages.UserCompanyForm import UserCompanyForm
from Prozorro.Pages.UserRegForm import UserRegForm
from Prozorro.Procedures.Tenders import init_driver
from Prozorro import Utils


def registerUserCompany(filename, testMode=True):
    chrm, tp, mpg = init_driver(testMode)
    with open(filename, 'r',
              encoding="UTF-8") as company_file:
        cmp = json.load(company_file)



    for cmpp in cmp["Company"]:
        ussr = cmpp["Users"][0]
        if len(cmpp["Users"])>1:
            ussr = cmpp["Users"][1]

        if ussr["login"].startswith("no@mail"):
            print("Фейковая почта", ussr["login"])
            continue

        Utils.waitFadeIn(mpg.drv)
        lf = mpg.open_login_form()
        lf.login(ussr["login"], "123456")
        try:
            WebDriverWait(lf.drv, 2).until(
                expected_conditions.visibility_of_element_located(
                    (By.ID, "error")))
            error = lf.drv.find_element_by_id("error")

            #если есть ошибка с таким текстом - регистрирумеся
            if error.text == "Невірна спроба входу в систему":
                lf.drv.find_element_by_id("btnRegister").click()
                WebDriverWait(lf.drv, 5).until(
                    expected_conditions.
                        visibility_of_element_located(
                        (By.CLASS_NAME, "btn-success")))
                print("START USER registartion",ussr["login"])
                rf= UserRegForm(lf.drv)
                rf.set_from_dic(cmpp)
        except Exception as e:
            print("USER register ERROR", e.__str__())
            pass

        try:
            print("USER registered", ussr["login"])
            danger =lf.drv.find_element_by_xpath("//span[@class='label label-danger']")
            lf.drv.find_element_by_xpath("//a[@ng-click=\"userMenuClick('/Profile#/company')\"]/../../..").click()
            butCabinet  = lf.drv.find_element_by_xpath("//a[@ng-click=\"userMenuClick('/Profile#/company')\"]")
            butCabinet.click()
            WebDriverWait(lf.drv, 10).until(
                expected_conditions.visibility_of_element_located(
                    (By.ID, "save_changes")))
            print("START COMPANY registartion",
                   ussr["login"],
                   "EDRPOU",
                   cmpp["subj_ident_code"] )
            cmF = UserCompanyForm(lf.drv)
            cmF.companyForm(cmpp)

            WebDriverWait(lf.drv, 15).until(
                expected_conditions.visibility_of_element_located(
                    (By.ID, "edit")))

            WebDriverWait(lf.drv, 15).until(
                expected_conditions.visibility_of_element_located(
                    (By.ID, "liLoginAuthenticated"))).click()

            WebDriverWait(lf.drv, 15).until(
                expected_conditions.visibility_of_element_located(
                    (By.ID, "liLoginNoAuthenticated")))

            time.sleep(1)

        except:
            pass







