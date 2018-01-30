# страница загружена, есть хотя бы один тендер на странице
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from Aladdin.Accounting.decorators.StoreTestResult import add_res_to_DB
from Prozorro.Pages.LoginPage import LoginPage


class Login_page(ParamsTestCase):

    @add_res_to_DB(test_name="Меню авторизации")
    def login_menu(self):
        with self.subTest("liLoginNoAuthenticated"):
            liLoginNoAuthenticated= WebDriverWait(self.wts.drv, 10).until(
                      expected_conditions.visibility_of_element_located((By.ID, "liLoginNoAuthenticated")))
            self.assertIsNotNone(liLoginNoAuthenticated, "Пункт меню  liLoginNoAuthenticated не найден")
            liLoginNoAuthenticated.click()
            self.log_subtest_res("login_menu_click OK")

        with self.subTest("butLoginPartial"):
            butLoginPartial= WebDriverWait(self.wts.drv, 10).until(
                      expected_conditions.visibility_of_element_located((By.ID, "butLoginPartial")))
            self.assertIsNotNone(butLoginPartial, "Пункт меню butLoginPartial не найден")
            self.log_subtest_res("Вхід visible OK")

        with self.subTest("butRegisterPartial"):
            butRegisterPartial= WebDriverWait(self.wts.drv, 10).until(
                      expected_conditions.visibility_of_element_located((By.ID, "butRegisterPartial")))
            self.assertIsNotNone(butRegisterPartial, "Пункт меню butRegisterPartial не найден")
            self.log_subtest_res("Реистрация visible OK")

        with self.subTest("bodyBoxToggle"):
            bodyBoxToggle= WebDriverWait(self.wts.drv, 10).until(
                      expected_conditions.visibility_of_element_located((By.ID, "bodyBoxToggle")))
            self.assertIsNotNone(bodyBoxToggle, "Пункт меню bodyBoxToggle не найден")
            self.log_subtest_res("Змінити режим єкрану OK")

    @add_res_to_DB(test_name="Форма авторизации - тексты")
    def check_lang(self):
        lform = self.parent_suite.suite_params["login_form"]

        with self.subTest("ru"):
            lform = lform.set_ru()

            self.assertEqual(lform.greeting.text,"Добро пожаловать на Aladdin Government")
            self.assertEqual(lform.label_for_email.text,"Электронная почта")
            self.assertEqual(lform.label_for_password.text,"Пароль")
            self.assertEqual(lform.msg_email.text,"Ваше уникальное имя пользователя")
            self.assertEqual(lform.msg_password.text,"Пароль")
            self.assertEqual(lform.remember_me_label.text, "Запомнить меня?")
            self.assertEqual(lform.remember_me_private.text,"(если это частный компьютер)")
            self.assertEqual(lform.btnLogin.text,"Вход")
            self.assertEqual(lform.register.text,"Регистрация")
            self.assertEqual(lform.restorePass.text,"Забыли пароль ?")

            self.log_subtest_res("Русский интекрфейс OK")


        with self.subTest("en"):
            lform = lform.set_en()

            self.assertEqual(lform.greeting.text,"Welcome to Aladdin Government")
            self.assertEqual(lform.label_for_email.text,"E-mail")
            self.assertEqual(lform.label_for_password.text,"Password")
            self.assertEqual(lform.msg_email.text,"Your unique username to app")
            self.assertEqual(lform.msg_password.text,"Password")
            self.assertEqual(lform.remember_me_label.text,"Remember me?")
            self.assertEqual(lform.remember_me_private.text,"(if this is a private computer)")
            self.assertEqual(lform.btnLogin.text,"Login")
            self.assertEqual(lform.register.text,"Registration")
            self.assertEqual(lform.restorePass.text,"Forgot password ?")

            self.log_subtest_res("Английский интерфейс OK")

        with self.subTest("ua"):
            lform = lform.set_ua()

            self.assertEqual(lform.greeting.text,"Ласкаво просимо до Aladdin Government")
            self.assertEqual(lform.label_for_email.text,"Електронна пошта")
            self.assertEqual(lform.label_for_password.text,"Пароль")
            self.assertEqual(lform.msg_email.text,"Ваше унікальне ім'я користувача")
            self.assertEqual(lform.msg_password.text,"Пароль")
            self.assertEqual(lform.remember_me_label.text, "Запам'ятати мене?")
            self.assertEqual(lform.remember_me_private.text,"(якщо це приватний комп'ютер)")
            self.assertEqual(lform.btnLogin.text,"Вхід")
            self.assertEqual(lform.register.text,"Реєстрація")
            self.assertEqual(lform.restorePass.text,"Забули пароль ?")

            self.log_subtest_res("Украинский интерфейс OK")

            self.parent_suite.suite_params.update({"login_form": lform})
            self.log_test_res("Text OK")

    @add_res_to_DB(test_name="Форма авторизации")
    def open_login(self):
        with self.subTest("butLoginPartial"):
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

        lform.login(self, login, password)

    @add_res_to_DB(test_name="Авторизация поставщиком")
    def login_provider(self):
        lform = self.parent_suite.suite_params["login_form"]

        login = self.parent_suite.suite_params["authorization"]["provider_login"]
        password = self.parent_suite.suite_params["authorization"]["provider_password"]

        lform.login(self, login, password)


# failed_login
# open_register_form
# open_restore_password