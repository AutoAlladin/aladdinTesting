import json
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from Aladdin.Accounting.decorators.StoreTestResult import add_res_to_DB
from Prozorro.Pages.LoginPage import LoginPage
from Prozorro.Pages.TenderNew import TenderNew
from Prozorro.Utils import waitFadeIn


class Test_Below(ParamsTestCase):

    @add_res_to_DB(test_name="Меню создания тендеров")
    def create_menu(self):

        url = self.parent_suite.suite_params["login_url"]
        self.wts.drv.get(url)

        if "new_owner_login" in self.parent_suite.suite_params :
            with self.subTest("авторизация"):
                LoginPage(self.wts.drv).login(
                    self.parent_suite.suite_params["new_owner_login"],
                    self.parent_suite.suite_params["new_owner_password"]
                )
        else:
            with self.subTest("авторизация"):
                LoginPage(self.wts.drv).login(
                    self.parent_suite.suite_params["tender_json"]["below"]["login"],
                    self.parent_suite.suite_params["tender_json"]["below"]["password"]
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

            if self.parent_suite.suite_params['tender_json']['name'] == "below_and_bids":
                self.assertEqual(len(items), 10,
                               "Количество типов сортировки !=10 : " + str(len(items)))
            elif self.parent_suite.suite_params['tender_json']['name']=="realto_below_and_bids":
                self.assertEqual(len(items), 4,
                                 "Количество типов сортировки !=4 : " + str(len(items)))


            proc_list = {"План закупівлі", "Допорогова закупівля",
                         "Відкриті торги","Відкриті торги з публікацією англійською мовою",
                         "Звіт про укладені договори",
                         "Переговорна процедура для потреб оборони",
                         "Переговорна процедура закупівлі","Переговорна процедура скорочена",
                         "Конкурентний діалог", "Конкурентний діалог з публікацією англійською мовою",
                         "Відкриті торги для закупівлі енергосервісу"
                         }

            if self.parent_suite.suite_params['tender_json']['name'] == "realto_below_and_bids":
                proc_list.add('Простий тендер' )
                proc_list.add( 'Двоетапний тендер')
                proc_list.add( 'Запит цінових пропозицій')
            for value in items:
                with self.subTest("создать процедуру - "+value.text):
                    self.assertIn(value.text, proc_list, "Невалидный текст меню создания тендера - "+value.text)

    def select_below_menu_F(self):
        self.wts.drv.get(self.parent_suite.suite_params["start_url"])
        waitFadeIn(self.wts.drv)
        WebDriverWait(self.wts.drv, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.ID, "btn_create_purchase"))) \
            .click()

        waitFadeIn(self.wts.drv)
        with self.subTest("пункт меню создать Below"):
            WebDriverWait(self.wts.drv, 10).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, "//a[@href='/Purchase/Create/BelowThreshold']"))) \
                .click()

        WebDriverWait(self.wts.drv, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.ID, "next_step")))

    @add_res_to_DB(test_name="Выбор создания допорогового")
    def select_below_menu(self):
        self.select_below_menu_F()
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
        tn = tn.set_multilot(dic, "true")
        self.parent_suite.suite_params.update({"tender_new": tn})

    @add_res_to_DB(test_name="Допороговый - периоды")
    def set_dates(self):
        dic = self.parent_suite.suite_params["tender_json"]
        tn = self.parent_suite.suite_params["tender_new"]
        tn = tn.set_dates(dic).\
                click_next_button()

        WebDriverWait(self.wts.drv, 20).until(
            expected_conditions.visibility_of_element_located(
                (By.ID, "buttonAddNewLot")))

        # потому что в прозорро EndPurchaseController, а в rialto editPurchaseController
        div = self.wts.drv.find_element_by_xpath("//div[contains(@ng-controller,'ditPurchaseController')]")

        purchaseId=0
        if dic["name"] == "realto_below_and_bids":
            txt = div.get_attribute("data-ng-init")[23:-1]
            model = json.loads(txt)
            purchaseId = model["model"]["purchase"]["purchaseId"]
        else:
            txt = div.get_attribute("data-ng-init")[15:-1]
            model = json.loads(txt)
            purchaseId = model["purchase"]["purchaseId"]

        self.log(purchaseId)
        self.parent_suite.suite_params.update({"tender_new": tn})
        self.parent_suite.suite_params.update({"tenderID": purchaseId})

    @add_res_to_DB(test_name="Допороговый - + лот")
    def add_lot(self):
        dic = self.parent_suite.suite_params["tender_json"]
        tn = self.parent_suite.suite_params["tender_new"]
        tn = tn.add_lot(1, dic)
        self.parent_suite.suite_params.update({"tender_new": tn})

    @add_res_to_DB(test_name="Допороговый - + позиция")
    def add_item(self):
        dic = self.parent_suite.suite_params["tender_json"]
        tn = self.parent_suite.suite_params["tender_new"]
        tn = tn.add_item(dic, 1,1)
        self.parent_suite.suite_params.update({"tender_new": tn})

    @add_res_to_DB(test_name="Допороговый - + позиция")
    def add_item(self):
        dic = self.parent_suite.suite_params["tender_json"]
        tn = self.parent_suite.suite_params["tender_new"]
        tn = tn.add_item(dic, 1, 1).click_next_button()
        self.parent_suite.suite_params.update({"tender_new": tn})

    @add_res_to_DB(test_name="Допороговый - + параметр")
    def add_features(self):
        dic = self.parent_suite.suite_params["tender_json"]
        tn = self.parent_suite.suite_params["tender_new"]
        tn = tn.add_features(dic, 1, 1,2)
        self.parent_suite.suite_params.update({"tender_new": tn})

    @add_res_to_DB(test_name="Допороговый - + документ")
    def add_doc(self):
        dic = self.parent_suite.suite_params["tender_json"]
        tn = self.parent_suite.suite_params["tender_new"]
        tn = tn.add_doc(1)
        self.parent_suite.suite_params.update({"tender_new": tn})

    def open_draft_by_url_F(self):
        with self.subTest("открыть тендер"):
            id = self.parent_suite.suite_params["tenderID" ]
            url = self.parent_suite.suite_params["start_url"][:-1]
            url = url + "/" + str(id)
            self.wts.drv.get(url)

            WebDriverWait(self.wts.drv, 15).until(
                expected_conditions.visibility_of_element_located(
                    (By.ID, "goToListPurchase")))

    @add_res_to_DB(test_name="Допороговый - открыть тендер по урлу")
    def open_draft_by_url(self):
        self.open_draft_by_url_F()

    @add_res_to_DB(test_name="Допороговый - открыть тендер по урлу - изменить описание")
    def open_draft_by_url_edit(self):
        self.open_draft_by_url_F()

        waitFadeIn(self.wts.drv)
        WebDriverWait(self.wts.drv, 15).until(
            expected_conditions.visibility_of_element_located(
                (By.ID, "purchaseEdit")))\
        .click()
        save = WebDriverWait(self.wts.drv, 15).until(
            expected_conditions.visibility_of_element_located(
                (By.ID, "save_changes")))
        description = WebDriverWait(self.wts.drv, 15).until(
            expected_conditions.visibility_of_element_located(
                (By.ID, "description")))
        description.send_keys("отрекдактировано")
        waitFadeIn(self.wts.drv)
        save.click()
        waitFadeIn(self.wts.drv)
        WebDriverWait(self.wts.drv, 15).until(
            expected_conditions.visibility_of_element_located(
                (By.ID, "movePurchaseView")))\
        .click()
        waitFadeIn(self.wts.drv)
        WebDriverWait(self.wts.drv, 15).until(
            expected_conditions.visibility_of_element_located(
                (By.ID, "goToListPurchase")))

    @add_res_to_DB(test_name="Допороговый - открыть тендер по урлу - удалить")
    def open_draft_by_url_delete(self):
        waitFadeIn(self.wts.drv)
        WebDriverWait(self.wts.drv, 15).until(
            expected_conditions.visibility_of_element_located(
                (By.ID, "deletePurchase")))\
        .click()

        waitFadeIn(self.wts.drv)
        WebDriverWait(self.wts.drv, 15).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//div[@class='jconfirm-buttons']/button[1]")))\
        .click()

        waitFadeIn(self.wts.drv)
        WebDriverWait(self.wts.drv, 15).until(
            expected_conditions.visibility_of_element_located(
                (By.ID,"hrefPurchases")))

    @add_res_to_DB(test_name="Допороговый полный опубликовать")
    def create_below_publish(self):
        self.wts.drv.get(self.parent_suite.suite_params["login_url"])
        if "new_owner_login" in self.parent_suite.suite_params :
            with self.subTest("авторизация"):
                LoginPage(self.wts.drv).login(
                    self.parent_suite.suite_params["new_owner_login"],
                    self.parent_suite.suite_params["new_owner_password"]
                )
        else:
            with self.subTest("авторизация"):
                LoginPage(self.wts.drv).login(
                    self.parent_suite.suite_params["tender_json"]["below"]["login"],
                    self.parent_suite.suite_params["tender_json"]["below"]["password"]
                )

        self.select_below_menu_F()
        dic = self.parent_suite.suite_params["tender_json"]

        l=0
        i=1

        TenderNew(self.wts.drv). \
            set_description(dic, "Для подачі пропозицій "). \
            set_curr(). \
            set_multilot(dic, "false"). \
            set_dates(dic). \
            click_next_button(). \
            add_lot(l, dic). \
            add_item(dic,  lot=l, item=i). \
            click_next_button(). \
            add_features(dic, lots=l , items=i). \
            add_doc(1). \
            click_finish_edit_button(). \
            click_publish_button()

        tenderGUD = WebDriverWait(self.wts.drv, 25).until(
            expected_conditions.visibility_of_element_located(
                (By.ID, "purchaseProzorroId"))).text

        self.parent_suite.suite_params.update({"ProzorroId": tenderGUD})
        self.log(tenderGUD)









































