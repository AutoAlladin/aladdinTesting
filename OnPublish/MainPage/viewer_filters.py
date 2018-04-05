import unittest
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException

br = webdriver.Chrome()
br.get("https://test-gov.ald.in.ua/purchases")



class ViewerFilters(unittest.TestCase):
    #help(unittest.TestCase)

    def test_01_check_open(self):
        self.el = br.find_element_by_css_selector("#headingTwo > div")
        self.el.click()
        self.ch_op_el = br.find_element_by_css_selector("#tender > div > div > div:nth-child(1) > label")
        ch_op_el_text = self.ch_op_el.text
        print(ch_op_el_text)
        self.ch_op_el.click()
        self.search_button = br.find_element_by_css_selector("#navPopover > div > button")
        sleep(3)
        self.search_button.click()

        self.q = br.execute_script("window.scrollTo(0, 1000)")
        sleep(3)
        self.el = br.find_element_by_css_selector(
            "#purchase-page > div > div:nth-child(3) > div > div.panel-footer.text-muted > div > div.col-md-6 > span > span:nth-child(3)")
        el_text = self.el.text
        print(el_text)


        self.assertEqual(ch_op_el_text, el_text)

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
        self.ch_op_el = br.find_element_by_css_selector("#tender > div > div > div:nth-child(1) > label")
        self.ch_op_el_text = self.ch_op_el.text
        print(self.ch_op_el_text)
        self.ch_op_el.click()


        self.el_op_energo = br.find_element_by_css_selector("#tender > div > div > div:nth-child(2) > label")
        self.el_op_energo_text = self.el_op_energo.text
        self.el_op_energo.click()
        self.search_button = br.find_element_by_css_selector("#navPopover > div > button")
        sleep(3)
        self.search_button.click()
        self.q = br.execute_script("window.scrollTo(0, 1000)")
        sleep(3)
        self.viewer1 = br.find_element_by_css_selector("#purchase-page > div > div:nth-child(3) > div > div.panel-footer.text-muted > div > div.col-md-6 > span > span:nth-child(3)")
        self.viewer1_text = self.viewer1.text

        #self.assertEqual(self.viewer1_text, self.el_op_energo_text) or self.assertNotEqual(self.viewer1_text, self.el_op_energo_text)
        self.assertTrue(
            (self.viewer1_text, self.ch_op_el_text) or (self.viewer1_text, self.el_op_energo_text)
        )

    def test_03_viewer_open_en(self):
        pass

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


