from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from Aladdin.Accounting.decorators.StoreTestResult import add_res_to_DB
from Prozorro.Pages.LoginPage import LoginPage
from Prozorro.Pages.UserCompanyForm import UserCompanyForm
from Prozorro.Pages.UserRegForm import UserRegForm
from Prozorro.Utils import waitFadeIn


class Registartion(ParamsTestCase):

    @add_res_to_DB(test_name='Попытка входа без регистрации')
    def try_login(self):
        with self.subTest("авторизация"):
            url = self.parent_suite.suite_params["login_url"]
            self.wts.drv.get(url)
            LoginPage(self.wts.drv).login("tgedgdf@fgdfg.com","23423v423v4")

        with self.subTest("ловим ошибки входа"):
            WebDriverWait(self.wts.drv, 2).until(
                expected_conditions.visibility_of_element_located(
                    (By.ID, "error")))
            error = self.wts.drv.find_element_by_id("error")

        self.assertEqual(error.text,"Невірна спроба входу в систему")

    @add_res_to_DB(test_name="Открыть форму регистрации")
    def open_register_form(self):
        user = self.params["registartion_data"]["users"][0]

        old = user["login"]
        w = user["login"][4:9]
        user["login"] = "test"+str(int(w)+1).rjust(5, '0')+"@ukr.net"
        self.params["registartion_data"]["users"][0].update({"new_login":user["login"]})

        self.wts.__mongo__.test_params.update_one(
            {"_id":23, "company.users.login": old},
            {"$set":{"company.$.users.0.login":  user["login"]}})

        with self.subTest("заполнение полей"):
            self.wts.drv.get(self.parent_suite.suite_params["login_url"])
            r = LoginPage(self.wts.drv).open_register()

            r.set_user_name(user["user_name"])
            self.assertEqual(r.UserName.get_attribute('value') ,user["user_name"])

            r.set_user_name_eng(user["user_name_eng"])
            self.assertEqual(r.FullNameEn.get_attribute('value'),user["user_name_eng"])

            r.set_user_phone(user["user_phone"])
            self.assertEqual(r.Phone.get_attribute('value'),user["user_phone"])

            r.set_login(user["login"])
            self.assertEqual(r.Email.get_attribute('value'),user["login"])

            r.set_pas("123456")
            self.assertEqual(r.Password.get_attribute('value'),"123456")

            r.set_confpas("123456")
            self.assertEqual(r.ConfirmPassword.get_attribute('value'),"123456")

            r.set_agreement(None)

            r.set_btn_ok(None)
        with self.subTest("сообщения об ошибках"):
            self.wts.drv.implicitly_wait(0)
            try:
                WebDriverWait(self.wts.drv, timeout=1).until(
                        expected_conditions.invisibility_of_element_located(
                            (By.ID,'UserName-error')))
            except:
                self.assertIsNotNone(None,
                                     self.wts.drv.find_element_by_id('UserName-error').text
                                     )

            try:
                WebDriverWait(self.wts.drv, 1).until(
                        expected_conditions.invisibility_of_element_located(
                            (By.ID,'FullNameEn-error')))
            except:
                self.assertIsNotNone(None,
                                     self.wts.drv.find_element_by_id('FullNameEn-error').text
                                     )

            try:
                WebDriverWait(self.wts.drv, 1).until(
                    expected_conditions.invisibility_of_element_located(
                        (By.ID, 'Phone-error')))
            except:
                self.assertIsNotNone(None,
                                     self.wts.drv.find_element_by_id('Phone-error').text
                                     )

            try:
                WebDriverWait(self.wts.drv, 1).until(
                        expected_conditions.invisibility_of_element_located(
                            (By.ID,'Email-error')))
            except:
                self.assertIsNotNone(None,
                                     self.wts.drv.find_element_by_id('Email-error').text
                                     )
            try:
                WebDriverWait(self.wts.drv, 1).until(
                    expected_conditions.invisibility_of_element_located(
                        (By.ID, 'Password-error')))
            except:
                self.assertIsNotNone(None,
                                     self.wts.drv.find_element_by_id('Password-error').text
                                     )

            try:
                WebDriverWait(self.wts.drv, 1).until(
                    expected_conditions.invisibility_of_element_located(
                        (By.ID, 'ConfirmPassword-error')))
            except:
                self.assertIsNotNone(None,
                                     self.wts.drv.find_element_by_id('ConfirmPassword-error').text
                                     )

        WebDriverWait(self.wts.drv, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.ID, 'butLogoutPartial')))

    @add_res_to_DB(test_name='Создание компании')
    def reg_company(self):
        self.wts.drv.get(self.parent_suite.suite_params["login_url"])
        login = self.params["registartion_data"]["users"][0]["new_login"]
        cmpp =  self.params["registartion_data"]

        old = cmpp["subj_ident_code"]
        edr = str(int(old)+1).rjust(8,"0")
        cmpp.update({"old_subj_ident_code":old})
        cmpp["subj_ident_code"] = edr
        self.wts.__mongo__.test_params.update_one(
            {"_id": 23, "company.subj_ident_code": old },
            {"$set": {"company.$.subj_ident_code": edr}})


        with self.subTest("авторизация"):
            LoginPage(self.wts.drv).login(login,"123456")

        with self.subTest("вход в редактирование предприятия"):
            danger = self.wts.drv.find_element_by_xpath("//span[@class='label label-danger']")
            self.wts.drv.find_element_by_xpath("//a[@ng-click=\"userMenuClick('/Profile#/company')\"]/../../..").click()
            butCabinet = self.wts.drv.find_element_by_xpath("//a[@ng-click=\"userMenuClick('/Profile#/company')\"]")
            waitFadeIn(self.wts.drv)
            butCabinet.click()

            WebDriverWait(self.wts.drv, 5).until(
                expected_conditions.visibility_of_element_located(
                    (By.ID, "save_changes")))

        with self.subTest("редактирование предприятия"):
            cmF = UserCompanyForm(self.wts.drv)
            with self.subTest("форма собственности"):
                cmF.set_Ownership(cmpp["Ownership"])
                # self.assertEqual(cmF.select_type.get_attribute('value'), cmpp["Ownership"])

            with self.subTest("роль пользователя"):
                cmF.set_company_role(cmpp["company_role"])

            with self.subTest("полное название компании"):
                cmF.set_subj_legal_name(cmpp["subj_legal_name"])
                self.assertEqual(cmF.full_name.get_attribute('value'), cmpp["subj_legal_name"])

            with self.subTest("полное англ название компании"):
                cmF.set_subj_legal_name_eng(cmpp["subj_legal_name_eng"])
                self.assertEqual(cmF.full_name_en.get_attribute('value'), cmpp["subj_legal_name_eng"])

            with self.subTest("короткое название компании"):
                cmF.set_subj_short_name(cmpp["subj_short_name"])
                self.assertEqual(cmF.short_name.get_attribute('value'), cmpp["subj_short_name"])

            with self.subTest("короткое англ название компании"):
                cmF.set_subj_short_name_eng(cmpp["subj_short_name_eng"])
                self.assertEqual(cmF.short_name_en.get_attribute('value'), cmpp["subj_short_name_eng"])

            with self.subTest("код регистрации"):
                cmF.set_subj_ident_code(cmpp["subj_ident_code"])
                self.assertEqual(cmF.edrpou.get_attribute('value'), cmpp["subj_ident_code"])

            with self.subTest("телефон конторы"):
                cmF.set_subj_phone(cmpp["subj_phone"])
                self.assertEqual(cmF.phones0.get_attribute('value'), cmpp["subj_phone"])

            with self.subTest("почта конторы"):
                cmF.set_subj_email(cmpp["subj_email"])
                self.assertEqual(cmF.emails0.get_attribute('value'), cmpp["subj_email"])

            with self.subTest("хз"):
                cmF.set_state_company(cmpp["state_company"])
                # self.assertEqual(cmF..get_attribute('value'), cmpp[""])

            with self.subTest("тип кода регистрации"):
                cmF.set_subj_ident_scheme(cmpp["subj_ident_scheme"].strip())
                #self.assertEqual(cmF.select_scheme_edrpous.get_attribute('value'), cmpp["subj_ident_scheme"])

            with self.subTest("страна"):
                cmF.set_countries("Україна")
                #self.assertEqual(cmF.select_countries.get_attribute('value'), "Україна")

            with self.subTest("область"):
                cmF.set_addr_region(cmpp["addr_region"].strip())

            with self.subTest("город"):
                cmF.set_addr_locality(cmpp["addr_locality"])


            with self.subTest("улица"):
                cmF.set_addr_street(cmpp["addr_street"])

            with self.subTest("почтовый индекс"):
                cmF.set_addr_post_code(cmpp["addr_post_code"])

            self.wts.drv.execute_script("window.scroll(0, {0}-{1})".
                format(cmF.bankName_0.location.get("y"), 10))

            with self.subTest("банк"):
                cmF.set_bank_name(cmpp["bank_name"])
                self.assertEqual(cmF.bankName_0.get_attribute('value'), cmpp["bank_name"])

            with self.subTest("мфо банка"):
                cmF.set_mfo(cmpp["mfo"])
                self.assertEqual(cmF.mfo_0.get_attribute('value'), cmpp["mfo"])

            with self.subTest("номер счета"):
                cmF.set_account(cmpp["account"])
                self.assertEqual(cmF.bankAccount_0.get_attribute('value'), cmpp["account"])

            with self.subTest("сохранить компанию"):
                cmF.save_company()

        with self.subTest("перехват ошибок при сохранении предприятия"):
            try:
                WebDriverWait(self.wts.drv, 5).until(
                    expected_conditions.invisibility_of_element_located(
                        (By.XPATH, "//div[@id='toast-container']//div[@class ='toast-message']")))
            except:
                try:
                    msg = WebDriverWait(self.wts.drv, 1).until(
                        expected_conditions.visibility_of_element_located(
                            (By.XPATH, "//div[@id='toast-container']//div[@class ='toast-message']")))
                except:
                    pass
                raise msg

        WebDriverWait(self.wts.drv, 15).until(
            expected_conditions.visibility_of_element_located(
                (By.ID, "edit")))

        if "new_owner_login" not in self.parent_suite.suite_params :
            self.parent_suite.suite_params.update({"new_owner_login":login})
            self.parent_suite.suite_params.update({"new_owner_password":"123456"})
        elif "new_provider_login" not in self.parent_suite.suite_params :
            self.parent_suite.suite_params.update({"new_provider_login":login})
            self.parent_suite.suite_params.update({"new_provider_password":"123456"})
