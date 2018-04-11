import unittest
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException

from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase


class ViewerFilters(ParamsTestCase):

    def test_01_check_open(self):
        #кликаем на тип процедуры
        self.el = self.wts.w_css("#headingTwo > div")
        self.el.click()
        #выбираем тип процедуры "Відкриті торги"
        self.ch_op_el = self.wts.w_css("#tender > div > div > div:nth-child(1) > label")
        ch_op_el_text = self.ch_op_el.text
        self.ch_op_el.click()

        #кликаем на кнопку "Шукати"
        self.search_button = self.wts.w_css("#navPopover > div > button")
        sleep(5)
        self.search_button.click()

        self.q = self.wts.execute_script("window.scrollTo(0, 1000)")
        sleep(5)
        #выбираем найденый тендер
        self.el = self.wts.w_css(
            "#purchase-page > div > div:nth-child(3) > div > div.panel-footer.text-muted > div > div.col-md-6 > span > span:nth-child(3)")
        el_text = self.el.text
        #проверяем, что название выбранной процедуры совпадает с названием найденой процедуры
        self.assertEqual(ch_op_el_text, el_text)
        #кликаем на кнокпу "Очистити"
        self.clear_button = self.wts.w_css("#butClearFilterGeo > span")
        self.clear_button.click()


        # try:
        #     el = br.find_element_by_css_selector("#purchase-page > div > div:nth-child(3) > div > div.panel-footer.text-muted > div > div.col-md-6 > span > span:nth-child(3)")
        #     el_text = el.text
        #     print(el_text)
        #     self.e = br.find_element_by_css_selector(
        #         "#purchase-page > div > div:nth-child(5) > div > div.panel-footer.text-muted > div > div.col-md-6 > span > span:nth-child(3)")
        # except NoSuchElementException:
        #     return False
        # return True


    def test_02_check_open_with_open_energo(self):
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

        self.q = self.wts.execute_script("window.scrollTo(0, 1000)")
        sleep(3)
        #тип найденой процедуры
        self.viewer1 = self.wts.w_css("#purchase-page > div > div:nth-child(3) > div > div.panel-footer.text-muted > div > div.col-md-6 > span > span:nth-child(3)")
        self.viewer1_text = self.viewer1.text
        #отображение кнопки "Відкриті торги"
        self.but_op = self.wts.w_css("#wrapper > div > div > div > div.row > div > div > div > div:nth-child(4) > div > div:nth-child(1) > button")
        self.but_op_text = self.but_op.text
        print(self.but_op_text)
        #отображение кнопки "Відкриті торги для закупівлі енергосервісу"
        self.but_op_energo = self.wts.w_css("#wrapper > div > div > div > div.row > div > div > div > div:nth-child(4) > div > div:nth-child(2) > button")
        self.but_op_energo_text = self.but_op_energo.text
        print(self.but_op_energo_text)

        #проверяем, что тип найденой процедуры равен одному из типов выбранной
        self.assertTrue(
            (self.viewer1_text, self.ch_op_el_text) or (self.viewer1_text, self.el_op_energo_text)
        )
        #проверяем, что текст кнопок равен тексту заданных типов
        self.assertTrue(self.ch_op_el_text, self.but_op_text)
        self.assertTrue(self.el_op_energo_text, self.but_op_energo_text)

        sleep(3)
    def test_03_choose_all(self):
        #кликаем на кнопку "Очистити"
        self.clear_button = self.wts.w_css("#butClearFilterGeo")
        self.clear_button.click()
        #кликаем на кнопку "Вибрати все"
        self.choose_all_but = self.wts.w_css("#butSelectFilterGeo")
        self.choose_all_but.click()

        br.execute_script("window.scrollTo(1000, 0)")
        #кликаем на кнопку "Шукати"
        self.search_button = self.wts.w_css("#butSimpleSearch")
        sleep(3)
        self.search_button.click()
        self.all_but = self.wts.w_css("#wrapper > div > div > div > div.row > div > div > div > div:nth-child(4) > div > div > button")
        self.all_but_text = self.all_but.text
        self.up = str(self.all_but_text).upper()
        print(self.up)
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

        #найденый тендер
        tender_random_1_text = self.wts.w_css("#purchase-page > div > div:nth-child(3) > div > div.panel-footer.text-muted > div > div.col-md-6 > span > span:nth-child(3)").text
        tender_random_2_text = self.wts.w_css("#purchase-page > div > div:nth-child(4) > div > div.panel-footer.text-muted > div > div.col-md-6 > span > span:nth-child(3)").text
        br.execute_script("window.scrollTo(0, 1000)")
        tender_random_3_text = self.wts.w_css("#purchase-page > div > div:nth-child(5) > div > div.panel-footer.text-muted > div > div.col-md-6 > span > span:nth-child(3)").text

        rand = [tender_random_1_text,
                tender_random_2_text,
                tender_random_3_text]

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
           tender_random_2_text in proced and  \
           tender_random_3_text in proced :
            return True

        res = list(set(proced) - set(rand))
        print(res)

    def test_04_viewer_region(self):
        pass

    def test_05_viewer_list_CPV(self):
        pass

    def test_06_viewer_currency_budget(self):
        pass

    def test_07_viewer_filter_of_date(self):
        pass

    def test_08_viewer_edrpou_owner(self):
        pass


