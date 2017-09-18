from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.select import Select
from Prozorro.Utils import set_datepicker,waitFadeIn


class TenderNew:
    def __init__(self, _drv):
        self.drv = _drv
        #self.drv = webdriver.Chrome(_drv)

    def click_finish_edit_button(self):
        try:
            movePurchaseView = self.drv.find_element_by_id("movePurchaseView")
            self.drv.execute_script("window.scroll(0, " + str(movePurchaseView.location["y"]) + "-"+str(self.drv.find_element_by_id("header").size["height"])+")")
            movePurchaseView.click()
        except WebDriverException as w:
            raise Exception("Не нажимается кнопка movePurchaseView  - \n" + w.msg)
        return self

    def click_publish_button(self):
        try:
            waitFadeIn(self.drv)
            publishPurchase = self.drv.find_element_by_id("publishPurchase")
            publishPurchase.click()

            waitFadeIn(self.drv)
            WebDriverWait(self.drv, 120).until(EC.visibility_of_element_located((By.ID, "purchaseGuid")))
            purchaseGuid =self.drv.find_element_by_id("purchaseGuid")

            return purchaseGuid.text
        except WebDriverException as w:
            raise Exception("Не нажимается кнопка publishPurchase  - \n" + w.msg)
        return None


    def click_next_button(self):
        try:
            next_step = self.drv.find_element_by_id("next_step")
            self.drv.execute_script("window.scroll(0, "+str(next_step.location["y"])+")")
            next_step.click()
        except WebDriverException as w:
            raise Exception("Не нажимается кнопка next_step  - \n" + w.msg)
        return self


    def set_dates(self):
        try:
            dt = datetime.now()
            set_datepicker(self.drv, "period_enquiry_start", (dt + timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S"))
            set_datepicker(self.drv, "period_enquiry_end", (dt + timedelta(minutes=10)).strftime("%Y-%m-%d %H:%M:%S"))
            set_datepicker(self.drv, "period_tender_start", (dt + timedelta(minutes=10)).strftime("%Y-%m-%d %H:%M:%S"))
            set_datepicker(self.drv, "period_tender_end", (dt + timedelta(minutes=100)).strftime("%Y-%m-%d %H:%M:%S"))
        except Exception as e:
            raise Exception("Чтото не так с датами шапки тендера - \n" + e)
        return self

    def set_curr(self):
        select_currencies = self.drv.find_element_by_id("select_currencies")
        Select(select_currencies).select_by_value("string:UAH")
        is_vat = self.drv.find_element_by_xpath("//*[@id='is_vat']/div[1]/div[2]/div")
        is_vat.click()
        return self

    def set_multilot(self, is_multi):
        is_multilot = self.drv.find_element_by_xpath("//*[ @id='is_multilot']/div[1]/div[2]")
        if (is_multi == "true"):
            is_multilot.click()
        else:
            budget = self.drv.find_element_by_id("budget")
            budget.send_keys("10000.15")
            min_step = self.drv.find_element_by_id("min_step")
            min_step.send_keys("150")
            min_step_percentage = self.drv.find_element_by_id("min_step_percentage")
            min_step_percentage.send_keys("1.54")
        return self

    def set_description(self):
        title = self.drv.find_element_by_id("titleOfTenderForEdit")
        title.send_keys("below tebder")
        description = self.drv.find_element_by_id("description")
        description.send_keys("tender description")
        return self

    def add_item(self, lot="0", item="0"):
        add_procurement_subject=self.drv.find_element_by_id("add_procurement_subject"+lot)
        add_procurement_subject.click()

        add_item_button = WebDriverWait(self.drv, 20).until(EC.visibility_of_element_located((By.ID, "update_"+lot+item)))
        print(self.drv.current_url)

        procurementSubject_description = self.drv.find_element_by_id("procurementSubject_description"+lot+item)
        procurementSubject_description.send_keys("item description")
        procurementSubject_quantity = self.drv.find_element_by_id("procurementSubject_quantity"+lot+item)
        procurementSubject_quantity.send_keys("100")
        select_unit = Select(self.drv.find_element_by_id("select_unit"+lot+item))
        select_unit.select_by_value("LTR")

        cls_click_ = self.drv.find_element_by_id("cls_click_")
        cls_click_.click()
        add_classifier= WebDriverWait(self.drv, 20).until(EC.visibility_of_element_located((By.ID, "add-classifier")))
        search_classifier_text = self.drv.find_element_by_id("search-classifier-text")
        search_classifier_text.send_keys("15000000-8")
        WebDriverWait(self.drv, 20).until(EC.visibility_of_element_located((By.XPATH, "//li[@aria-selected = 'true']")))
        add_classifier.click()

        WebDriverWait(self.drv, 20).until(EC.invisibility_of_element_located((By.XPATH, "//div[@id = 'modDialog']")))

        btn_otherClassifier = self.drv.find_element_by_id("btn_otherClassifier")
        btn_otherClassifier.click()
        add_classifier = WebDriverWait(self.drv, 20).until(EC.visibility_of_element_located((By.ID, "add-classifier")))
        search_classifier_text = self.drv.find_element_by_id("search-classifier-text")
        search_classifier_text.send_keys("000")
        WebDriverWait(self.drv, 20).until(EC.visibility_of_element_located((By.XPATH, "//li[@aria-selected = 'true']")))
        add_classifier.click()

        set_datepicker(self.drv, "delivery_start_"+lot+item,
                       (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"))
        set_datepicker(self.drv, "delivery_end_" + lot + item,
                       (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"))

        select_countries = self.drv.find_element_by_id("select_countries"+lot+item)
        Select(select_countries).select_by_value("1")


        select_regions = self.drv.find_element_by_id("select_regions"+lot+item)
        WebDriverWait(self.drv, 20).until(EC.element_to_be_clickable((By.ID, "select_regions" + lot + item)))
        Select(select_regions).select_by_value("7")

        zip_code_ = self.drv.find_element_by_id("zip_code_"+lot+item)
        zip_code_.send_keys("3354345345")

        locality_  = self.drv.find_element_by_id("locality_"+lot+item)
        locality_.send_keys("Чернівці")
        street_ = self.drv.find_element_by_id("street_"+lot+item)
        street_.send_keys("Європейська")

        latutide_ = self.drv.find_element_by_id("latutide_"+lot+item)
        latutide_.send_keys("65")
        longitude_ = self.drv.find_element_by_id("longitude_"+lot+item)
        longitude_.send_keys("47")

        add_item_button = WebDriverWait(self.drv, 20).until(
            EC.element_to_be_clickable((By.ID, "update_" + lot + item)))
        add_item_button.click()

        return self

