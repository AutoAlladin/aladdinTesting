import os
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
            paint(self.drv, "publishPurchaseERROR.png")
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


    def set_delivery_adress(self, dic, item_id):
        select_countries = self.drv.find_element_by_id("select_countries" + item_id)
        Select(select_countries).select_by_value("1")
        select_regions = self.drv.find_element_by_id("select_regions" + item_id)
        WebDriverWait(self.drv, 20).until(EC.element_to_be_clickable((By.ID, "select_regions" + item_id)))
        Select(select_regions).select_by_value("7")
        zip_code_ = self.drv.find_element_by_id("zip_code_" + item_id)
        zip_code_.send_keys(get_dic_val(dic, "below.zip_code_"))
        locality_ = self.drv.find_element_by_id("locality_" + item_id)
        locality_.send_keys(get_dic_val(dic, "below.locality_"))
        street_ = self.drv.find_element_by_id("street_" + item_id)
        street_.send_keys(get_dic_val(dic, "below.street_"))
        latutide_ = self.drv.find_element_by_id("latutide_" + item_id)
        latutide_.send_keys(get_dic_val(dic, "below.latutide_"))
        longitude_ = self.drv.find_element_by_id("longitude_" + item_id)
        longitude_.send_keys(get_dic_val(dic, "below.longitude_"))

    def set_delivery_period(self, item_id):
        set_datepicker(self.drv, "delivery_start_" + item_id,
                       (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"))
        set_datepicker(self.drv, "delivery_end_" + item_id,
                       (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"))

    def set_otherDK(self, dic):
        btn_otherClassifier = self.drv.find_element_by_id("btn_otherClassifier")
        btn_otherClassifier.click()
        self.set_classifier(dic)

    def set_dk2015(self, dic):
        cls_click_ = self.drv.find_element_by_id("cls_click_")
        cls_click_.click()
        self.set_classifier(dic)

    def set_classifier(self, dic):
        add_classifier = WebDriverWait(self.drv, 20).until(EC.visibility_of_element_located((By.ID, "add-classifier")))
        search_classifier_text = self.drv.find_element_by_id("search-classifier-text")
        search_classifier_text.send_keys(get_dic_val(dic, "below.search_classifier_other"))
        WebDriverWait(self.drv, 20).until(EC.visibility_of_element_located((By.XPATH, "//li[@aria-selected = 'true']")))
        add_classifier.click()

    def set_item_base_info(self, dic, item_id):
        procurementSubject_description = self.drv.find_element_by_id("procurementSubject_description" + item_id)
        procurementSubject_description.send_keys(get_dic_val(dic, "below.item_descr"))
        procurementSubject_quantity = self.drv.find_element_by_id("procurementSubject_quantity" + item_id)
        procurementSubject_quantity.send_keys(get_dic_val(dic, "below.quantity"))
        select_unit = Select(self.drv.find_element_by_id("select_unit" + item_id))
        select_unit.select_by_value("LTR")

    def click_add_item(self, item_id):
        try:
            WebDriverWait(self.drv, 20).until(
                EC.visibility_of_element_located((By.ID, "update_" + item_id)))

            add_item_button = self.drv.find_element_by_id("update_" + item_id)
            add_item_button.click()
            print(self.drv.current_url)
        except Exception as e:
            raise  Exception(" Не нажимается кнопка add_item_button: update_" + item_id+e)
            paint(self.drv, "update_" + item_id+"ERROR.png")


    def add_item(self, dic, lot=0, item=0):
        try:
            if lot==0:
                self.set_item(dic, item, "0")
            else:
                for j in range(lot):
                        self.set_item(dic, item, j+1)

        except Exception as e:
            raise Exception(" Не нажимается кнопка add_item_button "+ e)
            paint(self.drv, "add_item_" + item_id + "ERROR.png")

        return self

    def set_item(self, dic, item, j):
        for i in range(item):
            add_procurement_subject = self.drv.find_element_by_id("add_procurement_subject" + str(j))
            add_procurement_subject.click()
            item_id = str(j) + "0"
            self.set_item_base_info(dic, item_id)
            self.set_dk2015(dic)
            WebDriverWait(self.drv, 20).until(EC.invisibility_of_element_located((By.XPATH, "//div[@id = 'modDialog']")))
            self.set_otherDK(dic)
            self.set_delivery_period(item_id)
            add_item_button = WebDriverWait(self.drv, 20).until(
                EC.element_to_be_clickable((By.ID, "update_" + item_id)))
            self.drv.execute_script("window.scroll(0, {0}-105)".format(add_item_button.location.get("y")))
            self.set_delivery_adress(dic, item_id)
            self.click_add_item(item_id)

    def add_doc(self, docs):
        documents_tab=self.drv.find_element_by_id("documents-tab")
        documents_tab.click()

        upload_document=self.drv.find_element_by_id("upload_document")
        upload_document.click()

        WebDriverWait(self.drv, 20).until(
            EC.element_to_be_selected((By.ID, "categorySelect")))

        Select(self.drv.find_element_by_id("categorySelect")).select_by_value("biddingDocuments")
        Select(self.drv.find_element_by_id("documentOfSelect")).select_by_value("Tender")


        with(open(os.path.dirname(os.path.abspath(__file__)) + '\\fortender.txt', 'w')) as f:
            f.write("wwwwwww")
        fileInput=self.drv.find_element_by_id("fileInput")
        fileInput.send_keys(os.path.dirname(os.path.abspath(__file__)) + "\\fortender.txt")

        save_file==self.drv.find_element_by_id("save_file")
        save_file