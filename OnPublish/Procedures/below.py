import json

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from Aladdin.Accounting.decorators.StoreTestResult import add_res_to_DB
from Prozorro.Pages.LoginPage import LoginPage
from Prozorro.Pages.TenderNew import TenderNew
from Prozorro.Utils import waitFadeIn


class Test_Below(ParamsTestCase):
    """
    self.drv.find_element_by_xpath("").click()
    return TenderNew(self.drv). \
        set_description(dic, nom). \
        set_curr(). \
        set_multilot(dic, is_multilot). \
        set_dates(dic). \
        click_next_button(). \
        add_lot(lots, dic). \
        add_item(dic, lots, items). \
        click_next_button(). \
        add_features(dic, lots, features). \
        add_doc(docs). \
        click_finish_edit_button(). \
        click_publish_button()
    """

    @add_res_to_DB(test_name="Меню создания тендеров")
    def create_menu(self):
        # TODO push to parameter
        self.wts.drv.get('https://test-gov.ald.in.ua/Account/Login')

        with self.subTest("авторизация"):
            LoginPage(self.wts.drv).login(
                self.parent_suite.suite_params["authorization"]["owner_login"],
                self.parent_suite.suite_params["authorization"]["owner_password"]
            )

        with self.subTest("меню создать"):
            waitFadeIn(self.wts.drv)
            menu = WebDriverWait(self.wts.drv, 10).until(
                        expected_conditions.visibility_of_element_located(
                            (By.ID, "btn_create_purchase")))
            menu.click()

        with self.subTest("пункты меню создать"):
            items = WebDriverWait(self.wts.drv, 10).until(
                        expected_conditions.visibility_of_any_elements_located(
                            (By.XPATH, "//button[@id='btn_create_purchase']/../ul/li/a")))

            self.assertIsNotNone(items, "Элемент items не найден ")
            self.assertEqual(len(items), 10,
                               "Количество типов сортировки !=10 : " + str(len(items)))

            proc_list = {"План закупівлі", "Допорогова закупівля", "Відкриті торги","Відкриті торги з публікацією англійською мовою",
                         "Звіт про укладені договори", "Переговорна процедура закупівлі","Переговорна процедура скорочена",
                         "Конкурентний діалог", "Конкурентний діалог з публікацією англійською мовою",
                         "Відкриті торги для закупівлі енергосервісу"
                         }

            for value in items:
                with self.subTest("создать процедуру - "+value.text):
                    self.assertIn(value.text, proc_list, "Невалидный текст меню создания тендера - "+value.text)

    @add_res_to_DB(test_name="Выбор создания допорогового")
    def select_below_menu(self):
        # TODO push to parameter
        self.wts.drv.get('https://test-gov.ald.in.ua/purchases')
        waitFadeIn(self.wts.drv)
        WebDriverWait(self.wts.drv, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.ID, "btn_create_purchase")))\
        .click()
        with self.subTest("пункт меню создать Below"):
            WebDriverWait(self.wts.drv, 10).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, "//a[@href='/Purchase/Create/BelowThreshold']")))\
            .click()

            WebDriverWait(self.wts.drv, 10).until(
                expected_conditions.visibility_of_element_located(
                    (By.ID, "next_step")))

            self.parent_suite.suite_params.update({"tender_new": TenderNew(self.wts.drv) })

    @add_res_to_DB(test_name="Допороговый - тексты")
    def set_description(self):
        dic = self.parent_suite.suite_params["tender_json"]
        tn = self.parent_suite.suite_params["tender_new"]
        tn = tn.set_description(dic, "publish")
        self.parent_suite.suite_params.update({"tender_new": tn})

    @add_res_to_DB(test_name="Допороговый - валюта")
    def set_curr(self):
        dic = self.parent_suite.suite_params["tender_json"]
        tn = self.parent_suite.suite_params["tender_new"]
        tn = tn.set_curr()
        self.parent_suite.suite_params.update({"tender_new": tn})

    @add_res_to_DB(test_name="Допороговый - мультилоты")
    def set_multilot(self):
        dic = self.parent_suite.suite_params["tender_json"]
        tn = self.parent_suite.suite_params["tender_new"]
        tn = tn.set_multilot(dic, True)
        self.parent_suite.suite_params.update({"tender_new": tn})

    @add_res_to_DB(test_name="Допороговый - периоды")
    def set_dates(self):
        dic = self.parent_suite.suite_params["tender_json"]
        tn = self.parent_suite.suite_params["tender_new"]
        tn = tn.set_dates(dic).\
                click_next_button()

        WebDriverWait(self.wts.drv, 20).until(
            expected_conditions.visibility_of_element_located(
                (By.ID, "add_procurement_subject0")))

        div = self.wts.drv.find_element_by_xpath("//div[@ng-controller='endEditPurchaseController']")
        txt=div.get_attribute("data-ng-init")[15:-1]
        model = json.loads(txt)
        self.log(model["purchase"]["purchaseId"])
        self.parent_suite.suite_params.update({"tender_new": tn})
        self.parent_suite.suite_params.update({"tenderID": model["purchase"]["purchaseId"]})


    def create_simple_below(self):
        pass








































