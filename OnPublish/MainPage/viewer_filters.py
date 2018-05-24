import unittest
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase




class ViewerFilters(ParamsTestCase):

    def test_01_check_open(self):
        #кликаем на тип процедуры
        self.el = self.wts.w_id("headingTwo")
        sleep(5)
        self.el.click()


        #выбираем тип процедуры "Відкриті торги"
        self.ch_op_el = self.wts.w_xpath(".//*[@id='tender']/div/div/div[1]")
        self.ch_op_el_text = self.ch_op_el.text
        self.ch_op_el.click()

        #кликаем на кнопку "Шукати"
        self.search_button = self.wts.w_id("butSimpleSearch")
        self.search_button.click()
        sleep(5)
        #self.q = self.wts.execute_script("window.scrollTo(0, 1000)")

        #выбираем найденый тендер
        self.el = self.wts.w_xpath(
            ".//*[@id='purchase-page']/div/div[2]/div/div[2]/div/div[1]/span/span[3]")
        self.el_text = self.el.text

        #проверяем, что название выбранной процедуры совпадает с названием найденой процедуры
        self.assertEqual(self.ch_op_el_text, self.el_text)

        #кликаем на кнокпу "Очистити"
        self.clear_button = self.wts.w_id("butClearFilterGeo")
        self.clear_button.click()
        #self.clear_button.isDisplayed()

        # проверяем, что список процедур раскрылся (проверка на наличие кнопки "Вибрати все")
        # try:
        #     el = self.wts.find_element_by_css_selector("#butSelectFilterGeo")
        #     el_text = el.text
        #     print(el_text)
        #     self.el = self.wts.find_element_by_css_selector("#butSelectFilterGeo")
        # except NoSuchElementException:
        #     return False
        # return True

        #сворачиваем тип процедуры
        self.el = self.wts.w_id("headingTwo")
        self.el.click()
        sleep(3)


        # self.list_size = self.clear_button.size
        # print(self.list_size)
        #
        # if self.list_size['height'] == 0:
        #     print(self.list_size['height'])
            # return True

        test = self.clear_button.size['height']
        print("test")
        if test == 0:
            return True



        # if self.wts.w_id("headingTwo").size == 0:
        #     return True

    def test_02_check_open_with_open_energo(self):
        #разворачиваем тип процедуры
        self.el = self.wts.w_id("headingTwo")
        self.el.click()

        #выбираем тип процедуры "Відкриті торги"
        self.ch_op_el = self.wts.w_css("#tender > div > div > div:nth-child(1) > label")
        self.ch_op_el_text = self.ch_op_el.text
        self.ch_op_el.click()
        #выбираем тип процедуры "Відкриті торги для закупівлі енергосервісу"
        self.el_op_energo = self.wts.w_css("#tender > div > div > div:nth-child(2) > label")
        self.el_op_energo_text = self.el_op_energo.text
        self.el_op_energo.click()
        #кликаем на кнопку "Шукати"
        self.search_button = self.wts.w_css("#navPopover > div > button")
        sleep(3)
        self.search_button.click()

        #self.q = self.wts.execute_script("window.scrollTo(0, 1000)")
        sleep(3)
        #тип найденой процедуры
        self.viewer1 = self.wts.w_css("#purchase-page > div > div:nth-child(3) > div > div.panel-footer.text-muted > div > div.col-md-6 > span > span:nth-child(3)")
        self.viewer1_text = self.viewer1.text
        #отображение кнопки "Відкриті торги"
        self.but_op = self.wts.w_css("#wrapper > div > div > div > div.row > div > div > div > div:nth-child(4) > div > div:nth-child(1) > button")
        self.but_op_text = self.but_op.text
        #print(self.but_op_text)
        #отображение кнопки "Відкриті торги для закупівлі енергосервісу"
        self.but_op_energo = self.wts.w_css("#wrapper > div > div > div > div.row > div > div > div > div:nth-child(4) > div > div:nth-child(2) > button")
        self.but_op_energo_text = self.but_op_energo.text
        #print(self.but_op_energo_text)

        #проверяем, что тип найденой процедуры равен одному из типов выбранной
        self.assertTrue(
            (self.viewer1_text, self.ch_op_el_text) or (self.viewer1_text, self.el_op_energo_text)
        )
        #проверяем, что текст кнопок равен тексту заданных типов
        self.assertTrue(self.ch_op_el_text, self.but_op_text)
        self.assertTrue(self.el_op_energo_text, self.but_op_energo_text)

        sleep(3)
    def test_03_choose_all_procedures(self):
        #кликаем на кнопку "Очистити"
        self.clear_button = self.wts.w_css("#butClearFilterGeo")
        self.clear_button.click()
        #кликаем на кнопку "Вибрати все"
        self.choose_all_but = self.wts.w_css("#butSelectFilterGeo")
        self.choose_all_but.click()

        #br.execute_script("window.scrollTo(1000, 0)")
        #кликаем на кнопку "Шукати"
        self.search_button = self.wts.w_css("#butSimpleSearch")
        sleep(3)
        self.search_button.click()
        self.all_but = self.wts.w_css("#wrapper > div > div > div > div.row > div > div > div > div:nth-child(4) > div > div > button")
        self.all_but_text = self.all_but.text
        self.up = str(self.all_but_text).upper()
        #print(self.up)
        self.all_label = self.wts.w_css("#headingTwo > div > span.label.label-success-outline.pull-right.ng-scope")
        self.all_label_text = self.all_label.text
        #проверяем, что текст кнопки и лейбла совпадает
        self.assertEqual(self.all_label_text, self.up)

        #список типов процедур
        negatiation_short_text = self.wts.w_css("#tender > div > div > div:nth-child(12) > label").text
        negatiation_text = self.wts.w_css("#tender > div > div > div:nth-child(11) > label").text
        negatiation_oborona_text = self.wts.w_css("#tender > div > div > div:nth-child(10) > label").text
        competitive_dialogue_en_2_level_text = self.wts.w_css("#tender > div > div > div:nth-child(9) > label").text
        competitive_dialogue_en_text = self.wts.w_css("#tender > div > div > div:nth-child(8) > label").text
        competitive_dialogue_2_level_text = self.wts.w_css("#tender > div > div > div:nth-child(8) > label").text
        competitive_dialogue_text = self.wts.w_css("#tender > div > div > div:nth-child(6) > label").text
        zvit_text = self.wts.w_css("#tender > div > div > div:nth-child(5) > label").text
        doporog_text = self.wts.w_css("#tender > div > div > div:nth-child(4) > label").text
        open_en_text = self.wts.w_css("#tender > div > div > div:nth-child(3) > label").text
        open_energo_text = self.wts.w_css("#tender > div > div > div:nth-child(3) > label").text
        open_text = self.wts.w_css("#tender > div > div > div:nth-child(3) > label").text

        #найденые тендера
        tender_random_1_text = self.wts.w_css("#purchase-page > div > div:nth-child(3) > div > div.panel-footer.text-muted > div > div.col-md-6 > span > span:nth-child(3)").text

        tender_random_2_text = self.wts.w_css("#purchase-page > div > div:nth-child(4) > div > div.panel-footer.text-muted > div > div.col-md-6 > span > span:nth-child(3)").text
        #self.wts.execute_script("window.scrollTo(0, 1000)")
        #tender_random_3_text = self.wts.w_css("#purchase-page > div > div:nth-child(5) > div > div.panel-footer.text-muted > div > div.col-md-6 > span > span:nth-child(3)").text

        rand = [tender_random_1_text,
                tender_random_2_text]
                #tender_random_3_text]

        proced = [negatiation_short_text,
                  negatiation_text,
                  negatiation_oborona_text,
                  competitive_dialogue_en_2_level_text,
                  competitive_dialogue_en_text,
                  competitive_dialogue_2_level_text,
                  competitive_dialogue_text,
                  zvit_text,
                  doporog_text,
                  open_en_text,
                  open_energo_text,
                  open_text
                  ]

        if tender_random_1_text in proced and \
           tender_random_2_text in proced:
           #tender_random_3_text in proced:
            return True

        # res = list(set(proced) - set(rand))
        # print(res)

        #кликаем на кнокпу "Очистити"
        # self.clear_button = self.wts.w_css("#butClearFilterGeo")
        # sleep(10)
        # self.clear_button.click()


        self.but_for_clear = self.wts.w_id("butClearFilterGeo")
        sleep(10)
        self.but_for_clear.click()
        sleep(10)

        #проверка того, что кнопка не "Очистити" не отображается(под вопросом)
        #self.but_for_clear.is_disabled()

        #self.assertFalse(self.but_for_clear)
        self.but_for_clear.is_enabled()

        #сворачиваем тип процедуры

        self.el = self.wts.w_id("headingOne")
        self.el.click()

    #     # if self.el.click():
    #     #     return True
    #
    def test_04_viewer_stage(self):
        #разворачиваем этапы

        self.stage_down = self.wts.w_css("#filterblock > li:nth-child(2)")
        sleep(10)
        self.stage_down.click()

        #выбор этапа
        self.stage = self.wts.w_css("#tenderEtap > div > div:nth-child(3) > div > label")

        sleep(10)
        self.stage.click()
        sleep(10)
        self.stage_text = self.stage.text

        #кликаем на кнопку "Шукати"
        self.search_button = self.wts.w_css("#butSimpleSearch")
        sleep(3)
        self.search_button.click()

        # self.refinement_period = self.wts.w_css(".getpurchase-times.more-arr")
        # self.refinement_period_text = self.refinement_period.text
        # print(self.refinement_period_text)

        sleep(10)
        #Вытягиваем текст из кнопки
        self.but_refinement_period = self.wts.w_css(".btn.btn-default.btn-xs")
        self.but_refinement_period_text = self.but_refinement_period.text
        #print("текст кнопки: " + self.but_refinement_period_text)


        # try:
        #     self.but_refinement_period = self.wts.w_css(".btn.btn-default.btn-xs")
        #     self.but_refinement_period_text = self.but_refinement_period.text
        #     self.wts.w_xpath(".//*[@id='wrapper']/div/div/div/div[2]/div/div/div/div[5]/div/div[1]/button//*[contains(text{self.but_refinement_period_text},"")]")
        # except NoSuchElementException:
        #     return False
        # return True


        #Сравниваем текст кнопки и выбранного этапа
        #self.assertEqual(self.but_refinement_period_text, self.stage_text)


        #Сравниваем текст найденных тендеров и текст выбранного этапа
        self.randtender_1_text = self.wts.w_css(".getpurchase-times.more-arr").text
        self.randtender_2_text = self.wts.w_xpath(".//*[@id='purchase-page']/div/div[3]/div/div[2]/div/div[2]/div[1]/span[1]").text
        self.randtender_3_text = self.wts.w_xpath(".//*[@id='purchase-page']/div/div[4]/div/div[2]/div/div[2]/div[1]/span[1]").text

        self.assertTrue(
            (self.randtender_1_text,self.stage_text) and (self.randtender_2_text, self.stage_text) and (self.randtender_3_text, self.stage_text)
        )

        #Кликаем на кнокпу "Очистити"
        sleep(10)
        self.but_for_clear = self.wts.w_id("butClearFilterGeo").click()



        #сворачиваем этапы
        self.stage_down = self.wts.w_css("#filterblock > li:nth-child(2)")
        sleep(10)
        self.stage_down.click()


    def test_05(self):
        pass

    def test_06_check_refinement_period_with_finished(self):
        #разворачиваем этапы

        self.stage_down = self.wts.w_css("#filterblock > li:nth-child(2)")
        sleep(10)
        self.stage_down.click()

        #выбор этапа "Период уточнений"
        self.stage = self.wts.w_xpath(".//*[@id='tenderEtap']/div/div[3]/div/label")

        sleep(10)
        self.stage.click()
        sleep(10)
        self.stage_text = self.stage.text


        #выбор этапа "Завершено"
        self.finished_stage = self.wts.w_xpath(".//*[@id='tenderEtap']/div/div[9]/div")
        self.finished_stage.click()
        self.finished_stage_text = self.finished_stage.text


        #кликаем на кнопку "Шукати"
        self.search_button = self.wts.w_css("#butSimpleSearch")
        sleep(3)
        self.search_button.click()
        sleep(10)


        #Вытягиваем текст из кнопки
        self.refinement_but = self.wts.w_xpath(".//*[@id='wrapper']/div/div/div/div[2]/div/div/div/div[5]/div/div[1]/button")
        self.refinement_but_text = self.refinement_but.text

        self.finished_stage_but = self.wts.w_xpath(".//*[@id='wrapper']/div/div/div/div[2]/div/div/div/div[5]/div/div[2]/button")
        self.finished_stage_but_text = self.finished_stage_but.text


        #Сравниваем текст кнопок
        self.assertTrue(
            (self.refinement_but_text, self.stage_text) and (self.finished_stage_text, self.finished_stage_but_text)
        )

        #Сравниваем текст найденных тендеров с выбранными этапами
        self.randten_1_text = self.wts.w_xpath(".//*[@id='purchase-page']/div/div[2]/div/div[2]/div/div[2]/div[1]/span[1]").text
        self.randten_2_text = self.wts.w_xpath(".//*[@id='purchase-page']/div/div[3]/div/div[2]/div/div[2]/div[1]/span[1]").text
        self.randten_3_text = self.wts.w_xpath(".//*[@id='purchase-page']/div/div[4]/div/div[2]/div/div[2]/div[1]/span[1]").text

        self.assertTrue(
            (self.randten_1_text, self.stage_text) or (self.randten_1_text, self.finished_stage_text)
        )

        self.assertTrue(
            (self.randten_2_text, self.stage_text) or (self.randten_2_text, self.finished_stage_text)
        )

        self.assertTrue(
            (self.randten_3_text, self.stage_text) or (self.randten_3_text, self.finished_stage_text)
        )

        #Кликаем на кнокпу "Очистити"
        sleep(10)
        self.but_for_clear = self.wts.w_id("butClearFilterGeo").click()

        #сворачиваем этапы
        self.stage_down = self.wts.w_css("#filterblock > li:nth-child(2)")
        sleep(10)
        self.stage_down.click()


    def test_07_list_of_caterogia(self):
        #разворачиваем список номенклатур
        self.nomenclature = self.wts.w_id("dkHelpers")
        self.nomenclature.click()
        sleep(10)


        #выбираем ДК
        self.cpv = self.wts.w_xpath(".//*[@id='dkHelpersList']/div/ul/li[1]/a/span").click()
        sleep(10)

        #self.cpv_text = self.wts.w_xpath(".//*[@id='31850_anchor'][contains(text(),\"03000000-1\")]")

        #вводим код категории и кликаем на кнопку "Закрити"
        self.input_code_cpv = '03000000-1'
        self.wts.w_id("search-classifier-text").send_keys(self.input_code_cpv)


        self.search_cpv =self.wts.w_id("31850_anchor")
        #self.search_cpv_text = self.search_cpv.text
        self.but_close = self.wts.w_css(".btn.btn-sm.btn-white").click()


        #вытягиваем и сверяем текст из кнопки
        self.but_cpv_text = self.wts.w_css(".btn.btn-default.btn-xs").text
        #self.assertEqual(self.search_cpv_text, self.but_cpv_text)
        #print(self.search_cpv_text)
        print(self.but_cpv_text)


        #кликаем на кнопку "Шукати"
        self.search_button = self.wts.w_css("#butSimpleSearch")
        sleep(3)
        self.search_button.click()
        sleep(10)


        #переходим по первой ссылке
        self.first_link = self.wts.w_xpath(".//*[contains(@id,'href-purchase-')]").click()

        # self.lots = self.wts.w_id("view-lots-tab")
        # self.content_info = self.wts.w_xpath(".//*[@id='info-purchase']/div/div/md-content")
        self.item_tad = self.wts.w_id("procurement-subject-tab")
        self.item_tad.click()
        self.cpv_code_in_item_text = self.wts.w_xpath(".//*[contains(@id,'procurementSubjectCpvCode')]").text


        # if self.lots in self.content_info:
        #     self.item_tad.click()

        #проверяем, что позиция выбранного тендера содержит тот же cpv, который был выбран изначально
        self.assertEqual(self.cpv_code_in_item_text, "03000000-1")


        #возвращаемся на главную страницу
        self.wts.w_xpath(".//*[@id='logo']/a/span/img").click()


        #удаляем все категории
        self.wts.w_id("clear_all").click()



    def test_08_check_few_caterogias(self):
        #разворачиваем список номенклатур
        sleep(30)
        self.nomenclature = self.wts.w_xpath(".//*[@id='dkHelpers']/div")
        self.nomenclature.click()
        sleep(10)


        #выбираем ДК
        self.cpv = self.wts.w_xpath(".//*[@id='dkHelpersList']/div/ul/li[1]/a/span").click()
        sleep(10)


        #вводим код категории и кликаем на кнопку "Закрити"
        self.input_code_cpv_1 = '03000000-1'
        self.wts.w_id("search-classifier-text").send_keys(self.input_code_cpv_1)
        self.full_text_cpv_1 = self.wts.w_xpath(".//*[@id='31850_anchor']").text


        sleep(3)
        self.but_close = self.wts.w_css(".btn.btn-sm.btn-white").click()
        sleep(3)
        self.cpv9 = self.wts.w_xpath(".//*[@id='dkHelpersList']/div/ul/li[1]/a/span").click()
        sleep(3)
        self.input_code_cpv_2 = '09000000-3'
        self.wts.w_id("search-classifier-text").send_keys(self.input_code_cpv_2)
        self.full_text_cpv_2 = self.wts.w_xpath('.//*[@id=\'32080_anchor\']').text
        sleep(3)
        self.but_close = self.wts.w_css(".btn.btn-sm.btn-white").click()


        #кликаем на кнопку "Шукати"
        self.search_button = self.wts.w_css("#butSimpleSearch")
        sleep(3)
        self.search_button.click()
        sleep(10)

        #сверяем текст кнопок с введенным
        self.cpv_but_text_1 = self.wts.w_xpath('.//*[@id=\'wrapper\']/div/div/div/div[2]/div/div/div/div[3]/div/div[1]/button').text
        self.cpv_but_text_2 = self.wts.w_xpath('.//*[@id=\'wrapper\']/div/div/div/div[2]/div/div/div/div[3]/div/div[2]/button').text
        self.assertEqual(self.full_text_cpv_1, self.cpv_but_text_1)
        self.assertEqual(self.cpv_but_text_2, self.full_text_cpv_2)



