#!/usr/bin/python3 -u

import os
import random


from datetime import datetime, timedelta
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.select import Select
from Prozorro.Utils import set_datepicker,waitFadeIn,get_dic_val, paint,scroll_to_element


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
            publishPurchase = \
                WebDriverWait(self.drv, 5).until(EC.visibility_of_element_located((By.ID,"publishPurchase")))

            waitFadeIn(self.drv)
            publishPurchase.click()

            waitFadeIn(self.drv)
            WebDriverWait(self.drv, 120).until(EC.visibility_of_element_located((By.ID, "purchaseProzorroId")))
            purchaseProzorroId = self.drv.find_element_by_id("purchaseProzorroId")
            print("click publish", self.drv.current_url        )

            return purchaseProzorroId.text, self.drv.current_url
        except WebDriverException as w:
            toast_title = ""
            toast_message = ""
            try:
                WebDriverWait(self.drv, 1).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='toast toast-error']")))
                toast_title =self.drv.find_element_by_xpath("//div[@class='toast toast-error']//div[@class='toast-title']").text()
                toast_message = self.drv.find_element_by_xpath("//div[@class='toast toast-error']//div[@class='toast-message']").text()
            except:
                pass
            paint(self.drv, "publishPurchaseERROR.png")
            raise Exception("Не нажимается кнопка publishPurchase {0}  - \n\t {1}\t{2}".\
                            format(self.drv.current_url, toast_title, toast_message) +\
                            w.msg)

        return None


    def click_next_button(self):
        try:
            #next_step = self.drv.find_element_by_xpath("//button[@id='next_step'][2]")
            #self.drv.execute_script("window.scroll(0, "+str(next_step.location["y"])+")")
            waitFadeIn(self.drv)
            self.drv.execute_script("$('#next_step').click()")
            sleep(1)

            # WebDriverWait(self.drv, 20).until(
            #     EC.invisibility_of_element_located(
            #         (By.ID, "next_step")
            #     )
            # )

            #next_step.click()
            print("click NEXT", self.drv.current_url)
        except WebDriverException as w:
            raise Exception("Не нажимается кнопка next_step  - \n" + w.msg)
        return self

    def set_dates(self, dic):
        print("start set_dates")
        try:
            dt = datetime.now()
            set_datepicker(
                self.drv,
                "period_enquiry_start",
                (dt + timedelta(seconds = 20)).strftime("%d-%m-%Y %H:%M:%S"))
            set_datepicker(
                self.drv,
                "period_enquiry_end",
                (dt + timedelta(
                    minutes=get_dic_val(dic,"below.enqueriPeriod")
                )
                 ).strftime("%d-%m-%Y %H:%M:%S"))

            set_datepicker(self.drv, "period_tender_start",
                           (dt + timedelta(
                               minutes=get_dic_val(dic,"below.enqueriPeriod"))
                            ).strftime("%d-%m-%Y %H:%M:%S"))

            set_datepicker(self.drv, "period_tender_end",
                           (dt + timedelta(
                               minutes=get_dic_val(dic,"below.enqueriPeriod")+get_dic_val(dic,"below.tenderPeriod"))
                            ).strftime("%d-%m-%Y %H:%M:%S"))
            print("end set_dates")
        except Exception as e:
            raise Exception("Чтото не так с датами шапки тендера - \n" + e)
        return self

    def set_open_tender_dates(self, dic):
        try:
            dt = datetime.now()
            set_datepicker(self.drv, "period_tender_end", (dt + timedelta(minutes=get_dic_val(dic, "open.tenderPeriod"))).strftime("%d-%m-%Y %H:%M:%S"))
        except Exception as e:
            raise Exception("Чтото не так с датами шапки тендера - \n" + e)
        return self

    def set_curr(self):
        select_currencies = self.drv.find_element_by_id("select_currencies")
        Select(select_currencies).select_by_value("string:UAH")
        is_vat = self.drv.find_element_by_xpath("//*[@id='is_vat']/div[1]/div[2]/div")
        waitFadeIn(self.drv)
        is_vat.click()
        return self

    def set_multilot(self, dic, is_multi):
        is_multilot = self.drv.find_element_by_xpath("//*[ @id='is_multilot']/div[1]/div[2]")
        if (is_multi == "true"):
            is_multilot.click()
        else:
            # bu = random.randrange(1000, 990000)
            budget = self.drv.find_element_by_id("budget")
            # budget.send_keys(bu)
            b = get_dic_val(dic,"below.budget")
            print("XYZZZZZZZZ", b)
            budget.send_keys(b)

            min_step_p = random.randrange(1, 3)
            min_step_percentage = self.drv.find_element_by_id("min_step_percentage")
            min_step_percentage.send_keys(min_step_p)
        return self

    def add_lot(self, count, dic):
        if count == 0:
            return self
        if count >= 1:
            for currentLot in range(count):
                print("start Add lot ",get_dic_val(dic, "below.description_of_lot"))
                lotid = str(1)
                #lotid = str(currentLot+1)
                WebDriverWait(self.drv, 20).until(
                    EC.element_to_be_clickable((By.ID, "buttonAddNewLot")))
                is_add_lot = self.drv.find_element_by_id("buttonAddNewLot")
                waitFadeIn(self.drv)
                is_add_lot.click()

                title_of_lot = self.drv.find_element_by_id("lotTitle_" + lotid)
                title_of_lot.send_keys(str(currentLot)+" - "+get_dic_val(dic, "below.title_ofLot"))
                description_of_lot = self.drv.find_element_by_id("lotDescription_" + lotid)
                description_of_lot.send_keys(get_dic_val(dic, "below.description_of_lot"))
                budget_of_lot = self.drv.find_element_by_id("lotBudget_" + lotid)
                budget_of_lot.send_keys(get_dic_val(dic, "below.budget_of_lot"))
                min_step_of_lot = self.drv.find_element_by_id("lotMinStep_" + lotid)
                min_step_of_lot.send_keys(get_dic_val(dic, "below.min_step_of_lot"))
                min_step_of_lot_perc = self.drv.find_element_by_id("lotMinStepPercentage_" + lotid)
                min_step_of_lot_perc.send_keys(get_dic_val(dic, "below.min_step_of_lot_perc"))
                self.drv.find_element_by_xpath("//div[contains(@id,'updateOrCreateLot')]//button[@class='btn btn-success']").click()
                print("end Add lot")

            next_step = self.drv.find_element_by_xpath("//button[@id='next_step'][1]")
            self.drv.execute_script("window.scroll(0, " + str(next_step.location["y"]+10) + ")")
            waitFadeIn(self.drv)
            #next_step.click()
            self.drv.execute_script("$('#next_step').click()")

        return self


    def set_description(self, dic,nom):
        print("start Set  description")
        title = WebDriverWait(self.drv, 20).until(
                EC.visibility_of_element_located(
                    (By.ID, "titleOfTenderForEdit")
                )
            )

        description = self.drv.find_element_by_id("description")
        title.send_keys(get_dic_val(dic, "below.title"))
        description.send_keys(get_dic_val(dic, "below.description"))

        print("end Set  description")

        return self

    def set_delivery_adress(self, dic, item_id):
        print("start Set_delivery_adress")
        select_countries = self.drv.find_element_by_xpath("//div[@id='procurementSubjectCountryWrap{0}']//select[contains(@id,'countries')]".format(item_id))
        Select(select_countries).select_by_value("1")

        select_regions =  self.drv.find_element_by_xpath("//div[@id='procurementSubjectCountryWrap{0}']//select[contains(@id,'regions')]".format(item_id))
        WebDriverWait(self.drv, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='procurementSubjectCountryWrap{0}']//select[contains(@id,'regions')]".format(item_id))))

        sleep(1.5)
        Select(select_regions).select_by_visible_text(get_dic_val(dic, "below.region"))
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
        print("end Set_delivery_adress")


    def set_delivery_period(self, item_id):
        print("start Set_delivery_period")
        set_datepicker(self.drv, "delivery_start_" + item_id,
                       (datetime.now() + timedelta(days=1)).strftime("%d-%m-%Y %H:%M:%S"))
        set_datepicker(self.drv, "delivery_end_" + item_id,
                       (datetime.now() + timedelta(days=1)).strftime("%d-%m-%Y %H:%M:%S"))
        print("end Set_delivery_period")

    def set_otherDK(self, dic):
        print("start set_otherDK")
        btn_otherClassifier = self.drv.find_element_by_id("btn_otherClassifier")
        btn_otherClassifier.click()
        self.set_classifier(dic)
        print("end set_otherDK")

    def set_dk2015(self, dic):
        print("start set_dk2015")
        cls_click_ = self.drv.find_element_by_id("cls_click_")
        waitFadeIn(self.drv)
        cls_click_.click()
        add_classifier = WebDriverWait(self.drv, 20).until(EC.visibility_of_element_located((By.ID, "add-classifier")))
        search_classifier_text = self.drv.find_element_by_id("search-classifier-text")
        search_classifier_text.send_keys(get_dic_val(dic, "below.search_classifier_cpv"))
        WebDriverWait(self.drv, 20).until(EC.visibility_of_element_located((By.XPATH, "//li[@aria-selected = 'true']")))
        add_classifier.click()
        print("end set_dk2015")

    def set_classifier(self, dic):
        add_classifier = WebDriverWait(self.drv, 20).until(EC.visibility_of_element_located((By.ID, "add-classifier")))
        search_classifier_text = self.drv.find_element_by_id("search-classifier-text")
        search_classifier_text.send_keys(get_dic_val(dic, "below.search_classifier_other"))
        WebDriverWait(self.drv, 20).until(EC.visibility_of_element_located((By.XPATH, "//li[@aria-selected = 'true']")))
        add_classifier.click()

    def set_item_base_info(self, dic, item_id,item_vomber):
        print("  start set_item_base_info")
        procurementSubject_description =WebDriverWait(self.drv, 20).\
        until(EC.visibility_of_element_located((By.ID, "procurementSubject_description" + item_id)))

        procurementSubject_description.send_keys(str(item_vomber)+str(item_id)+" - "+get_dic_val(dic, "below.item_descr"))

        q=random.randrange(1,700)

        procurementSubject_quantity = self.drv.find_element_by_id("procurementSubject_quantity" + item_id)
        procurementSubject_quantity.send_keys(q)
        #procurementSubject_quantity.send_keys(get_dic_val(dic, "below.quantity"))

        unit= random.choice(["KVR", "BX", "D44", "RM", "SET", "GRM", "HUR","LTR"])

        select_unit = Select(self.drv.find_element_by_xpath("//div[@id='procurementSubjectUnitWrap{0}']//select".format(item_id)))
        select_unit.select_by_value(unit)
        #select_unit.select_by_value("LTR")
        print("  end set_item_base_info")

    def click_add_item(self, item_id):
        try:
            WebDriverWait(self.drv, 20).until(
                EC.visibility_of_element_located((By.ID, "update_" + item_id)))

            add_item_button = self.drv.find_element_by_id("update_" + item_id)
            add_item_button.click()
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
            sleep(1)
        except Exception as e:
            raise Exception(" Не нажимается кнопка add_item_button "+ str(e))
            paint(self.drv, "add_item_" + item_id + "ERROR.png")

        return self

    def set_item(self, dic, item, j):
        for i in range(item):
            print("start set_item", i)
            waitFadeIn(self.drv)
            add_procurement_subject = \
                WebDriverWait(self.drv, 5).until(
                    EC.element_to_be_clickable((By.ID,"add_procurement_subject" + str(j))))

            waitFadeIn(self.drv)
            scroll_to_element(self.drv,add_procurement_subject)
            add_procurement_subject.click()

            item_id = str(j) + "0"
            self.set_item_base_info(dic, item_id, i)
            self.set_dk2015(dic)
            WebDriverWait(self.drv, 20).until(EC.invisibility_of_element_located((By.XPATH, "//div[@id = 'modDialog']")))

            self.set_otherDK(dic)

            self.set_delivery_period(item_id)
            self.set_delivery_adress(dic, item_id)

            add_item_button = WebDriverWait(self.drv, 20).until(
                EC.element_to_be_clickable((By.ID, "update_" + item_id)))
            scroll_to_element(self.drv, add_item_button)
            self.click_add_item(item_id)
            print("start set_item", i)

    def add_doc(self, docs):
        try:
            if docs > 0:
                documents_tab = WebDriverWait(self.drv, 20).until(
                    EC.presence_of_element_located(
                        (By.ID, "documents-tab")))

                scroll_to_element(self.drv,documents_tab)
                waitFadeIn(self.drv)
                documents_tab.click()

            for i in range(docs):
                print("start add_doc")
                waitFadeIn(self.drv)
                upload_document=WebDriverWait(self.drv, 20).until(
                    EC.visibility_of_element_located(
                        (By.ID, "upload_document")
                    )
                )

                waitFadeIn(self.drv)
                upload_document.click()

                WebDriverWait(self.drv, 20).until(
                    EC.visibility_of_element_located((By.ID,"categorySelect")))

                Select(self.drv.find_element_by_id("categorySelect")).select_by_value("biddingDocuments")
                Select(self.drv.find_element_by_id("documentOfSelect")).select_by_value("Tender")

                if not os.path.isfile(os.path.abspath(__file__)+ '\\fortender{0}.txt'.format(i)):
                    with(open(os.path.dirname(os.path.abspath(__file__)) + '\\fortender{0}.txt'.format(i), 'w')) as f:
                        f.write("wwwwwww")
                fileInput=self.drv.find_element_by_id("fileInput")
                fileInput.send_keys(os.path.dirname(os.path.abspath(__file__)) + "\\fortender{0}.txt".format(i))

                save_file=self.drv.find_element_by_id("save_file")
                save_file.click()

                sleep(15)
                print("end add_doc")

        except Exception as e:
            paint(self.drv, "addDocERROR.png")
            raise Exception("Error add_doc {0}\n".format(self.drv.current_url)+str(e))
        return self

    def set_feature_decription(self, dic, end):
        print("start set_feature_decription")
        WebDriverWait(self.drv, 20).until(EC.visibility_of_element_located((By.ID, "featureTitle_"+end)))
        featureTitle=self.drv.find_element_by_id("featureTitle_"+end)
        featureTitle.send_keys(get_dic_val(dic,"feature.title"))

        featureDescription=self.drv.find_element_by_id("featureDescription_"+end)
        featureDescription.send_keys(get_dic_val(dic, "feature.description"))
        print("end set_feature_decription")

    def add_feature_enum(self,dic,enum_index, lot_index=0):
        print("start add_feature_enum")
        featureEnumAdd = self.drv.find_element_by_id("addFeatureEnum_"+str(lot_index)+"_0")
        featureEnumAdd.click()

        featureEnumValue =   WebDriverWait(self.drv, 20).until(
                EC.visibility_of_element_located(
                    (By.ID, "featureEnumValue_"+str(lot_index)+"_0_"+str(enum_index))))
        featureEnumValue.clear()
        featureEnumValue.send_keys(str(enum_index))

        featureEnumTitle = self.drv.find_element_by_id(
            "featureEnumTitle_"+str(lot_index)+"_0_"+str(enum_index))
        featureEnumTitle.clear()
        featureEnumTitle.send_keys(get_dic_val(dic, "feature.option_name"))

        featureEnumDescription = self.drv.find_element_by_id(
            "featureEnumDescription_"+str(lot_index)+"_0_"+str(enum_index))
        featureEnumDescription.clear()
        featureEnumDescription.send_keys(get_dic_val(dic, "feature.option_description"))
        print("end add_feature_enum")

    def set_feature_zero_enum(self, dic, end="0"):
        print("start set_feature_zero_enum")
        WebDriverWait(self.drv, 20).until(EC.visibility_of_element_located((By.ID, "featureEnumTitle_"+end+"_0_0")))
        featureEnumTitle = self.drv.find_element_by_id("featureEnumTitle_"+end+"_0_0")
        featureEnumTitle.clear()
        featureEnumTitle.send_keys(get_dic_val(dic, "feature.titleEnum_zero"))

        featureEnumDescription = self.drv.find_element_by_id("featureEnumDescription_"+end+"_0_0")
        featureEnumDescription.clear()
        featureEnumDescription.send_keys(get_dic_val(dic, "feature.descriptionEnum_zero"))
        print("start set_feature_zero_enum")

    def add_feature_to_tender(self, features, items, dic,to_item=True):
        WebDriverWait(self.drv, 20).until(EC.visibility_of_element_located((By.ID, "add_features0")))
        for findex in range(features):
            print("start add_feature_to_tender")
            waitFadeIn(self.drv)
            add_features = self.drv.find_element_by_id("add_features0")
            add_features.click()
            self.set_feature_decription(dic,"0_0")
            if to_item:
                to_i = self.drv.find_element_by_xpath("//label[@for='featureOf_0_0']")
                to_i.click()
                select =  WebDriverWait(self.drv, 20).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//select[@id='featureItem_0_0']")
                    )
                )
                Select(select).select_by_index(1)

            self.set_feature_zero_enum(dic)

            for enum_index in range(get_dic_val(dic,"feature.enum_count", 2)-1):
                self.add_feature_enum(dic, enum_index+1)

            updateFeature=WebDriverWait(self.drv, 20).until(EC.element_to_be_clickable((By.ID, "updateFeature_0_0")))
            scroll_to_element(self.drv, updateFeature)

            updateFeature.click()
            print("end add_feature_to_tender")
        pass

    def add_feature_to_lot(self, features, lots, items,dic, to_item=True):
        for lotix in range(1,lots+1):
            for findex in range(features):
                print("start add_feature_to_lot")
                waitFadeIn(self.drv)
                add_features = WebDriverWait(self.drv, 20).until(
                    EC.visibility_of_element_located(
                        (By.ID, "add_features"+str(lotix))
                        )
                    )
                scroll_to_element(self.drv,add_features)
                add_features.click()
                self.set_feature_decription(dic, str(lotix)+"_0")

                isPara = (findex % 2 != 0)
                _to_item = False
                if isPara: _to_item = get_dic_val(dic, "feature.lot_item", False)
                if _to_item:
                    to_i = self.drv.find_element_by_xpath("//label[@for='featureOf_"+str(lotix)+"_0']")
                    scroll_to_element(self.drv,to_i)
                    to_i.click()
                    select = WebDriverWait(self.drv, 20).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, "//select[@id='featureItem_"+str(lotix)+"_0']")
                        )
                    )
                    scroll_to_element(self.drv, select)
                    Select(select).select_by_index(1)

                self.set_feature_zero_enum(dic,end=str(lotix))

                for enum_index in range(get_dic_val(dic, "feature.enum_count", 2)-1):
                     self.add_feature_enum(dic,enum_index+1, lotix)

                updateFeature = WebDriverWait(self.drv, 20).until(
                    EC.visibility_of_element_located(
                        (By.ID, "updateFeature_"+str(lotix)+"_0")
                    )
                )
                scroll_to_element(self.drv,updateFeature)
                updateFeature.click()
                print("start add_feature_to_lot")


    def add_features(self, dic, lots, items, features=0):
        try:
            if features > 0:
                WebDriverWait(self.drv, 20).until(
                    EC.visibility_of_element_located((By.ID, "features-tab")))
                features_tab = self.drv.find_element_by_id("features-tab")
                waitFadeIn(self.drv)
                features_tab.click()

                _to_item = get_dic_val(dic, "feature.tender_item", False)
                self.add_feature_to_tender(features, items, dic, to_item=False)

                if lots > 0:
                    self.add_feature_to_lot(features, lots, items, dic, to_item=_to_item)
                print("IS FEATURE")

        except WebDriverException as e:
            paint(self.drv, "addFeatureERROR.png")
            raise Exception("Error add_feature {0}\n".format(self.drv.current_url) + e.msg)

        return self

