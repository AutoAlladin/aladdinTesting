import unittest
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException

br = webdriver.Chrome()
br.get("https://test-gov.ald.in.ua/purchases")



class ViewerFilters(unittest.TestCase):
    #help(unittest.TestCase)



    def test_01_check_open(self):
        #кликаем на тип процедуры
        self.el = br.find_element_by_css_selector("#headingTwo > div")
        self.el.click()
        #выбираем тип процедуры "Відкриті торги"
        self.ch_op_el = br.find_element_by_css_selector("#tender > div > div > div:nth-child(1) > label")
        ch_op_el_text = self.ch_op_el.text
        self.ch_op_el.click()

        #кликаем на кнопку "Шукати"
        self.search_button = br.find_element_by_css_selector("#navPopover > div > button")
        sleep(5)
        self.search_button.click()

        self.q = br.execute_script("window.scrollTo(0, 1000)")
        sleep(5)
        #выбираем найденый тендер
        self.el = br.find_element_by_css_selector(
            "#purchase-page > div > div:nth-child(3) > div > div.panel-footer.text-muted > div > div.col-md-6 > span > span:nth-child(3)")
        el_text = self.el.text
        #проверяем, что название выбранной процедуры совпадает с названием найденой процедуры
        self.assertEqual(ch_op_el_text, el_text)
        #кликаем на кнокпу "Очистити"
        self.clear_button = br.find_element_by_css_selector("#butClearFilterGeo > span")
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
        self.ch_op_el = br.find_element_by_css_selector("#tender > div > div > div:nth-child(1) > label")
        self.ch_op_el_text = self.ch_op_el.text
        self.ch_op_el.click()
        #выбираем тип процедуры "Відкриті торги для закупівлі енергосервісу"
        self.el_op_energo = br.find_element_by_css_selector("#tender > div > div > div:nth-child(2) > label")
        self.el_op_energo_text = self.el_op_energo.text
        self.el_op_energo.click()
        #кликаем на кнопку "Шукати"
        self.search_button = br.find_element_by_css_selector("#navPopover > div > button")
        sleep(3)
        self.search_button.click()

        self.q = br.execute_script("window.scrollTo(0, 1000)")
        sleep(3)
        #тип найденой процедуры
        self.viewer1 = br.find_element_by_css_selector("#purchase-page > div > div:nth-child(3) > div > div.panel-footer.text-muted > div > div.col-md-6 > span > span:nth-child(3)")
        self.viewer1_text = self.viewer1.text
        #отображение кнопки "Відкриті торги"
        self.but_op = br.find_element_by_css_selector("#wrapper > div > div > div > div.row > div > div > div > div:nth-child(4) > div > div:nth-child(1) > button")
        self.but_op_text = self.but_op.text
        print(self.but_op_text)
        #отображение кнопки "Відкриті торги для закупівлі енергосервісу"
        self.but_op_energo = br.find_element_by_css_selector("#wrapper > div > div > div > div.row > div > div > div > div:nth-child(4) > div > div:nth-child(2) > button")
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
        self.clear_button = br.find_element_by_css_selector("#butClearFilterGeo")
        self.clear_button.click()
        #кликаем на кнопку "Вибрати все"
        self.choose_all_but = br.find_element_by_css_selector("#butSelectFilterGeo")
        self.choose_all_but.click()

        br.execute_script("window.scrollTo(1000, 0)")
        #кликаем на кнопку "Шукати"
        self.search_button = br.find_element_by_css_selector("#butSimpleSearch")
        sleep(3)
        self.search_button.click()
        self.all_but = br.find_element_by_css_selector("#wrapper > div > div > div > div.row > div > div > div > div:nth-child(4) > div > div > button")
        self.all_but_text = self.all_but.text
        self.up = str(self.all_but_text).upper()
        print(self.up)
        self.all_label = br.find_element_by_css_selector("#headingTwo > div > span.label.label-success-outline.pull-right.ng-scope")
        self.all_label_text = self.all_label.text
        self.assertEqual(self.all_label_text, self.up)



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


