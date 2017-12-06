from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Prozorro.Utils import paint


class UserRegForm:
    def __init__(self, _drv):
        self.drv = _drv
        #self.drv =  webdriver.Chrome(_drv)
        self.UserName = self.drv.find_element_by_id("UserName")
        self.FullNameEn = self.drv.find_element_by_id("FullNameEn")
        self.Phone = self.drv.find_element_by_id("Phone")
        self.Email = self.drv.find_element_by_id("Email")
        self.Password = self.drv.find_element_by_id("Password")
        self.ConfirmPassword = self.drv.find_element_by_id("ConfirmPassword")
        self.btn_ok = self.drv.find_element_by_class_name("btn-success")

    def set_from_dic(self,company):
        user=company["Users"][0]
        self.UserName.send_keys(user["user_name"])
        self.FullNameEn.send_keys(user["user_name_eng"])
        self.Phone.send_keys(user["user_phone"])
        self.Email.send_keys(user["login"])
        self.Password.send_keys("123456")
        self.ConfirmPassword.send_keys("123456")
        self.drv.execute_script("$('#AgreementPolicy').click()")
        self.btn_ok.click()
        try:
            WebDriverWait(self.drv, 5).until(
                   expected_conditions.visibility_of_element_located((By.XPATH, "//md-tab-item[@aria-controls='tab-content-1']")))
        except:
            paint( self.drv,user["user_name"]+"ERROR.png" )
        print('register user', user["user_name"] )