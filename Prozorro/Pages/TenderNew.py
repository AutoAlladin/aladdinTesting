from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.select import Select
from Prozorro.Utils import set_datepicker,waitFadeIn,get_dic_val, paint


class TenderNew:
    def __init__(self, _drv):
        self.drv = _drv
        #self.drv = webdriver.Chrome(_drv)

    def click_finish_edit_button(self):
        try:
            movePurchaseView = self.drv.find_element_by_id("movePurchaseView")
            self.drv.execute_script("window.scroll(0, " + str(movePurchaseView.location["y"]) + "-"+str(self.drv.find_element_by_id("header").size["height"])+")")
            waitFadeIn(self.drv)
            movePurchaseView.click()
        except WebDriverException as w:
            raise Exception("Не нажимается кнопка movePurchaseView  - \n" + w.msg)
        return self

    def click_publish_button(self):
        try:
            waitFadeIn(self.drv)
            publishPurchase = self.drv.find_element_by_id("publishPurchase")
            waitFadeIn(self.drv)
            publishPurchase.click()

            waitFadeIn(self.drv)
            WebDriverWait(self.drv, 120).until(EC.visibility_of_element_located((By.ID, "purchaseProzorroId")))
            purchaseProzorroId =self.drv.find_element_by_id("purchaseProzorroId")

            return purchaseProzorroId.text, self.drv.current_url
        except WebDriverException as w:
            paint("publishPurchaseERROR.png")
            raise Exception("Не нажимается кнопка publishPurchase  - \n" + w.msg)
        return None


    def click_next_button(self):
        try:
            next_step = self.drv.find_element_by_id("next_step")
            self.drv.execute_script("window.scroll(0, "+str(next_step.location["y"])+")")
            waitFadeIn(self.drv)
            next_step.click()
        except WebDriverException as w:
            raise Exception("Не нажимается кнопка next_step  - \n" + w.msg)
        return self


    def set_dates(self, dic):
        try:
            dt = datetime.now()
            print(get_dic_val(dic,"below.enqueriPeriod"))
            print(get_dic_val(dic,"below.tenderPeriod"))
            set_datepicker(self.drv, "period_enquiry_start", (dt + timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S"))
            set_datepicker(self.drv, "period_enquiry_end", (dt + timedelta(minutes=get_dic_val(dic,"below.enqueriPeriod"))).strftime("%Y-%m-%d %H:%M:%S"))
            set_datepicker(self.drv, "period_tender_start", (dt + timedelta(minutes=get_dic_val(dic,"below.enqueriPeriod"))).strftime("%Y-%m-%d %H:%M:%S"))
            set_datepicker(self.drv, "period_tender_end", (dt + timedelta(minutes=get_dic_val(dic,"below.tenderPeriod"))).strftime("%Y-%m-%d %H:%M:%S"))
        except Exception as e:
            raise Exception("Чтото не так с датами шапки тендера - \n" + e)
        return self

    def set_open_tender_dates(self, dic):
        try:
            dt = datetime.now()
            set_datepicker(self.drv, "period_tender_end", (dt + timedelta(minutes=get_dic_val(dic, "open.tenderPeriod"))).strftime("%Y-%m-%d %H:%M:%S"))
        except Exception as e:
            raise Exception("Чтото не так с датами шапки тендера - \n" + e)
        return self

    def set_curr(self):
        select_currencies = self.drv.find_element_by_id("select_currencies")
        Select(select_currencies).select_by_value("string:UAH")
        is_vat = self.drv.find_element_by_xpath("//*[@id='is_vat']/div[1]/div[2]/div")
        is_vat.click()
        return self

    def set_multilot(self, dic, is_multi):
        is_multilot = self.drv.find_element_by_xpath("//*[ @id='is_multilot']/div[1]/div[2]")
        if (is_multi == "true"):
            is_multilot.click()
        else:
            budget = self.drv.find_element_by_id("budget")
            budget.send_keys(get_dic_val(dic, "below.budget"))
            min_step = self.drv.find_element_by_id("min_step")
            min_step.send_keys(get_dic_val(dic, "below.min_step"))
            min_step_percentage = self.drv.find_element_by_id("min_step_percentage")
            min_step_percentage.send_keys(get_dic_val(dic, "below.min_step_percentage"))
        return self

    def add_lot(self, count, dic):
        if count == 0:
            return self
        if count >= 1:
            for currentLot in range(count):
                lotid = str(1)
                #lotid = str(currentLot+1)
                is_add_lot = self.drv.find_element_by_id("buttonAddNewLot")
                is_add_lot.click()
                title_of_lot = self.drv.find_element_by_id("lotTitle_" + lotid)
                title_of_lot.send_keys(get_dic_val(dic, "below.title_ofLot"))
                description_of_lot = self.drv.find_element_by_id("lotDescription_" + lotid)
                description_of_lot.send_keys(get_dic_val(dic, "below.description_of_lot"))
                budget_of_lot = self.drv.find_element_by_id("lotBudget_" + lotid)
                budget_of_lot.send_keys(get_dic_val(dic, "below.budget_of_lot"))
                min_step_of_lot = self.drv.find_element_by_id("lotMinStep_" + lotid)
                min_step_of_lot.send_keys(get_dic_val(dic, "below.min_step_of_lot"))
                min_step_of_lot_perc = self.drv.find_element_by_id("lotMinStepPercentage_" + lotid)
                min_step_of_lot_perc.send_keys(get_dic_val(dic, "below.min_step_of_lot_perc"))
                save_lot = self.drv.find_element_by_xpath(".//*[@id='divLotControllerEdit']/div/div/div/div[8]/div/button[1]").click()

            next_step = self.drv.find_element_by_id("next_step")
            self.drv.execute_script("window.scroll(0, " + str(next_step.location["y"]) + ")")
            waitFadeIn(self.drv)
            next_step.click()

        return self

    def set_description(self, dic):
        title = self.drv.find_element_by_id("titleOfTenderForEdit")
        description = self.drv.find_element_by_id("description")
        title.send_keys(get_dic_val(dic, "below.title"))
        description.send_keys(get_dic_val(dic, "below.description"))
        return self

    def add_item(self, dic, lot="0", item="0"):
        add_procurement_subject=self.drv.find_element_by_id("add_procurement_subject"+lot+item)
        add_procurement_subject.click()

        add_item_button = WebDriverWait(self.drv, 20).until(EC.visibility_of_element_located((By.ID, "update_"+lot+item)))
        print(self.drv.current_url)

        procurementSubject_description = self.drv.find_element_by_id("procurementSubject_description"+lot+item)
        procurementSubject_description.send_keys(get_dic_val(dic, "below.item_descr"))
        procurementSubject_quantity = self.drv.find_element_by_id("procurementSubject_quantity"+lot+item)
        procurementSubject_quantity.send_keys(get_dic_val(dic, "below.quantity"))
        select_unit = Select(self.drv.find_element_by_id("select_unit"+lot+item))
        select_unit.select_by_value("LTR")

        cls_click_ = self.drv.find_element_by_id("cls_click_")
        cls_click_.click()
        add_classifier= WebDriverWait(self.drv, 20).until(EC.visibility_of_element_located((By.ID, "add-classifier")))
        search_classifier_text = self.drv.find_element_by_id("search-classifier-text")
        search_classifier_text.send_keys(get_dic_val(dic, "below.search_classifier_cpv"))
        WebDriverWait(self.drv, 20).until(EC.visibility_of_element_located((By.XPATH, "//li[@aria-selected = 'true']")))
        add_classifier.click()

        WebDriverWait(self.drv, 20).until(EC.invisibility_of_element_located((By.XPATH, "//div[@id = 'modDialog']")))

        btn_otherClassifier = self.drv.find_element_by_id("btn_otherClassifier")
        btn_otherClassifier.click()
        add_classifier = WebDriverWait(self.drv, 20).until(EC.visibility_of_element_located((By.ID, "add-classifier")))
        search_classifier_text = self.drv.find_element_by_id("search-classifier-text")
        search_classifier_text.send_keys(get_dic_val(dic, "below.search_classifier_other"))
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
        zip_code_.send_keys(get_dic_val(dic, "below.zip_code_"))

        locality_  = self.drv.find_element_by_id("locality_"+lot+item)
        locality_.send_keys(get_dic_val(dic, "below.locality_"))
        street_ = self.drv.find_element_by_id("street_"+lot+item)
        street_.send_keys(get_dic_val(dic, "below.street_"))

        latutide_ = self.drv.find_element_by_id("latutide_"+lot+item)
        latutide_.send_keys(get_dic_val(dic, "below.latutide_"))
        longitude_ = self.drv.find_element_by_id("longitude_"+lot+item)
        longitude_.send_keys(get_dic_val(dic, "below.longitude_"))

        add_item_button = WebDriverWait(self.drv, 20).until(
            EC.element_to_be_clickable((By.ID, "update_" + lot + item)))
        add_item_button.click()

        return self

