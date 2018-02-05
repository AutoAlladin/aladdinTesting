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

    def new(self,prepare=0,uaid=""):

        try:
            try:
                bidAmount = self.drv.find_element_by_id("bidAmount")
                bidAmount.send_keys("100.22");
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

                WebDriverWait(self.drv, 20).until(
                    EC.visibility_of_element_located((By.XPATH,"//div[@ng-if='bid.isPublished']/span[2]")))

                bidGUID =self.drv.find_element_by_xpath("//div[@ng-if='bid.isPublished']/span[2]")

                self.drv.execute_script("window.scroll(0, {0}-105)".format(bidGUID.location.get("y")))

                print(bidGUID.text())

                return bidGUID.text()
            else:
                return None

        except Exception as e:
            Utils.paint(self.drv,"new_bir_ERROR_UAID{0}.png".format(uaid))
            pass




