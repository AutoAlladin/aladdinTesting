class UserRegForm:
    def __init__(self):
        self.UserName = self.drv.find_element_by_id("UserName")
        self.FullNameEn = self.drv.find_element_by_id("FullNameEn")
        self.Phone = self.drv.find_element_by_id("Phone")
        self.Email = self.drv.find_element_by_id("Email")
        self.Password = self.drv.find_element_by_id("Password")
        self.ConfirmPassword = self.drv.find_element_by_id("ConfirmPassword")
        self.AgreementPolicy =  self.drv.find_element_by_id("AgreementPolicy")
        self.btn_ok =  self.drv.find_element_by_class("btn btn-success")