from selenium.webdriver.support.select import Select
from selenium import webdriver
from Prozorro.Pages.LoginPage import LoginPage
from Prozorro.Pages.TenderNew import *
from Prozorro.Pages.TenderView import TenderView
from Prozorro.Utils import *
import time





class MainPage:

    def __init__(self, _drv):
        self.drv =_drv
        #self.drv = webdriver.Chrome(_drv)
        self.liLoginNoAuthenticated = self.drv.find_element_by_id("liLoginNoAuthenticated")
        self.butLoginPartial = self.drv.find_element_by_id("butLoginPartial")

    def open_login_form(self):
        self.liLoginNoAuthenticated.click()
        self.butLoginPartial.click()
        return LoginPage(self.drv)

    def open_tender(self, uaid, waitstatus=None ):

        if self.drv.current_url!="https://test-gov.ald.in.ua/purchases":
            self.drv.get("https://test-gov.ald.in.ua")

        waitNotifyToast(self.drv)

        Select(self.drv.find_element_by_id("searchType")).select_by_value("1")

        self.searchInput = self.drv.find_element_by_id("findbykeywords")
        self.searchInput.clear()
        self.searchInput.send_keys(uaid)

        self.butSimpleSearch = self.drv.find_element_by_id("butSimpleSearch")
        self.butSimpleSearch.click()

        waitFadeIn(self.drv)

        tenderLink =WebDriverWait(self.drv, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='"+uaid+"']/../a")))
        tenderLink.click()

        WebDriverWait(self.drv, 20).until(
            EC.visibility_of_element_located((By.ID, "goToListPurchase")))

        return TenderView(self.drv)


    def create_tender(self, procurementMethodType, lots=0, items=1, docs=0, features=0, dic=None):
        self.btn_create_purchase=self.drv.find_element_by_id("btn_create_purchase")
        self.btn_create_purchase.click()

        if(procurementMethodType=="belowThreshold"):
            self.drv.find_element_by_xpath("//a[@href='/Purchase/Create/BelowThreshold']").click()
        is_multilot = "true"
        if lots == 0:
            is_multilot="false"

        return TenderNew(self.drv).\
            set_description(dic).\
            set_curr().\
            set_multilot(dic, is_multilot).\
            set_dates().\
            click_next_button().\
            add_lot(lots, dic).\
            add_item(dic).\
            click_finish_edit_button().\
            click_publish_button()

    def create_bid(self, uaid):
        return self.open_tender(uaid).\
                open_bids().\
                new();




