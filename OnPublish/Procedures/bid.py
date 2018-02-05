from datetime import datetime
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from Prozorro.Pages.LoginPage import LoginPage
from Prozorro.Pages.TenderView import TenderView
from Prozorro.Utils import waitFadeIn


class Below_Bid(ParamsTestCase):

    def login_provider(self):
        url = self.parent_suite.suite_params["start_url"]
        self.wts.drv.get(url)

        with self.subTest("авторизация"):
            LoginPage(self.wts.drv).login(
                self.parent_suite.suite_params["tender_json"]["authorization"]["provider_login"],
                self.parent_suite.suite_params["tender_json"]["authorization"]["provider_password"]
            )

        myTendersList = WebDriverWait(self.wts.drv, 10).until(
            expected_conditions.visibility_of_element_located((By.ID,"myTendersList")))
        myTenders = WebDriverWait(self.wts.drv, 10).until(
            expected_conditions.visibility_of_element_located((By.ID, "myTenders")))

        if(    myTendersList.get_attribute("aria-expanded")=="true"
            or self.wts.drv.find_element_by_xpath("//div[@id='myTenders']/div").\
                get_attribute("class") =="filter-title"
            ):
            myTenders.click()

    def select_below_type(self):
        xpath_tender_type = "//ul[@id='filterblock']/li/div[@id='headingTwo']"

        tender_type = WebDriverWait(self.wts.drv, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath_tender_type)))
        self.assertIsNotNone(tender_type, "Элемент tenderType filter не найден  " + xpath_tender_type)
        waitFadeIn(self.wts.drv)
        tender_type.click()

        xpath_tender_type = "//input[@id='purchaseType1']/.."
        tender_period = WebDriverWait(self.wts.drv, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath_tender_type)))
        self.assertIsNotNone(tender_period, "Элемент tender_type filter не найден  " + xpath_tender_type)
        tender_period.click()

        sleep(1)
        waitFadeIn(self.wts.drv)
        tender_type.click()

        sleep(1)

    def select_tender_period(self):
        xpath_tender_etap = "//ul[@id='filterblock']/li/div[@id='headingOne']"

        tender_etap = WebDriverWait(self.wts.drv, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath_tender_etap)))
        self.assertIsNotNone(tender_etap, "Элемент tenderEtap filter не найден  " + xpath_tender_etap)
        waitFadeIn(self.wts.drv)
        tender_etap.click()

        xpath_below = "//input[@id='status3']/.."
        below = WebDriverWait(self.wts.drv, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath_below)))
        self.assertIsNotNone(below, "Элемент tender_period filter не найден  " + xpath_below)
        below.click()
        tender_etap.click()

    def find_tender_for_bid(self):
        id_searchType='searchType'
        id_findbykeywords='findbykeywords'
        id_butSimpleSearch='butSimpleSearch'

        ProzorroId = self.parent_suite.suite_params["ProzorroId"]

        select_searchType = WebDriverWait(self.wts.drv, 5).until(
            expected_conditions.visibility_of_element_located((By.ID, id_searchType)))
        Select(select_searchType).select_by_visible_text("Системному номеру (у форматі UA-....)")
        butSimpleSearch = WebDriverWait(self.wts.drv, 5).until(
            expected_conditions.visibility_of_element_located((By.ID, id_butSimpleSearch)))
        findbykeywords = WebDriverWait(self.wts.drv, 5).until(
            expected_conditions.visibility_of_element_located((By.ID, id_findbykeywords)))
        findbykeywords.clear()

        findbykeywords.send_keys(ProzorroId)
        butSimpleSearch.click()

        self.wts.drv.execute_script("window.scroll(0,1000)")

        sleep(5)

        tender_link = WebDriverWait(self.wts.drv, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH,
        "//div[@id='purchase-page']//a[contains(@id,'href-purchase')]/../span[text()='"+ProzorroId+"']/../a")))

        tender_link.click()

    def wait_for_tender_period(self):

        with self.subTest("дата начала периода подачи предложений"):
            str_date_start = WebDriverWait(self.wts.drv, 5).until(
                expected_conditions.visibility_of_element_located(
                    (By.ID, "purchasePeriodTenderStart"))).text
            date_start = datetime.strptime(str_date_start,"%d-%m-%Y %H:%M:%S")
            secondsDiff = (date_start-datetime.now()).seconds
            minutesDiff = secondsDiff // 60

        url = self.wts.drv.current_url
        for m in range(1, minutesDiff*2+16):
            status =self.wts.drv.execute_script("return $('#purchaseStatus').text()")
            if status !="3" :
                sleep(30)
                self.wts.drv.get(url)
            else:
                break

        self.assertEquals(status,"3")

    def add_bid(self):
        TenderView(self.wts.drv).\
            open_bids().\
            new(prepare=0)


