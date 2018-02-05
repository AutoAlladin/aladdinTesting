from datetime import time
from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from Aladdin.Accounting.decorators.StoreTestResult import add_res_to_DB
from Prozorro.Utils import waitFadeIn


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
            with self.subTest("проверка " + wait_text):
                element = WebDriverWait(self.wts.drv, 20).until(
                    expected_conditions.visibility_of_element_located(locator))
                self.assertIsNotNone(element, "Проверка надписей, элемент  не найден  "+str(locator))
                self.assertEqual(element.text, wait_text,"не совпадают значение в интерфейсе и ожидаемое")
                self.log("element.text = "+wait_text)

        if lang=='en':
            check((By.ID, 'hrefPurchases'), "Tenders")
            check((By.XPATH, ".//*[@id='navigation']/div/button[1]"), "Clear")
            check((By.XPATH, ".//*[@id='headingTwo']/div/span"), "Type of procedure".upper())
            check((By.XPATH, ".//*[@id='headingOne']/div"), "Stages".upper())
            check((By.XPATH, ".//*[@id='headingThree']/div"), "Delivery region".upper())
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
            check((By.XPATH, ".//*[@id='headingThree']/div"), "Регион доставки".upper())
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
            check((By.XPATH, ".//*[@id='headingThree']/div"), "Регіон доставки".upper())
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

        with self.subTest('главное меню'):
            xpath = '//a[@class="dropdown-toggle"]/i[@class="pe-7s-menu"]/..'
            element =WebDriverWait(self.wts.drv, 20).until(
                expected_conditions.visibility_of_element_located(
                        (By.XPATH, xpath)
                        )
                    )
            self.assertIsNotNone(element, "Элемент меню не найден  "+xpath)
            self.log("subTest('меню') OK")

        with self.subTest('переключение языка интерфейса'):
            xpath = "//li[@id='liCultureSelector']"
            element = WebDriverWait(self.wts.drv, 20).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, xpath)
                )
            )
            self.assertIsNotNone(element, "Элемент мова не найден  " + xpath)
            self.log("subTest('мова') OK")


        with self.subTest('меню авторизации'):
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

        with self.subTest('английский интерфейс'):
            try:
                xpath = "//a[@id='select_lang_en-us']"
                select_lang_en = WebDriverWait(self.wts.drv, 20).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, xpath)))

                self.assertIsNotNone(select_lang_en, "Элемент select_lang_en не найден  " + xpath)
                select_lang_en.click()
                self.log("select_lang_en CLICK OK")

                self.check_labels('en')

            except Exception as e :
                self.assertEqual(True, False, "select_lang_en-us - "+e.__str__())

        with self.subTest("русский интерфейс"):
            try:
                self.wts.drv.find_element_by_id('liCultureSelector').click()

                xpath = "//a[@id='select_lang_ru-ru']"
                select_lang_en = WebDriverWait(self.wts.drv, 20).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, xpath)))

                self.assertIsNotNone(select_lang_en, "Элемент select_lang_ru-ru не найден  " + xpath)
                select_lang_en.click()
                self.log("select_lang_ru-ru CLICK OK")

                self.check_labels('ru')

            except Exception as e :
                self.assertEqual(True, False, "select_lang_ru-ru - "+e.__str__())


        with self.subTest("украинский интерфейс"):
            try:
                self.wts.drv.find_element_by_id('liCultureSelector').click()

                xpath = "//a[@id='select_lang_uk-ua']"
                select_lang_en = WebDriverWait(self.wts.drv, 20).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, xpath)))

                self.assertIsNotNone(select_lang_en, "Элемент select_lang_uk-ua не найден  " + xpath)
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
            with self.subTest("список тендеров"):
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
            #xpath_first  = '//ul[@class="pagination"]//a[@ng-click="selectPage(1)"]'
            #xpath_last = '//ul[@class="pagination"]//a[@ng-click="selectPage(totalPages)"]'

            xpath_prev   = '//ul[@class="pagination"]//a[@ng-click="selectPage(page - 1)"]'
            xpath_next   = '//ul[@class="pagination"]//a[@ng-click="selectPage(page + 1)"]'


            with self.subTest("выбор страницы с тендерами по номеру"):
                pagi_number = WebDriverWait(self.wts.drv, 20).until(
                    expected_conditions.visibility_of_any_elements_located((By.XPATH, xpath_number)))

                self.assertIsNotNone(pagi_number, "Элемент pagi_number не найден  " + xpath_number)
                self.assertGreater(len(pagi_number), 0, "Нет страниц в списке " + xpath_number)
                self.log("Кнопки перехода на выбраные страницы пагинации ОК " + str(len(pagi_number)))

            # with self.subTest("pagi_first"):
            #     pagi_first = WebDriverWait(self.wts.drv, 20).until(
            #         expected_conditions.visibility_of_element_located((By.XPATH, xpath_first)))
            #     self.assertIsNotNone(pagi_first, "Элемент pagi_first не найден  " + xpath_first)
            #     self.log("Кнопка \"Первая страница\" пагинации ОК " + xpath_first)

            with self.subTest("выбор предыдущей страницы с тендерами"):
                pagi_prev = WebDriverWait(self.wts.drv, 20).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, xpath_prev)))
                self.assertIsNotNone(pagi_prev, "Элемент pagi_prev не найден  " + xpath_prev)
                self.log("Кнопка \"Предыдущая страница\" пагинации ОК " + xpath_prev)

            with self.subTest("выбор следующей страницы с тендерами"):
                pagi_next = WebDriverWait(self.wts.drv, 20).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, xpath_next)))
                self.assertIsNotNone(pagi_next, "Элемент pagi_next не найден  " + xpath_next)
                self.log("Кнопка \"Следующая страница\" пагинации ОК " + xpath_next)

            # with self.subTest("pagi_last"):
            #     pagi_last = WebDriverWait(self.wts.drv, 20).until(
            #         expected_conditions.visibility_of_element_located((By.XPATH, xpath_last)))
            #     self.assertIsNotNone(pagi_last, "Элемент pagi_last не найден  " + xpath_last)
            #     self.log("Кнопка \"Последняя страница\" пагинации ОК " + xpath_last)

        except Exception as e:
            self.assertEqual(True, False, "PAGINATION - " + e.__str__())


        try:
            self.log("Элементы отдельного тендера")

            with self.subTest("отображение первого тендера в списке"):
                one_tender=WebDriverWait(self.wts.drv, 20).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='purchase-page']/div/div[@class='col-md-12'][2]")))
                self.assertIsNotNone(one_tender)

            with self.subTest("заголовок первого тендера в списке"):
                title =one_tender.find_element_by_xpath("//p/a")
                self.assertIsNotNone(title, "Элемент title не найден")
                self.log("заголовок ОК - "+title.text)

            with self.subTest("название заказчика первого тендера в списке"):
                owner_name = one_tender.find_element_by_xpath("//small[contains(@id,'companyName')]")
                self.assertIsNotNone(owner_name, "Элемент owner_name не найден")
                self.log("название закупщика ОК - "+owner_name.text)

            with self.subTest("ИД прозорро первого тендера в списке"):
                ID = one_tender.find_element_by_xpath("//span[@class='spanProzorroId']")
                self.assertIsNotNone(ID, "Элемент ID не найден")
                self.log("ИД прозорро ОК - "+ID.text)

            with self.subTest("тип процедуры первого тендера в списке"):
                proc_type = one_tender.find_element_by_xpath("//div[@class='col-md-6']/span/span[3]")
                self.assertIsNotNone(proc_type, "Элемент proc_type не найден")
                self.log("тип процедуры ОК - "+proc_type.text)

            with self.subTest("этап первого тендера в списке"):
                status = one_tender.find_element_by_xpath("//div[@class='project-label text-success']/span")
                self.assertIsNotNone(status, "Элемент status не найден")
                self.log("этап  тендера ОК - "+status.text)

            with self.subTest("дата модификации первого тендера в списке"):
                mode_time = one_tender.find_element_by_xpath("//div[@class='row row-with-purchase-times']/div[3]/span")
                self.assertIsNotNone(mode_time, "Элемент mode_time не найден")
                self.log("дата  модификации ОК - "+mode_time.text)


        except Exception as e:
            self.assertEqual(True, False, "TENDER PANEL - " + e.__str__())

    @add_res_to_DB(test_name='Поиск тендеров')
    def tab_search(self):
        id_searchType='searchType'
        id_findbykeywords='findbykeywords'
        id_butSimpleSearch='butSimpleSearch'
        id_clear_all="clear_all"
        xpath_activ="//span[@id='topActiveStatusWrap']"
        xpath_done="//span[@id='topOverStatusWrap']"
        xpath_archive="//span[@id='topArchiveStatusWrap']"
        id_excell="IdExportExcelButton"
        xpath_page_total="//div[contains(@class,'pager-total')]/span"

        try:
            with self.subTest("типы поиска тедера"):
                select_searchType = WebDriverWait(self.wts.drv, 5).until(
                    expected_conditions.visibility_of_element_located((By.ID, id_searchType)))
                self.assertIsNotNone(select_searchType, "Элемент select_searchType не найден  " + id_searchType)
                self.log("Выбор типов поиска ОК - " + id_searchType)

            searchType_text={"Шукати:","По назві","Системному номеру (у форматі UA-....)","По опису"}

            with self.subTest("названия типов поиска"):
                xpat = "//select[@id='searchType']/option"
                searchType_option = self.wts.drv.find_elements_by_xpath(xpat)
                self.assertIsNotNone(searchType_option, "Элемент searchType_option не найден  " + xpat)
                self.assertGreater(len(searchType_option),0, "Количество типов поиска !=4 : "+str(len(searchType_option)))
            for value in searchType_option:
                with self.subTest("searchType_optionText"):
                    self.assertIn(value.text, searchType_text, "Невалидный текст типа поиска - "+value.text)
            self.log("Названия типов поиска ОК")

        except Exception as e:
            self.assertEqual(True, False, "select_searchType - " + e.__str__())

        with self.subTest("поле ввода текста поиска") :
            findbykeywords = WebDriverWait(self.wts.drv, 5).until(
                expected_conditions.visibility_of_element_located((By.ID, id_findbykeywords)))
            self.assertIsNotNone(findbykeywords, "Элемент findbykeywords не найден  " + id_findbykeywords)
            # findbykeywords.clear()
            # findbykeywords.send_keys("xxx")
            # self.assertEqual(findbykeywords.text, "xxx")
            self.log("Текст поиска ОК - " + id_findbykeywords)

        with self.subTest("кнопка поиска"):
            butSimpleSearch = WebDriverWait(self.wts.drv, 5).until(
                expected_conditions.visibility_of_element_located((By.ID, id_butSimpleSearch)))
            self.assertIsNotNone(butSimpleSearch, "Элемент butSimpleSearch не найден  " + id_butSimpleSearch)
            self.log("Кнопка поиска ОК - " + id_butSimpleSearch)

        with self.subTest("элемент очистить все"):
            clear_all = WebDriverWait(self.wts.drv, 5).until(
                expected_conditions.visibility_of_element_located((By.ID, id_clear_all)))
            self.assertIsNotNone(clear_all, "Элемент butSimpleSearch не найден  " + id_clear_all)
            self.log("Кнопка очистки поиска ОК - " + id_clear_all)

        with self.subTest("попытка найти повторно первый тендер из списка"):
            one_tender = WebDriverWait(self.wts.drv, 5).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, "//div[@id='purchase-page']/div/div[@class='col-md-12'][2]")))

            id = one_tender.find_element_by_xpath("//span[@class='spanProzorroId']")
            select_searchType = WebDriverWait(self.wts.drv, 5).until(
                expected_conditions.visibility_of_element_located((By.ID, id_searchType)))
            Select(select_searchType).select_by_visible_text("Системному номеру (у форматі UA-....)")
            butSimpleSearch = WebDriverWait(self.wts.drv, 5).until(
                expected_conditions.visibility_of_element_located((By.ID, id_butSimpleSearch)))
            findbykeywords = WebDriverWait(self.wts.drv, 5).until(
                expected_conditions.visibility_of_element_located((By.ID, id_findbykeywords)))
            findbykeywords.clear()
            findbykeywords.send_keys(id.text)
            butSimpleSearch.click()
            # sleep(10)
            # wanted_tender = WebDriverWait(self.wts.drv, 15).until(
            #     expected_conditions.visibility_of_any_elements_located(
            #         (By.XPATH, "//div[@id='purchase-page']/div/div[@class='col-md-12']")))
            #
            # self.assertIsNotNone(wanted_tender, "Тендер "+id.text+" не найден, хотя он есть :(  " )
            self.log("Поиск тендера КАКБЫ ОК но не совсем - нужны доработки по структруе страницы - " + id.text)

        with self.subTest("чекбокс активные тендера"):
            label = WebDriverWait(self.wts.drv, 5).until(
                expected_conditions.visibility_of_element_located((By.XPATH, xpath_activ)))
            self.assertIsNotNone(label, "Элемент label_active не найден  " + xpath_activ)
            self.log("Чекбокс активные ОК - " + xpath_activ)

        with self.subTest("чекбокс завершенные тендера"):
            label = WebDriverWait(self.wts.drv, 5).until(
                expected_conditions.visibility_of_element_located((By.XPATH, xpath_done)))
            self.assertIsNotNone(label, "Элемент label_done не найден  " + xpath_done)
            self.log("Чекбокс завершенные ОК - " + xpath_done)

        with self.subTest("чекбокс архивные тендера"):
            label = WebDriverWait(self.wts.drv, 5).until(
                expected_conditions.visibility_of_element_located((By.XPATH, xpath_archive)))
            self.assertIsNotNone(label, "Элемент label_archive не найден  " + xpath_archive)
            self.log("Чекбокс архивные ОК - " + xpath_archive)

        with self.subTest("кнопка занрузки в ексель"):
            button = WebDriverWait(self.wts.drv, 5).until(
                expected_conditions.visibility_of_element_located((By.ID, id_excell)))
            self.assertIsNotNone(button, "Элемент id_excell не найден  " + id_excell)
            waitFadeIn(self.wts.drv)
            button.click()
            self.log("Кнопка сохранения в ексель ОК - " + id_excell)

        # with self.subTest("page_total"):
        #     page_total = WebDriverWait(self.wts.drv, 5).until(
        #         expected_conditions.visibility_of_element_located((By.XPATH, xpath_page_total)))
        #     self.assertIsNotNone(page_total, "Элемент page_total не найден  " + xpath_page_total)
        #     self.log("Всего страниц ОК - " +page_total.text+" - "+ xpath_page_total)

        with self.subTest("выбор сортировки"):
            xpath_orderingType = "//select[@ng-model='orderingType.selected']"
            orderingType = WebDriverWait(self.wts.drv, 5).until(
                expected_conditions.visibility_of_element_located((By.XPATH, xpath_orderingType)))
            self.assertIsNotNone(orderingType, "Элемент orderingType не найден  " + xpath_orderingType)
            self.log("Список способов сортировки ОК - " + " - " + xpath_orderingType)

            sort_list={'Сортувати по:','Бюджет за спаданням','Бюджет за зростанням',
                       'Дата публікації за зростанням','Дата публікації за спаданням'}

            with self.subTest("типы сортировки"):
                xpat = "//select[@ng-model='orderingType.selected']/option"
                orderingType_option = self.wts.drv.find_elements_by_xpath(xpat)
                self.assertIsNotNone(orderingType_option, "Элемент orderingType_option не найден  " + xpat)
                self.assertGreater(len(orderingType_option),0, "Количество типов сортировки !=5 : "+str(len(orderingType_option)))
            for value in orderingType_option:
                with self.subTest("тип сортировки - "+value.text):
                    self.assertIn(value.text, sort_list, "Невалидный текст типа сортировки - "+value.text)
            self.log("Названия типов сортировки ОК")

    @add_res_to_DB(test_name='Панель фильтров тендеров')
    def tab_filters(self):
        id_button_all = "butSelectFilterGeo"
        id_button_clear = "butClearFilterGeo"

        with self.subTest("фильтр по типам тендеров"):
            xpath_proc_type="//ul[@id='filterblock']/li/div[@id='headingTwo']"
            xpath_proc_labels="//div[@id='tender']/div/div/div/label"

            proc_type = WebDriverWait(self.wts.drv, 5).until(
                expected_conditions.visibility_of_element_located((By.XPATH, xpath_proc_type)))
            self.assertIsNotNone(proc_type, "Элемент proc_type filter не найден  " + xpath_proc_type)
            proc_type.click()

            with self.subTest("кнопка выбрать все"):
                button_all = WebDriverWait(self.wts.drv, 15).until(
                    expected_conditions.visibility_of_element_located((By.ID, id_button_all)))
                self.assertIsNotNone(button_all, "Элемент button_all filter не найден  " + id_button_all)
                button_all.click()
                self.log("Кнопка выбрать все типов тендеров ОК - " + id_button_all)

            with self.subTest("кнопка очистить все"):
                button_clear = WebDriverWait(self.wts.drv, 15).until(
                    expected_conditions.visibility_of_element_located((By.ID, id_button_clear)))
                self.assertIsNotNone(button_clear, "Элемент button_clear filter не найден  " + id_button_clear)
                button_clear.click()
                self.log("Кнопка очистить все типов тендеров ОК - " + id_button_all)

            proc_labels = WebDriverWait(self.wts.drv, 5).until(
                expected_conditions.visibility_of_any_elements_located((By.XPATH, xpath_proc_labels)))
            self.assertIsNotNone(proc_labels, "Элемент proc_labels  не найден  " + xpath_proc_labels)
            self.assertEqual(len(proc_labels), 12 , "Типов процедур !=12 : "+ str(len(proc_labels)) )

            proc_labels_text ={'Відкриті торги','Відкриті торги для закупівлі енергосервісу',
                'Відкриті торги з публікацією англійською мовою','Допорогова закупівля',
                'Звіт про укладені договори','Конкурентний діалог',
                'Конкурентний діалог (2ий етап)','Конкурентний діалог з публікацією англійською мовою',
                'Конкурентний діалог з публікацією англійською мовою (2ий етап)',
                'Переговорна процедура для потреб оборони','Переговорна процедура закупівлі',
                'Переговорна процедура скорочена'
            }

            for value in proc_labels:
                with self.subTest("тип тендерп - "+value.text):
                    self.assertIn(value.text, proc_labels_text, "Невалидный текст типа тендера - "+value.text)
            self.log("Названия типов тендера ОК ")
            proc_type.click()

            self.log("Фильтр типов тендеров ОК - " + xpath_proc_type)

        with self.subTest('фильтр по этапам тендеров'):
            id_tenderEtap = "headingOne"
            xpath_tenderEtap_label="//div[@id='tenderEtap']/div/div/div/label"

            tenderEtap = WebDriverWait(self.wts.drv, 5).until(
                expected_conditions.visibility_of_element_located((By.ID, id_tenderEtap)))
            self.assertIsNotNone(tenderEtap, "Элемент tenderEtap filter не найден  " + id_tenderEtap)
            tenderEtap.click()

            with self.subTest("кнопка выбрать все"):
                id_button_all = "//div[@id='tenderEtap']//button[@id='butSelectFilterGeo']"
                button_all = WebDriverWait(self.wts.drv, 10).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, id_button_all)))
                self.assertIsNotNone(button_all, "Элемент button_all filter не найден  " + id_button_all)
                button_all.click()
                self.log("Кнопка выбрать все типов тендеров ОК - " + id_button_all)

            with self.subTest("кнопка очистить все"):
                id_button_clear ="//div[@id='tenderEtap']//button[@id='butClearFilterGeo']"
                button_clear = WebDriverWait(self.wts.drv, 10).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, id_button_clear)))
                self.assertIsNotNone(button_clear, "Элемент button_clear filter не найден  " + id_button_clear)
                button_clear.click()
                self.log("Кнопка очистить все типов тендеров ОК - " + id_button_clear)

            tenderEtap_labels = WebDriverWait(self.wts.drv, 15).until(
                expected_conditions.visibility_of_any_elements_located((By.XPATH, xpath_tenderEtap_label)))
            self.assertIsNotNone(tenderEtap_labels, "Элемент tenderEtap_labels  не найден  " + xpath_tenderEtap_label)
            self.assertEqual(len(tenderEtap_labels), 16, "Этапов тендера !=16 : " + str(len(tenderEtap_labels)))

            tenderEtap_labels_text = {'Чернетка', 'Публікація торгів/планів',
                                'Період уточнень','Подача пропозицій',
                                'Період аукціону','Кваліфікація',
                                'Намір укласти договір','Торги відмінено',
                                'Завершено','Відмінена',
                                'Прекваліфікація','Оприлюднення укладеного договору',
                                'Чернетка 2-го етапу (конкурентний діалог)',
                                'Опубліковано протокол розгляду',
                                'Очікування початку 2-го етапу (технічний етап)',
                                'Проміжок між прийняттям рішення і появою тендеру 2'
                                }

            for value in tenderEtap_labels:
                with self.subTest("этап тендера - "+value.text):
                    self.assertIn(value.text, tenderEtap_labels_text, "Невалидный текст этапа тендера - "+value.text)
            self.log("Названия этапов тендера ОК ")
            tenderEtap.click()

            self.log("Фильтр этапов тендеров ОК - " + id_tenderEtap)

        with self.subTest('фильр по регионам доставки'):
            id_regions = "headingThree"
            xpath_regions_label="//div[@id='collapseFour']/div/div/div/label"

            regions = WebDriverWait(self.wts.drv, 5).until(
                expected_conditions.visibility_of_element_located((By.ID, id_regions)))
            self.assertIsNotNone(tenderEtap, "Элемент regions filter не найден  " + id_regions)
            regions.click()
            self.log("Фильтр регионов visible ОК - " + id_regions)

            self.wts.drv.execute_script("$('#navigation').slimScroll({ scrollTo: '100px' })")

            with self.subTest("кнопка выбрать все"):
                id_button_all = "//div[@id='collapseFour']//button[@id='butSelectFilterGeo']"
                button_all = WebDriverWait(self.wts.drv, 10).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, id_button_all)))
                self.assertIsNotNone(button_all, "Элемент button_all filter не найден  " + id_button_all)
                button_all.click()
                self.log("Кнопка выбрать все регионы ОК - " + id_button_all)

            with self.subTest("кнопка очистить все"):
                id_button_clear ="//div[@id='collapseFour']//button[@id='butClearFilterGeo']"
                button_clear = WebDriverWait(self.wts.drv, 10).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, id_button_clear)))
                self.assertIsNotNone(button_clear, "Элемент button_clear filter не найден  " + id_button_clear)
                button_clear.click()
                self.log("Кнопка очистить все регионы ОК - " + id_button_clear)

            regions_label = WebDriverWait(self.wts.drv, 15).until(
                expected_conditions.visibility_of_any_elements_located((By.XPATH, xpath_regions_label)))
            self.assertIsNotNone(regions_label, "Элемент regions_label  не найден  " + xpath_regions_label)
            self.assertEqual(len(regions_label), 26, "Регионов !=26 : " + str(len(regions_label)))
            self.log("Количесвто регионов ОК - " + str(len(regions_label)))

            regions_labels_text = {
                'Відповідно до тендерної документації', 'Автономна Республіка Крим',
                'Вінницька', 'Волинська', 'Дніпропетровська', 'Донецька',
                'Житомирська', 'Закарпатська', 'Запорізька', 'Івано-Франківська',
                'Київська','Кіровоградська','Луганська','Львівська','Миколаївська',
                'Одеська','Полтавська','Рівненська','Сумська','Тернопільська',
                'Харківська','Херсонська','Хмельницька','Черкаська','Чернівецька',
                'Чернігівська'
            }

            for value in regions_label:
                with self.subTest("регион - "+value.text):
                    self.assertIn(value.text, regions_labels_text, "Невалидное название региона - " + value.text)
            self.log("Названия регионов ОК ")

            self.wts.drv.execute_script("$('#navigation').slimScroll({ scrollTo: '-100px' })")
            regions.click()

            self.log("Фильтр регионов ОК - " + id_regions)

        with self.subTest("фильтр по классификаторам"):
            id_dkHelpers = "dkHelpers"

            xpath_cpv = "//a[@property='CPV']"
            xpath_cpv_dialog = "//div[@id='modDialog']//h4['CPV']"

            xpath_dk = "//a[@property='Other']"
            xpath_dk = "//div[@id='modDialog']//h4['Other']"

            xpath_kekv = "//a[@property='KEKV']"
            xpath__kekv= "//div[@id='modDialog']//h4['KEKV']"

            xpath_dialog_items = "//div[@id='dialogContent']//div[@id='tree']/ul/li"
            id_dk_search = "search-classifier-text"

            txt_cpv = "ДК021:2015"
            txt_dk = "Інші ДК"
            txt_kekv = "КЕКВ"

            with self.subTest("видимость фтльтров классификаторов"):
                dkHelpers = WebDriverWait(self.wts.drv, 5).until(
                    expected_conditions.visibility_of_element_located((By.ID, id_dkHelpers)))
                self.assertIsNotNone(tenderEtap, "Элемент dkHelpers filter не найден  " + id_dkHelpers)
                dkHelpers.click()
                self.log("Фильтр dkHelpers visible ОК - " + id_regions)

            with self.subTest("классификатор CPV"):
                cpv = WebDriverWait(self.wts.drv, 5).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, xpath_cpv)))
                self.assertIsNotNone(cpv, "Элемент CPV filter не найден  " + id_regions)

                self.assertEqual(cpv.text, txt_cpv, "CPV_LABEL "+cpv.text)
                self.log("Текст cpv OK - "+cpv.text)

                cpv.click()

                with self.subTest("диалог выбора CPV"):
                    dialog=WebDriverWait(self.wts.drv, 10).until(
                           expected_conditions.visibility_of_element_located((By.XPATH, xpath_cpv_dialog)))
                    self.log("Фильтр dialogCPV visible ОК - " + xpath_cpv_dialog)

                    dk_search = WebDriverWait(self.wts.drv, 10).until(
                        expected_conditions.visibility_of_element_located((By.ID, id_dk_search)))
                    self.log("Строка поиска dialogCPV visible ОК - " + id_dk_search )

                with self.subTest("выбор номенклатуры CPV"):
                    sleep(5)
                    dialog_items = WebDriverWait(self.wts.drv, 10).until(
                           expected_conditions.visibility_of_any_elements_located((By.XPATH, xpath_dialog_items)))
                    self.assertIsNotNone(dialog_items, "Элемент dialog_items  не найден  " + xpath_dialog_items)
                    self.assertGreater(len(dialog_items), 10, "Кодов <=10 : " + str(len(dialog_items)))
                    self.log("Много пунктов CPV ОК - " + str(len(dialog_items)))


                    button_close =   WebDriverWait(self.wts.drv, 10).until(
                           expected_conditions.visibility_of_element_located((By.XPATH,  "//div[@id='dialogContent']//button[contains(.,'Закрити')]")))
                    self.assertIsNotNone(button_close, "Элемент button_close диалога CPV не найден")
                    button_close.click()
                    self.log("Кнопка button_close диалога CPV ОК ")

                    WebDriverWait(self.wts.drv, 5).until(
                        expected_conditions.invisibility_of_element_located((By.XPATH, xpath_cpv_dialog)))
                    self.log("dialogCPV ОК")




