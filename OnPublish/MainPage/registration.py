from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from Aladdin.Accounting.decorators.StoreTestResult import add_res_to_DB
from Prozorro.Pages.LoginPage import LoginPage
from Prozorro.Pages.UserRegForm import UserRegForm


class Registartion(ParamsTestCase):

    @add_res_to_DB(test_name='Попытка входа без регистрации')
    def try_login(self):
        lf = None
        with self.subTest("авторизация"):
            url = self.parent_suite.suite_params["tender_json"]["start_url"]
            self.wts.drv.get(url)
            lf = LoginPage(self.wts.drv).login("tgedgdfgdfgdfg","23423v423v4")

        with self.subTest("ловим ошибки входа"):
            WebDriverWait(lf.drv, 2).until(
                expected_conditions.visibility_of_element_located(
                    (By.ID, "error")))
            error = lf.drv.find_element_by_id("error")

        self.assertEqual(error.text,"Невірна спроба входу в систему")
        self.parent_suite.suite_params.update({"login_form": lf})

    @add_res_to_DB(test_name="Открыть форму регистрации")
    def open_register_form(self):
        reg = self.parent_suite.suite_params["registartion_data"]
        lform = self.parent_suite.suite_params["login_form"]
        r = lform.open_register()
        r= UserRegForm()

        r.set_user_name(reg["user"]["user_name"])
        self.assertEqual(r.UserName.text,reg["user"]["user_name"])

        r.set_user_name_eng(reg["user"]["user_name_eng"])
        self.assertEqual(r.FullNameEn.text,reg["user"]["user_name_eng"])

        r.set_user_phone(reg["user"]["user_phone"])
        self.assertEqual(r.Phone.text,reg["user"]["user_phone"])

        r.set_login(reg["user"]["login"])
        self.assertEqual(r.Email.text,reg["user"]["login"])

        r.set_pas("123456")
        self.assertEqual(r.Password.text,"123456")

        r.set_confpas("123456")
        self.assertEqual(r.ConfirmPassword.text,"123456")


        r.set_agreement()
        # r.set_btn_ok()