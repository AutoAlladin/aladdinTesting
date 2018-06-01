from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions

from Prozorro.Pages.LoginPage import LoginPage
from Prozorro.Pages.TenderNew import *
from Prozorro.Pages.TenderView import TenderView
from Prozorro.Pages.UserRegForm import UserRegForm
from Prozorro.Utils import *
import time
from datetime import datetime, timedelta, time




class MainPage:

    def __init__(self, _drv):
        self.drv =_drv
        #self.drv = webdriver.Chrome(_drv)
        waitFadeIn(self.drv)
        #self.liLoginNoAuthenticated = self.drv.find_element_by_id("liLoginNoAuthenticated")
        self.butLoginPartial = self.drv.find_element_by_id("butLoginPartial")
        self.butRegPartial = self.drv.find_element_by_id("butRegisterPartial")

        self.liCultureSelector =self.drv.find_element_by_id("liCultureSelector")

        waitFadeIn(self.drv)
        self.liCultureSelector.click()
        select_lang = WebDriverWait(self.drv, 20).until(
            expected_conditions.visibility_of_element_located(
                (By.ID, "select_lang_uk-ua")))
        select_lang.click()

        WebDriverWait(self.drv, 10).until(
            expected_conditions.text_to_be_present_in_element(
                (By.CLASS_NAME, "content"), "Aladdin Government закупівлі"))
        waitFadeIn(self.drv)

    def open_reg_form(self):
        waitFadeIn(self.drv)
        #self.liLoginNoAuthenticated.click()
        self.butRegPartial.click()
        WebDriverWait(self.drv, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.CLASS_NAME, "btn-success")))

        return UserRegForm(self.drv)

    def open_login_form(self):
        waitFadeIn(self.drv)
        #self.liLoginNoAuthenticated = self.drv.find_element_by_id("liLoginNoAuthenticated")

        try:
            self.drv.find_element_by_id("butLogoutPartial").click()
        except:
            pass

        self.butLoginPartial = self.drv.find_element_by_id("butLoginPartial")

        waitFadeIn(self.drv)
        #self.liLoginNoAuthenticated.click()
        self.butLoginPartial.click()
        return LoginPage(self.drv)

    def open_tender(self, uaid, waitstatus=None ):

        waitNotifyToast(self.drv)

        #Select(self.drv.find_element_by_id("searchType")).select_by_value("1")

        self.searchInput = self.drv.find_element_by_id("findbykeywords")
        self.searchInput.clear()
        self.searchInput.send_keys(uaid)

        self.butSimpleSearch = self.drv.find_element_by_id("butSimpleSearch")
        waitFadeIn(self.drv)
        self.butSimpleSearch.click()

        waitFadeIn(self.drv)
        #print((By.XPATH,"//span[text()='"+uaid+"']/../a"))
        tenderLink =WebDriverWait(self.drv, 20).until(
            EC.visibility_of_element_located((By.XPATH,"//span[text()='"+uaid+"']/../a")))

        scroll_to_element(self.drv, tenderLink)
        waitFadeIn(self.drv)
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

    def create_tender(self, procurementMethodType, lots=0, items=1, docs=0, features=0,
                      dic=None, nom="", log=None):
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
                set_description(dic["below"], nom).\
                set_curr().\
                set_multilot(dic["below"], is_multilot).\
                set_dates(dic["below"]).\
                click_next_button().\
                add_lot(lots, dic["below"]).\
                add_item(dic["below"], lots, items). \
                click_next_button(). \
                add_features(dic["features"],lots,items,features).\
                add_doc(docs, dic["docs"]).\
                click_finish_edit_button().\
                click_publish_button()

        elif procurementMethodType=="aboveThresholdUA":
            self.drv.find_element_by_xpath("//a[@href='/Purchase/Create/AboveThresholdUA']").click()
            return TenderNew(self.drv). \
                set_description(dic["openUA"], nom). \
                set_curr(). \
                set_multilot(dic["openUA"], is_multilot). \
                set_open_tender_dates(dic) . \
                click_next_button(). \
                add_lot(lots, dic["openUA"]). \
                add_item(dic["openUA"], lots, items). \
                click_next_button(). \
                add_features(dic["features"], lots, items, features). \
                click_next_button().\
                add_doc(docs,dic["docs"]). \
                click_finish_edit_button().\
                click_publish_button()


        elif procurementMethodType=="aboveThresholdEU":
            self.drv.find_element_by_xpath("//a[@href='/Purchase/Create/AboveThresholdEU']").click()
            return TenderNew(self.drv). \
                set_description(dic["openEU"], nom, en=True). \
                set_curr(). \
                set_multilot(dic["openEU"], is_multilot). \
                set_open_tender_dates(dic["openEU"]) . \
                click_next_button(). \
                add_lot_en(lots, dic["openEU"]). \
                add_item(dic, lots, items, en=True). \
                click_next_button(). \
                add_features(dic["openEU"], lots, items, features, enf=True). \
                click_next_button().\
                add_doc(docs). \
                click_finish_edit_button().\
                click_publish_button()

        elif procurementMethodType=="concurentUA":
            self.drv.find_element_by_xpath("//a[@href='/Purchase/Create/CompetitiveDialogueUA']").click()
            return TenderNew(self.drv). \
                set_description(dic["concurentUA"],  nom, en=True). \
                set_curr(). \
                set_multilot(dic["concurentUA"],is_multilot). \
                set_open_tender_dates(dic["concurentUA"]). \
                click_next_button(). \
                add_lot(lots, dic["concurentUA"]). \
                add_item(dic["concurentUA"],lots,items). \
                click_next_button(). \
                add_features(dic["features"], lots, items, features). \
                click_next_button(). \
                add_doc(docs,dic["docs"]). \
                click_finish_edit_button(). \
                click_publish_button()

        return None


    def create_bid(self, proc, uaid, dic):
        if proc == "below":
            return self.open_tender(uaid).\
                   open_bids().\
                   new(uaid,dic)
        elif proc == "concurentUA":
            return self.open_tender(uaid).\
                   open_bids().\
                   new_concurent(uaid,dic)




