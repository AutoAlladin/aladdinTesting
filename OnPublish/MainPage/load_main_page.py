from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from Aladdin.Accounting.decorators.StoreTestResult import add_res_to_DB

class TabTest(ParamsTestCase):
    def tab_visible(self):
        pass

    def tab_list(self):
        pass

    def tab_filters(self):
        pass

    def tab_search(self):
        pass


class Load_main_page(ParamsTestCase):

    def check_labels(self, lang):
        def check(locator, wait_text):
            element = WebDriverWait(self.wts.drv, 20).until(
                expected_conditions.visibility_of_element_located(locator))
            self.assertIsNotNone(element, "Элемент tab_tenders не найден  "+str(locator))
            self.log(wait_text + " VISIBLE")
            self.assertEqual(element.text, wait_text,
                             "Интерфейс английский, вкладка называется - " + element.text)
            self.log("element.text = "+wait_text)

        if lang=='en':
            check((By.ID, 'hrefPurchases'), "Tenders")
            check((By.XPATH, ".//*[@id='navigation']/div/button[1]"), "Clear")
            check((By.XPATH, ".//*[@id='headingTwo']/div/span"), "Type of procedure".upper())
            check((By.XPATH, ".//*[@id='headingOne']/div"), "Stages".upper())
            check((By.XPATH, ".//*[@id='headingThree']/div"), "Region".upper())
            check((By.XPATH, ".//*[@id='dkHelpers']/div"), "Reference nomenclatures".upper())
            check((By.XPATH, ".//*[@id='sumOfTenders']/div"), "Budget of the tender".upper())
            check((By.XPATH, ".//*[@id='filterblock']/li[6]/div[1]/div"), "Filter by dates".upper())
            check((By.XPATH, ".//*[@id='ownerOfTenders']/div"), "Organizer of the auction".upper())
            check((By.XPATH, ".//*[@id='wrapper']/div/div/div/div[1]/h2"), "Aladdin Government public procurement")
            check((By.XPATH, ".//*[@id='wrapper']/div/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/span[1]/label"), "Active")
            check((By.XPATH, ".//*[@id='wrapper']/div/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/span[2]/label"), "Completed")
            check((By.XPATH, ".//*[@id='wrapper']/div/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/span[3]/label"), "Archive")
            check((By.ID, "clear_all"), "Clear")

        elif lang=='ru':
            check((By.ID, 'hrefPurchases'), "Тендеры")
            check((By.XPATH, ".//*[@id='navigation']/div/button[1]"), "Очистить")
            check((By.XPATH, ".//*[@id='headingTwo']/div/span"), "Тип процедуры".upper())
            check((By.XPATH, ".//*[@id='headingOne']/div"), "Этапы".upper())
            check((By.XPATH, ".//*[@id='headingThree']/div"), "Регион".upper())
            check((By.XPATH, ".//*[@id='dkHelpers']/div"), "Справочник номенклатур".upper())
            check((By.XPATH, ".//*[@id='sumOfTenders']/div"), "Бюджет тендера".upper())
            check((By.XPATH, ".//*[@id='filterblock']/li[6]/div[1]/div"), "Фильтр по датам".upper())
            check((By.XPATH, ".//*[@id='ownerOfTenders']/div"), "Организатор торгов".upper())
            check((By.XPATH, ".//*[@id='wrapper']/div/div/div/div[1]/h2"), "Aladdin Government закупки")
            check((By.XPATH, ".//*[@id='wrapper']/div/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/span[1]/label"), "Активные")
            check((By.XPATH, ".//*[@id='wrapper']/div/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/span[2]/label"), "Завершенные")
            check((By.XPATH, ".//*[@id='wrapper']/div/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/span[3]/label"), "Архивные")
            check((By.ID, "clear_all"), "Очистить")


        elif lang == 'ua':
            check((By.ID, 'hrefPurchases'), "Тендери")
            check((By.XPATH, ".//*[@id='navigation']/div/button[1]"), "Очистити")
            check((By.XPATH, ".//*[@id='headingTwo']/div/span"), "Тип процедури".upper())
            check((By.XPATH, ".//*[@id='headingOne']/div"), "Етапи".upper())
            check((By.XPATH, ".//*[@id='headingThree']/div"), "Регіон".upper())
            check((By.XPATH, ".//*[@id='dkHelpers']/div"), "Довідник номенклатур".upper())
            check((By.XPATH, ".//*[@id='sumOfTenders']/div"), "Бюджет тендера".upper())
            check((By.XPATH, ".//*[@id='filterblock']/li[6]/div[1]/div"), "Фільтр по датам".upper())
            check((By.XPATH, ".//*[@id='ownerOfTenders']/div"), "Організатор торгів".upper())
            check((By.XPATH, ".//*[@id='wrapper']/div/div/div/div[1]/h2"), "Aladdin Government закупівлі")
            check((By.XPATH, ".//*[@id='wrapper']/div/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/span[1]/label"), "Активні")
            check((By.XPATH, ".//*[@id='wrapper']/div/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/span[2]/label"), "Завершені")
            check((By.XPATH, ".//*[@id='wrapper']/div/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/span[3]/label"), "Архівні")
            check((By.ID, "clear_all"), "Очистити")


    #страница загружена, есть хотя бы один тендер на странице
    @add_res_to_DB(test_name="Загрузка страницы")
    def page_loaded(self):
        xpath_tenders='//div[@id="purchase-page"]/div/div[@class="col-md-12"]'
        tenders = self.wts.drv.find_elements_by_xpath(xpath_tenders)
        self.assertGreater(len(tenders),0, "Нет тендеров на странице")
        self.log( "page_loaded OK")

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
            self.log("subTest('меню') OK")
            print("subTest('меню')", "OK")

        with self.subTest('мова'):
            xpath = "//li[@id='liCultureSelector']"
            element = WebDriverWait(self.wts.drv, 20).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, xpath)
                )
            )
            self.assertIsNotNone(element, "Элемент мова не найден  " + xpath)
            self.log("subTest('мова') OK")


        with self.subTest('вхід'):
            xpath = '//li[@id="liLoginNoAuthenticated"]/..'
            element = WebDriverWait(self.wts.drv, 20).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, xpath)
                )
            )
            self.assertIsNotNone(element, "Элемент вхід не найден  " + xpath)
            self.log("subTest('вхід') OK")

    @add_res_to_DB(test_name="Выбрать язык интерфейса")
    def set_lang(self):
        liCultureSelector = None
        try:
            xpath = "//li[@id='liCultureSelector']"
            liCultureSelector = WebDriverWait(self.wts.drv, 20).until(
                expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
            self.assertIsNotNone(liCultureSelector, "Элемент мова не найден  " + xpath)
            self.log("меню выбора языка ОК")

            liCultureSelector.click()
        except Exception as e :
            self.assertEqual(True, False, "liCultureSelector - "+e.__str__())

        with self.subTest('select_lang_en-us'):
            try:
                xpath = "//a[@id='select_lang_en-us']"
                select_lang_en = WebDriverWait(self.wts.drv, 20).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, xpath)))

                self.assertIsNotNone(select_lang_en, "Элемент select_lang_en не найден  " + xpath)
                self.log("select_lang_en VISIBLE")
                select_lang_en.click()
                self.log("select_lang_en CLICK OK")

                self.check_labels('en')


            except Exception as e :
                self.assertEqual(True, False, "select_lang_en-us - "+e.__str__())

        with self.subTest('select_lang_ru-ru'):
            try:
                self.wts.drv.find_element_by_id('liCultureSelector').click()

                xpath = "//a[@id='select_lang_ru-ru']"
                select_lang_en = WebDriverWait(self.wts.drv, 20).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, xpath)))

                self.assertIsNotNone(select_lang_en, "Элемент select_lang_ru-ru не найден  " + xpath)
                self.log("select_lang_ru-ru VISIBLE")
                select_lang_en.click()
                self.log("select_lang_ru-ru CLICK OK")

                self.check_labels('ru')

            except Exception as e :
                self.assertEqual(True, False, "select_lang_ru-ru - "+e.__str__())


        with self.subTest('select_lang_uk-ua'):
            try:
                self.wts.drv.find_element_by_id('liCultureSelector').click()

                xpath = "//a[@id='select_lang_uk-ua']"
                select_lang_en = WebDriverWait(self.wts.drv, 20).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, xpath)))

                self.assertIsNotNone(select_lang_en, "Элемент select_lang_uk-ua не найден  " + xpath)
                self.log("select_lang_uk-ua VISIBLE")
                select_lang_en.click()
                self.log("select_lang_uk-ua CLICK OK")

                self.check_labels('ua')
            except Exception as e :
                self.assertEqual(True, False, "select_lang_uk-ua - "+e.__str__())

class Tender_Tab(TabTest):
    @add_res_to_DB(test_name='Видно вкладку тендеров')
    def tab_visible(self):
        try:
            tab_tenders = WebDriverWait(self.wts.drv, 20).until(
                expected_conditions.visibility_of_element_located((By.ID, 'hrefPurchases')))
            self.assertIsNotNone(tab_tenders, "Элемент tab_tenders ID:hrefPurchases не найден")
            self.assertTrue(tab_tenders.is_displayed, "Элемент tab_tenders ID:hrefPurchases не видим")
            self.log("tab_tenders VISIBLE")
        except Exception as e:
            self.assertEqual(True, False, "tab_tenders - " + e.__str__())
        pass

    @add_res_to_DB(test_name='Список тендеров')
    def tab_list(self):

        self.log("Проверка пагинации")

        try:
            xpath = "//div[@id='purchase-page']//div[@class='col-md-12']"
            tender_list = WebDriverWait(self.wts.drv, 20).until(
                expected_conditions.visibility_of_any_elements_located((By.XPATH, xpath)))
            self.assertIsNotNone(tender_list, "Элемент tender_list не найден  " + xpath)
            self.assertGreater(len(tender_list),0, "Нет тендеров в списке " + xpath)
            self.log("количество тендеров "+str(len(tender_list)))

        except Exception as e :
            self.assertEqual(True, False, "tender_list - "+e.__str__())

        try:
            xpath_number = "//ul[@class='pagination']//a[@ng-click='selectPage(page.number)']"
            xpath_first  = '//ul[@class="pagination"]//a[@ng-click="selectPage(1)"]'
            xpath_prev   = '//ul[@class="pagination"]//a[@ng-click="selectPage(page - 1)"]'
            xpath_next   = '//ul[@class="pagination"]//a[@ng-click="selectPage(page + 1)"]'
            xpath_last   = '//ul[@class="pagination"]//a[@ng-click="selectPage(totalPages)"]'

            with self.subTest("pagi_number"):
                pagi_number = WebDriverWait(self.wts.drv, 20).until(
                    expected_conditions.visibility_of_any_elements_located((By.XPATH, xpath_number)))

                self.assertIsNotNone(pagi_number, "Элемент pagi_number не найден  " + xpath_number)
                self.assertGreater(len(pagi_number), 0, "Нет страниц в списке " + xpath_number)
                self.log("Кнопки перехода на выбраные страницы пагинации ОК " + str(len(pagi_number)))

            with self.subTest("pagi_first"):
                pagi_first = WebDriverWait(self.wts.drv, 20).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, xpath_first)))
                self.assertIsNotNone(pagi_first, "Элемент pagi_first не найден  " + xpath_first)
                self.log("Кнопка \"Первая страница\" пагинации ОК " + xpath_first)

            with self.subTest("pagi_prev"):
                pagi_prev = WebDriverWait(self.wts.drv, 20).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, xpath_prev)))
                self.assertIsNotNone(pagi_prev, "Элемент pagi_first не найден  " + xpath_prev)
                self.log("Кнопка \"Предыдущая страница\" пагинации ОК " + xpath_prev)

            with self.subTest("pagi_next"):
                pagi_next = WebDriverWait(self.wts.drv, 20).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, xpath_next)))
                self.assertIsNotNone(pagi_next, "Элемент pagi_next не найден  " + xpath_next)
                self.log("Кнопка \"Следующая страница\" пагинации ОК " + xpath_next)

            with self.subTest("pagi_last"):
                pagi_last = WebDriverWait(self.wts.drv, 20).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, xpath_last)))
                self.assertIsNotNone(pagi_last, "Элемент pagi_next не найден  " + xpath_last)
                self.log("Кнопка \"Следующая страница\" пагинации ОК " + xpath_last)

        except Exception as e:
            self.assertEqual(True, False, "PAGINATION - " + e.__str__())


        try:
            self.log("Элементы отдельного тендера")

            one_tender=WebDriverWait(self.wts.drv, 20).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='purchase-page']/div/div[@class='col-md-12'][2]")))
            self.assertIsNotNone(one_tender)

            title =one_tender.find_element_by_xpath("//p/a")
            self.assertIsNotNone(title, "Элемент title не найден")
            self.log("заголовок ОК - "+title.text)

            owner_name = one_tender.find_element_by_xpath("//div[contains(@ng-click,'clickOnCompanyInfo')]")
            self.assertIsNotNone(owner_name, "Элемент owner_name не найден")
            self.log("название закупщика ОК - "+owner_name.text)

            ID = one_tender.find_element_by_xpath("//span[@class='spanProzorroId']")
            self.assertIsNotNone(ID, "Элемент ID не найден")
            self.log("ИД прозорро ОК - "+ID.text)

            proc_type = one_tender.find_element_by_xpath("//div[@class='col-md-6']/span/span[3]")
            self.assertIsNotNone(proc_type, "Элемент proc_type не найден")
            self.log("тип процедуры ОК - "+proc_type.text)

            status = one_tender.find_element_by_xpath("//div[@class='project-label text-success']/span")
            self.assertIsNotNone(status, "Элемент status не найден")
            self.log("этап  тендера ОК - "+status.text)

            mode_time = one_tender.find_element_by_xpath("//div[@class='row row-with-purchase-times']/div[3]/span")
            self.assertIsNotNone(mode_time, "Элемент mode_time не найден")
            self.log("дата  модификации ОК - "+mode_time.text)


        except Exception as e:
            self.assertEqual(True, False, "TENDER PANEL - " + e.__str__())

    @add_res_to_DB(test_name='Панель фильтров тендеров')
    def tab_filters(self):
        id_searchType='searchType'
        id_findbykeywords='findbykeywords'
        id_butSimpleSearch='butSimpleSearch'
        id_clear_all="clear_all"
        xpath_activ="//span[@class='check-wrap']/input[@id='topStatus3']/../label"
        xpath_done="//span[@class='check-wrap']/input[@id='topStatus5']/../label"
        xpath_archive="//span[@class='check-wrap']/input[@id='topStatus4']/../label"
        xpath_excell="//button[contains(@ng-click,'postFilterExcel')]"   #IdExportExcelButton
        xpath_page_total="//div[contains(@class,'pager-total')]/span"


    @add_res_to_DB(test_name='Поиск тендеров')
    def tab_search(self):
        pass






