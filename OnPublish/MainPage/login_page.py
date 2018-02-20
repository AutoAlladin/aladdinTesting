from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from Aladdin.Accounting.decorators.StoreTestResult import add_res_to_DB
from Prozorro.Pages.LoginPage import LoginPage
from Prozorro.Utils import waitFadeIn


class Login_page(ParamsTestCase):

    @add_res_to_DB(test_name="Меню авторизации")
    def login_menu(self):
        with self.subTest("меню авторизации"):
            liLoginNoAuthenticated= WebDriverWait(self.wts.drv, 10).until(
                      expected_conditions.visibility_of_element_located((By.ID, "liLoginNoAuthenticated")))
            self.assertIsNotNone(liLoginNoAuthenticated, "Пункт меню  liLoginNoAuthenticated не найден")
            liLoginNoAuthenticated.click()
            self.log_subtest_res("login_menu_click OK")

        with self.subTest("подпункт вход"):
            butLoginPartial= WebDriverWait(self.wts.drv, 10).until(
                      expected_conditions.visibility_of_element_located((By.ID, "butLoginPartial")))
            self.assertIsNotNone(butLoginPartial, "Пункт меню butLoginPartial не найден")
            self.log_subtest_res("Вхід visible OK")

        with self.subTest("подпункт регистрации"):
            butRegisterPartial= WebDriverWait(self.wts.drv, 10).until(
                      expected_conditions.visibility_of_element_located((By.ID, "butRegisterPartial")))
            self.assertIsNotNone(butRegisterPartial, "Пункт меню butRegisterPartial не найден")
            self.log_subtest_res("Реистрация visible OK")

        with self.subTest("подпункт переключения режима экрана"):
            bodyBoxToggle= WebDriverWait(self.wts.drv, 10).until(
                      expected_conditions.visibility_of_element_located((By.ID, "bodyBoxToggle")))
            self.assertIsNotNone(bodyBoxToggle, "Пункт меню bodyBoxToggle не найден")
            self.log_subtest_res("Змінити режим єкрану OK")

    @add_res_to_DB(test_name="Форма авторизации - тексты")
    def check_lang(self):
        lform = self.parent_suite.suite_params["login_form"]

        def set_elements(ddd):
            with self.subTest("проверка текста єлемента"):
                self.assertEqual(lform.greeting.text, ddd["greeting"])
                self.assertEqual(lform.label_for_email.text, ddd["label_for_email"])
                self.assertEqual(lform.label_for_password.text, ddd["label_for_password"])
                self.assertEqual(lform.msg_email.text, ddd["msg_email"])
                self.assertEqual(lform.msg_password.text, ddd["msg_password"])
                self.assertEqual(lform.remember_me_label.text, ddd["remember_me_label"])
                self.assertEqual(lform.remember_me_private.text, ddd["remember_me_private"])
                self.assertEqual(lform.btnLogin.text, ddd["btnLogin"])
                self.assertEqual(lform.register.text, ddd["register"])
                self.assertEqual(lform.restorePass.text, ddd["restorePass"])
            
        with self.subTest("русский интерфейс"):
            lform = lform.set_ru()
            dic = self.parent_suite.suite_params["lang"]["ru"]
            set_elements(dic)
            self.log_subtest_res("Русский интекрфейс OK")

        with self.subTest("английский интерфейс"):
            lform = lform.set_en()
            dic = self.parent_suite.suite_params["lang"]["en"]
            set_elements(dic)
            self.log_subtest_res("Английский интерфейс OK")

        with self.subTest("украинский интерфейс"):
            lform = lform.set_ua()
            dic = self.parent_suite.suite_params["lang"]["ua"]
            set_elements(dic)
            self.log_subtest_res("Украинский интерфейс OK")

            self.parent_suite.suite_params.update({"login_form": lform})
            self.log_test_res("Text OK")

    @add_res_to_DB(test_name="Форма авторизации")
    def open_login(self):
        with self.subTest("открыть форму авторизации"):
            butLoginPartial = WebDriverWait(self.wts.drv, 10).until(
                expected_conditions.visibility_of_element_located((By.ID, "butLoginPartial")))
            self.assertIsNotNone(butLoginPartial, "Пункт меню butLoginPartial не найден")
            self.log_subtest_res("Вхід visible OK")

        butLoginPartial.click()
        login_form = LoginPage(self.wts.drv)
        self.assertIsNotNone(login_form, "Форма авторизации не загрузилась")
        self.parent_suite.suite_params.update({"login_form":login_form})

    @add_res_to_DB(test_name="Авторизация заказчиком")
    def login_owner(self):

        lform =  self.parent_suite.suite_params["login_form"]
        login = self.parent_suite.suite_params["authorization"]["owner_login"]
        password = self.parent_suite.suite_params["authorization"]["owner_password"]

        with self.subTest("авторизация"):
            lform.login(login, password)

        with self.subTest("повторный вход в форму авторизации"):

            waitFadeIn(self.wts.drv)
            WebDriverWait(self.wts.drv, 10).until(
                    expected_conditions.visibility_of_element_located((By.ID, "butLogoutPartial")))\
            .click()

            liLoginNoAuthenticated = WebDriverWait(self.wts.drv, 10).until(
                expected_conditions.visibility_of_element_located((By.ID, "liLoginNoAuthenticated")))
            liLoginNoAuthenticated.click()
            butLoginPartial = WebDriverWait(self.wts.drv, 10).until(
                expected_conditions.visibility_of_element_located((By.ID, "butLoginPartial")))
            waitFadeIn(self.wts.drv)
            butLoginPartial.click()
            login_form = LoginPage(self.wts.drv)
            self.parent_suite.suite_params.update({"login_form": login_form})

    @add_res_to_DB(test_name="Авторизация поставщиком")
    def login_provider(self):
        lform = None
        lform = self.parent_suite.suite_params["login_form"]

        login = self.parent_suite.suite_params["authorization"]["provider_login"]
        password = self.parent_suite.suite_params["authorization"]["provider_password"]

        with self.subTest("авторизация"):
            lform.login(login, password)

        with self.subTest("повторный вход в форму авторизации"):
            waitFadeIn(self.wts.drv)
            WebDriverWait(self.wts.drv, 10).until(
                    expected_conditions.visibility_of_element_located((By.ID, "butLogoutPartial")))\
            .click()

            liLoginNoAuthenticated = WebDriverWait(self.wts.drv, 10).until(
                expected_conditions.visibility_of_element_located((By.ID, "liLoginNoAuthenticated")))
            waitFadeIn(self.wts.drv)
            liLoginNoAuthenticated.click()
            butLoginPartial = WebDriverWait(self.wts.drv, 10).until(
                    expected_conditions.visibility_of_element_located((By.ID, "butLoginPartial")))
            waitFadeIn(self.wts.drv)
            butLoginPartial.click()
            login_form = LoginPage(self.wts.drv)
            self.parent_suite.suite_params.update({"login_form":login_form})

    @add_res_to_DB(test_name="Открыть восстановление пароля")
    def open_restore_password(self):
        self.wts.drv.get('https://test-gov.ald.in.ua/Account/Login')
        lform = LoginPage(self.wts.drv)
        lform.restorePass.click()
        WebDriverWait(self.wts.drv, 10).until(
            expected_conditions.visibility_of_element_located((By.ID, "butForgotPassword")))

    @add_res_to_DB(test_name="Открыть форму регистрации")
    def open_register_form(self):
        self.wts.drv.get(self.parent_suite.suite_params["login_url"])
        lform = LoginPage(self.wts.drv)
        lform.register.click()
        WebDriverWait(self.wts.drv, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//form[@action='/Account/Register']//button[@type='submit']")))
