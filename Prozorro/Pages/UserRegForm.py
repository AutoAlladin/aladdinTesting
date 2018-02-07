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
        try:
            self.UserName = WebDriverWait(self.drv, 10).until(
                  expected_conditions.visibility_of_element_located((By.ID,"UserName")))
        except:
            raise Exception("not UserName found")

        try:
            self.FullNameEn = WebDriverWait(self.drv, 10).until(
                expected_conditions.visibility_of_element_located((By.ID,"FullNameEn")))
        except:
            raise Exception("not FullNameEn found")
        try:
            self.Phone = WebDriverWait(self.drv, 10).until(
                expected_conditions.visibility_of_element_located((By.ID,"Phone")))
        except:
            raise Exception("not Phone found")
        try:
            self.Email = WebDriverWait(self.drv, 10).until(
                expected_conditions.visibility_of_element_located((By.ID,"Email")))
        except:
            raise Exception("not Email found")
        try:
            self.Password = WebDriverWait(self.drv, 10).until(
                expected_conditions.visibility_of_element_located((By.ID,"Password")))
        except:
            raise Exception("not Password found ")
        try:
            self.ConfirmPassword = WebDriverWait(self.drv, 10).until(
                expected_conditions.visibility_of_element_located((By.ID,"ConfirmPassword")))
        except:
            raise Exception("not ConfirmPassword found")
        try:
            self.btn_ok = WebDriverWait(self.drv, 10).until(
                expected_conditions.visibility_of_element_located((By.ID,"btn-success")))
        except:
            raise Exception("not btn-success found")


    def set_user_name (self,val):
        self.UserName.send_keys(val)

    def set_user_name_eng(self,val):
        self.FullNameEn.send_keys(val)

    def set_user_phone(self,val):
        self.Phone.send_keys(val)

    def set_login(self,val):
        self.Email.send_keys(val)

    def set_pas(self,val):
        self.Password.send_keys(val)

    def set_confpas(self,val):
        self.ConfirmPassword.send_keys(val)

    def set_agreement(self,val):
        self.drv.execute_script("$('#AgreementPolicy').click()")

    def set_btn_ok(self,val):
        self.btn_ok.click()

    def set_from_dic(self,company):
        user=company["Users"][0]
        self.set_user_name(user["user_name"])
        self.set_user_name_eng(user["user_name_eng"])
        self.set_user_phone(user["user_phone"])
        self.set_login(user["login"])
        self.set_pas("123456")
        self.set_confpas("123456")
        self.set_agreement()
        self.set_btn_ok()
        try:
            WebDriverWait(self.drv, 15).until(
                   expected_conditions.visibility_of_element_located((By.XPATH, "//span[@class='label label-danger")))
        except:
            paint( self.drv,user["user_name"]+"ERROR.png" )
        print('register user', user["user_name"] )