from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions

from Prozorro.Pages.LoginPage import LoginPage
from Prozorro.Pages.TenderNew import *
from Prozorro.Pages.TenderView import TenderView
from Prozorro.Pages.UserRegForm import UserRegForm
from Prozorro.Utils import *
import time





class MainPage:

    def __init__(self, _drv):
        self.drv =_drv
        #self.drv = webdriver.Chrome(_drv)
        self.liLoginNoAuthenticated = self.drv.find_element_by_id("liLoginNoAuthenticated")
        self.butLoginPartial = self.drv.find_element_by_id("butLoginPartial")
        self.butRegPartial = self.drv.find_element_by_id("butRegisterPartial")
        self.liCultureSelector =self.drv.find_element_by_id("liCultureSelector")
        self.liCultureSelector.click()
        self.drv.find_element_by_id("select_lang_uk-ua").click()
        time.sleep(3)


    def open_reg_form(self):
        self.liLoginNoAuthenticated.click()
        self.butRegPartial.click()
        WebDriverWait(self.drv, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.CLASS_NAME, "btn-success")))

        return UserRegForm(self.drv)

    def open_login_form(self):
        self.liLoginNoAuthenticated = self.drv.find_element_by_id("liLoginNoAuthenticated")
        self.butLoginPartial = self.drv.find_element_by_id("butLoginPartial")
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
            EC.visibility_of_element_located((By.XPATH,"//span[text()='"+uaid+"']/../a")))
        tenderLink.click()

        WebDriverWait(self.drv, 20).until(
            EC.visibility_of_element_located((By.ID,"goToListPurchase")))

        return TenderView(self.drv)

    def open_tender_url(self,url):
        self.drv.execute_script('''window.open("{0}", "_blank");'''.format(url))
        self.drv.switch_to.window(self.drv.window_handles[-1])
        WebDriverWait(self.drv, 2).until(
            EC.visibility_of_element_located((By.ID, "goToListPurchase")))
        return TenderView(self.drv)



    def create_tender(self, procurementMethodType, lots=0, items=1, docs=0, features=0, dic=None, nom=""):
        self.btn_create_purchase=self.drv.find_element_by_id("btn_create_purchase")
        waitFadeIn(self.drv)
        WebDriverWait(self.drv, 3).until(
            EC.element_to_be_clickable((By.ID,"btn_create_purchase" )) )
        try:
            self.btn_create_purchase.click()
        except  StaleElementReferenceException as se:
            time.sleep(5)
            self.btn_create_purchase = self.drv.find_element_by_id("btn_create_purchase")
            waitFadeIn(self.drv)
            self.btn_create_purchase.click()

        is_multilot = "true"
        if lots == 0:
            is_multilot = "false"

        if(procurementMethodType=="belowThreshold"):
            self.drv.find_element_by_xpath("//a[@href='/Purchase/Create/BelowThreshold']").click()
            return TenderNew(self.drv).\
                set_description(dic, nom).\
                set_curr().\
                set_multilot(dic, is_multilot).\
                set_dates(dic).\
                click_next_button().\
                add_lot(lots, dic).\
                add_item(dic, lots, items). \
                click_next_button(). \
                add_features(dic,lots,items,features).\
                add_doc(docs).\
                click_finish_edit_button().\
                click_publish_button()

        elif procurementMethodType=="aboveThresholdUA":
            self.drv.find_element_by_xpath("//a[@href='/Purchase/Create/AboveThresholdUA']").click()
            return TenderNew(self.drv). \
                set_description(dic, nom). \
                set_curr(). \
                set_multilot(dic, is_multilot). \
                set_open_tender_dates(dic) . \
                click_next_button(). \
                add_lot(lots, dic). \
                add_item(dic, lots, items). \
                click_next_button(). \
                add_features(dic, lots, items, features). \
                click_next_button().\
                add_doc(docs). \
                click_finish_edit_button().\
                click_publish_button()

        elif procurementMethodType=="concurentUA":
            self.drv.find_element_by_xpath("//a[@href='/Purchase/Create/CompetitiveDialogueUA']").click()
            return TenderNew(self.drv). \
                set_description(dic). \
                set_curr(). \
                set_multilot("false"). \
                set_open_tender_dates(dic). \
                click_next_button(). \
                add_item(). \
                click_finish_edit_button(). \
                click_publish_button()
        return None


    def create_bid(self, uaid, prepare):
        if prepare==0:
            return self.open_tender(uaid).\
                open_bids().\
                new(uaid);
        elif prepare==2:
            return self.open_tender_url(uaid).\
                open_bids().\
                new(1,uaid);
        else:
            return self.open_tender_url(uaid). \
                open_bids(). \
                new(prepare,uaid)




