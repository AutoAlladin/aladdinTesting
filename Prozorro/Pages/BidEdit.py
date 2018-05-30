import os
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Prozorro import Utils
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Prozorro.Utils import paint


class bid:
    def __init__(self, _drv):
        self.drv = _drv
        #self.drv = webdriver.Chrome(_drv)

    def new(self,uaid, dic):
        Utils.waitFadeIn(self.drv)
        try:
            lots = WebDriverWait(self.drv, 5).until(
                        EC.presence_of_all_elements_located(
                            (By.XPATH,"//a[contains(@id,'openLotForm')]")))

            for lotForm in lots:
                suffix = lotForm.get_attribute("id").split("_")[1]
                Utils.waitFadeIn(self.drv)
                Utils.scroll_to_element(self.drv, lotForm)
                lotForm.click()

                bidLotAmount = WebDriverWait(self.drv, 20).until(
                    EC.element_to_be_clickable((By.ID, "lotAmount_{0}".format(suffix))))

                bidLotAmount.send_keys(str(dic["amount"]));
                print("  amount", str(dic["amount"]))
                time.sleep(0.2)
                Utils.waitFadeIn(self.drv)

                try:
                    if "tender_feature" in dic:
                        bidFeatures = WebDriverWait(self.drv, 1).until(
                            EC.element_to_be_clickable((By.ID, "bidFeatures_0_0"))) #".format(suffix))))
                        Select(bidFeatures).select_by_index(dic["tender_feature"])
                        print("  tender_feature",  Select(bidFeatures).first_selected_option.text)
                except TimeoutException as e :
                    paint(self.drv, "setTenderFeatureERROR.png")
                    print("  bidFeatures_0_0 not found")


                try:
                    if "lot_feature" in dic:
                        lotFeatures = WebDriverWait(self.drv, 1).until(
                            EC.element_to_be_clickable((By.ID, "lotFeatures_0_0")))  #{0}".format(suffix))))
                        Select(lotFeatures).select_by_index(dic["lot_feature"])
                        print("  lot_feature", Select(lotFeatures).first_selected_option.text)
                except TimeoutException as e :
                    paint(self.drv, "setLotFeatureERROR.png")
                    print("  lotFeatures_0_0 not found")

                try:
                    if "item_feature" in dic:
                        lotItemFeatures = WebDriverWait(self.drv, 1).until(
                            EC.element_to_be_clickable((By.ID, "lotItemFeatures_0_0")))  #{0}".format(suffix))))
                        Select(lotItemFeatures).select_by_index(dic["item_feature"])
                        print("  lotItemFeatures", Select(lotItemFeatures).first_selected_option.text )
                except TimeoutException as e :
                    paint(self.drv, "setItemLotFeatureERROR.png")
                    print("  lotItemFeatures_0_0 not found")

                bidDocInput_biddingDocuments = self.drv.find_element_by_id("openLotDocuments_biddingDocuments_0") # {0}".format(suffix))
                Utils.scroll_to_element(self.drv, bidDocInput_biddingDocuments)
                Utils.waitFadeIn(self.drv)
                bidDocInput_biddingDocuments.click()
                with(open(os.path.dirname(os.path.abspath(__file__))+os.sep+'forbid.txt', 'w')) as f:
                    f.write("qqqqqqq")
                Utils.waitFadeIn(self.drv)
                self.drv.find_element_by_id("bidDocInput_biddingDocuments_0").send_keys(os.path.dirname(os.path.abspath(__file__)) + "\\forbid.txt")
                print("  biddingDocuments ", os.path.abspath(__file__) +os.sep+ "forbid.txt")

            suffix = 0

            submitBid = self.drv.find_element_by_id("lotSubmit_{0}".format(suffix))
            Utils.scroll_to_element(self.drv, submitBid)
            time.sleep(0.2)
            Utils.waitFadeIn(self.drv)

            submitBid.click()
            print("  submitBid")
            time.sleep(0.2)

            b = WebDriverWait(self.drv, 5).until(
                EC.presence_of_element_located((By.XPATH,
                                                "//div[contains(@class,'jconfirm-buttons')]/button[1]")))
            Utils.waitFadeIn(self.drv)
            b.click()
            time.sleep(0.2)

            b = WebDriverWait(self.drv, 5).until(
                EC.presence_of_element_located((By.XPATH,
                                                "//div[contains(@class,'jconfirm-buttons')]/button[1]")))
            Utils.waitFadeIn(self.drv)
            b.click()
            print("  toaster killed, bid for lot added")
            time.sleep(0.2)

            Utils.waitFadeIn(self.drv)

            bidGUID = WebDriverWait(self.drv, 60).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[@ng-show='bid.guid']")))
            print("bid guid: " + bidGUID.text.strip())
            return bidGUID.text.strip()

        except TimeoutException as e:
            try:
                bidAmount  = WebDriverWait(self.drv, 5).until(
                    EC.element_to_be_clickable((By.ID, "bidAmount")))

                Utils.waitFadeIn(self.drv)
                bidAmount.send_keys(str(dic["amount"]));

                bidDocInput_biddingDocuments = self.drv.find_element_by_id("openDocuments_biddingDocuments")
                bidDocInput_biddingDocuments.click()
                with(open(os.path.dirname(os.path.abspath(__file__)) + '\\forbid.txt', 'w')) as f:
                    f.write("qqqqqqq")

                self.drv.find_element_by_id("bidDocInput_biddingDocuments").send_keys(os.path.dirname(os.path.abspath(__file__)) + "\\forbid.txt")

                submitBid = self.drv.find_element_by_id("submitBid")
                Utils.scroll_to_element(self.drv, submitBid)
                time.sleep(0.2)
                Utils.waitFadeIn(self.drv)

                submitBid.click()
                time.sleep(0.2)

                Utils.waitFadeIn(self.drv)

                b = WebDriverWait(self.drv, 5).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    "//div[contains(@class,'jconfirm-buttons')]/button[1]")))
                Utils.waitFadeIn(self.drv)
                b.click()
                time.sleep(0.2)

                b = WebDriverWait(self.drv, 5).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    "//div[contains(@class,'jconfirm-buttons')]/button[1]")))
                Utils.waitFadeIn(self.drv)
                b.click()
                time.sleep(0.2)

                Utils.waitFadeIn(self.drv)
                bidGUID = WebDriverWait(self.drv, 60).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[@ng-show='bid.guid']")))

                print("bid guid: " + bidGUID.text.strip())

                return bidGUID.text.strip()
            except Exception as e:
                paint(self.drv, "addBidPurchaseERROR.png")
                raise e
            pass






