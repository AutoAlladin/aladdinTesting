from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from Aladdin.Accounting.decorators.StoreTestResult import add_res_to_DB


class Load_main_page(ParamsTestCase):

    # страница загружена, есть хотя бы один тендер на странице
    @add_res_to_DB(test_name="Загрузка страницы")
    def page_loaded(self):
        xpath_tenders='//div[@id="purchase-page"]/div/div[@class="col-md-12"]'
        tenders = self.wts.drv.find_elements_by_xpath(xpath_tenders)
        self.assertGreater(len(tenders),0, "Нет тендеров на странице")

    @add_res_to_DB(test_name="Кнопки меню")
    def menu_presented(self):
        #кнопка есть и кликабельна

        with self.subTest('меню'):
            xpath = '//a[@class="dropdown-toggle"]/i[@class="pe-7s-menu"]/..'
            element =WebDriverWait(self.wts.drv, 20).until(
                expected_conditions.visibility_of_element_located(
                        (By.XPATH, xpath)
                        )
                    )
            self.assertIsNotNone(element, "Элемент меню не найден  "+xpath)
            self.tlog.append("subTest('меню') OK")
            print("subTest('меню')", "OK")

        with self.subTest('мова'):
            xpath = "//li[@id='liCultureSelector']"
            element = WebDriverWait(self.wts.drv, 20).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, xpath)
                )
            )
            self.assertIsNotNone(element, "Элемент мова не найден  " + xpath)
            self.tlog.append("subTest('мова') OK")
            print("subTest('мова')", "OK")

        with self.subTest('вхід'):
            xpath = '//li[@id="liLoginNoAuthenticated"]/..'
            element = WebDriverWait(self.wts.drv, 20).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, xpath)
                )
            )
            self.assertIsNotNone(element, "Элемент вхід не найден  " + xpath)
            self.tlog.append("subTest('вхід') OK")
            print("subTest('вхід')", "OK")

    @add_res_to_DB(test_name="Выбрать язык интерфейса")
    def set_lang(self):
        liCultureSelector = None
        try:
            xpath = "//li[@id='liCultureSelector']"
            liCultureSelector = WebDriverWait(self.wts.drv, 20).until(
                expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
            self.assertIsNotNone(liCultureSelector, "Элемент мова не найден  " + xpath)
            self.tlog.append("меню выбора языка ОК")

            liCultureSelector.click()
        except Exception as e :
            self.assertEqual(True, False, "liCultureSelector - "+e.__str__())

        with self.subTest('select_lang_en-us'):
            try:
                xpath = "//a[@id='select_lang_en-us']"
                select_lang_en = WebDriverWait(self.wts.drv, 20).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, xpath)))

                self.assertIsNotNone(select_lang_en, "Элемент select_lang_en не найден  " + xpath)
                self.tlog.append("select_lang_en VISIBLE")
                select_lang_en.click()
                self.tlog.append("select_lang_en CLICK OK")

                tab_tenders = WebDriverWait(self.wts.drv, 20).until(
                    expected_conditions.visibility_of_element_located((By.ID, 'hrefPurchases')))
                self.assertIsNotNone(select_lang_en, "Элемент tab_tenders не найден  " + xpath)
                self.tlog.append("tab_tenders VISIBLE")

                self.assertEqual(tab_tenders.text, "Tenders", "Интерфейс английский, вкладка называется - "+tab_tenders.text)
                self.tlog.append("tab_tenders TEXT=Tenders")
            except Exception as e :
                self.assertEqual(True, False, "select_lang_en-us - "+e.__str__())

        with self.subTest('select_lang_ru-ru'):
            try:
                self.wts.drv.find_element_by_id('liCultureSelector').click()

                xpath = "//a[@id='select_lang_ru-ru']"
                select_lang_en = WebDriverWait(self.wts.drv, 20).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, xpath)))

                self.assertIsNotNone(select_lang_en, "Элемент select_lang_ru-ru не найден  " + xpath)
                self.tlog.append("select_lang_ru-ru VISIBLE")
                select_lang_en.click()
                self.tlog.append("select_lang_ru-ru CLICK OK")

                tab_tenders = WebDriverWait(self.wts.drv, 20).until(
                    expected_conditions.visibility_of_element_located((By.ID, 'hrefPurchases')))
                self.assertIsNotNone(select_lang_en, "Элемент tab_tenders не найден  " + xpath)
                self.tlog.append("tab_tenders VISIBLE")

                self.assertEqual(tab_tenders.text, "Тендеры", "Интерфейс русский, вкладка называется - "+ tab_tenders.text)
                self.tlog.append("tab_tenders TEXT=Тендеры")
            except Exception as e :
                self.assertEqual(True, False, "select_lang_ru-ru - "+e.__str__())

        with self.subTest('select_lang_uk-ua'):
            try:
                self.wts.drv.find_element_by_id('liCultureSelector').click()

                xpath = "//a[@id='select_lang_uk-ua']"
                select_lang_en = WebDriverWait(self.wts.drv, 20).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, xpath)))

                self.assertIsNotNone(select_lang_en, "Элемент select_lang_uk-ua не найден  " + xpath)
                self.tlog.append("select_lang_uk-ua VISIBLE")
                select_lang_en.click()
                self.tlog.append("select_lang_uk-ua CLICK OK")

                tab_tenders = WebDriverWait(self.wts.drv, 20).until(
                    expected_conditions.visibility_of_element_located((By.ID, 'hrefPurchases')))
                self.assertIsNotNone(select_lang_en, "Элемент tab_tenders не найден  " + xpath)
                self.tlog.append("tab_tenders VISIBLE")

                self.assertEqual(tab_tenders.text, "Тендери", "Интерфейс английский, вкладка называется - "+ tab_tenders.text)
                self.tlog.append("tab_tenders TEXT=Тендери")
            except Exception as e :
                self.assertEqual(True, False, "select_lang_uk-ua - "+e.__str__())









