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


def registerUserCompany(filename):
    chrm, tp, mpg = init_driver()
    with open(os.path.dirname(os.path.abspath(__file__)) + '\\'+filename, 'r',
              encoding="UTF-8") as company_file:
        cmp = json.load(company_file)



    for cmpp in cmp["Company"]:
        ussr = cmpp["Users"][0]
        if len(cmpp["Users"])>1:
            ussr = cmpp["Users"][1]

        Utils.waitFadeIn(mpg.drv)
        lf = mpg.open_login_form()
        lf.login(ussr["login"], "123456")
        try:
            # WebDriverWait(lf.drv, 3).until(
            #     expected_conditions.text_to_be_present_in_element_value(
            #         (By.XPATH,'//div[@class="validation-summary-errors text-danger"]/ul/li'),
            #         "Invalid login attempt."))

            err = lf.drv.find_element_by_xpath('//div[@class="validation-summary-errors text-danger"]/ul/li')
            # print(err.text)
            if err.text=="Invalid login attempt.":
                lf.drv.find_element_by_id("btnRegister").click()
                WebDriverWait(lf.drv, 5).until(
                    expected_conditions.visibility_of_element_located(
                        (By.CLASS_NAME, "btn-success")))
                print("START USER registartion",ussr["login"])
                rf= UserRegForm(lf.drv)
                rf.set_from_dic(cmpp)
        except Exception as e :
            print("USER registered",ussr["login"], str(e))
            pass

        try:
            danger =lf.drv.find_element_by_xpath("//span[@class='label label-danger']")
            lf.drv.find_element_by_xpath("//a[@ng-click=\"userMenuClick('/Profile#/company')\"]/../../..").click()
            butCabinet  = lf.drv.find_element_by_xpath("//a[@ng-click=\"userMenuClick('/Profile#/company')\"]")
            butCabinet.click()
            WebDriverWait(lf.drv, 5).until(
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

            Utils.waitFadeIn(lf.drv)
            lf.drv.execute_script("$('#butLogoutPartial').click()")
            # print("b1")
            # exit =  lf.drv.find_element_by_id("liLoginAuthenticated")
            # exit.click()
            # exit = lf.drv.find_element_by_id("butLoginPartial")
            # exit.click()
            # time.sleep(5)
            # print("b232")
            # Utils.waitFadeIn(lf.drv)

            # time.sleep(5)

        except:
            pass







