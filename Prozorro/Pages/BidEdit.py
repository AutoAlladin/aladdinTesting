import os
import time
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from Prozorro import Utils
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class bid:
    def __init__(self, _drv):
        self.drv = _drv
        #self.drv = webdriver.Chrome(_drv)

    def new(self,prepare=0,uaid="", bidAm=100.2):

        try:
            try:
                bidAmount = WebDriverWait(self.drv, 60).until(
                    EC.visibility_of_element_located(
                        (By.ID,"bidAmount")))

                bidAmount.send_keys(str(bidAm));
                Utils.waitFadeIn(self.drv)
            except Exception as r:
                raise Exception("bidAmount - "+r)

            submitBid = self.drv.find_element_by_id("submitBid")
            openDocuments_biddingDocuments = self.drv.find_element_by_id("openDocuments_biddingDocuments")

            self.drv.execute_script("window.scroll(0, {0}-105)".format(openDocuments_biddingDocuments.location.get("y")))

            Utils.waitFadeIn(self.drv)
            openDocuments_biddingDocuments.click()

            Utils.waitFadeIn(self.drv)
            bidDocInput_biddingDocuments =self.drv.find_element_by_id("bidDocInput_biddingDocuments")
            with(open(os.path.dirname(os.path.abspath(__file__))+'\\forbid.txt','w')) as f:
                f.write("qqqqqqq")
            bidDocInput_biddingDocuments.send_keys(os.path.dirname(os.path.abspath(__file__))+"\\forbid.txt")

            Utils.scroll_to_element(self.drv,submitBid)
            Utils.waitFadeIn(self.drv)

            if prepare == 0:
                submitBid.click()
                Utils.waitFadeIn(self.drv)

                b = WebDriverWait(self.drv, 5).until(
                    EC.presence_of_element_located((By.XPATH,
                         "//div[contains(@class,'jconfirm-buttons')]/button[1]")))
                b.click()

                b = WebDriverWait(self.drv, 5).until(
                    EC.presence_of_element_located((By.XPATH,
                        "//div[contains(@class,'jconfirm-buttons')]/button[1]")))
                b.click()

                Utils.waitFadeIn(self.drv)
                bidGUID =WebDriverWait(self.drv, 30).until(
                    EC.visibility_of_element_located((By.XPATH,"//span[@ng-show='bid.guid']")))

                print("bid guid: " +bidGUID.text.strip())

                return bidGUID.text.strip()
            else:
                return None

        except Exception as e:
            Utils.paint(self.drv,"new_bir_ERROR_UAID{0}.png".format(uaid))
            pass




