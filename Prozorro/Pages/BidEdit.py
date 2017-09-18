import os
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from Prozorro import  Utils
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class bid:
    def __init__(self, _drv):
        self.drv = _drv
        #self.drv = webdriver.Chrome(_drv)

    def new(self):
        bidAmount = self.drv.find_element_by_id("bidAmount")
        bidAmount.send_keys("100.22");

        Utils.waitFadeIn(self.drv)

        submitBid = self.drv.find_element_by_id("submitBid")
        openDocuments_biddingDocuments = self.drv.find_element_by_id("openDocuments_biddingDocuments")

        self.drv.execute_script("window.scroll(0, {0}-65)".format(openDocuments_biddingDocuments.location.get("y")))

        Utils.waitFadeIn(self.drv)
        openDocuments_biddingDocuments.click()

        Utils.waitFadeIn(self.drv)
        bidDocInput_biddingDocuments =self.drv.find_element_by_id("bidDocInput_biddingDocuments")

        with(open(os.path.dirname(os.path.abspath(__file__))+'\\forbid.txt','w')) as f:
            f.write("qqqqqqq")

        bidDocInput_biddingDocuments.send_keys(os.path.dirname(os.path.abspath(__file__))+"\\forbid.txt")

        self.drv.execute_script("window.scroll(0, {0}-65)".format(submitBid.location.get("y")))
        Utils.waitFadeIn(self.drv)

        submitBid.click()

        bidGUID = WebDriverWait(self.drv, 20).until(
            EC.visibility_of_element_located((By.XPATH,"//div[@ng-if='bid.isPublished']/span[2]")))

        return bidGUID


