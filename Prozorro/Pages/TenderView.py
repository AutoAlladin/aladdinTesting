from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Prozorro.Pages.BidEdit import bid
from Prozorro.Utils import *
from selenium import webdriver


class TenderView:
    def __init__(self, _drv):
        self.drv = _drv
        #self.drv=webdriver.Chrome(  _drv)
        waitNotifyToast(self.drv)
        WebDriverWait(self.drv, 10).until(
            EC.visibility_of_element_located((By.ID, "info-purchase-tab")))

    def open_bids(self):

        try:
            waitFadeIn(self.drv)
            md_next_button=WebDriverWait(self.drv, 1).until(
                EC.element_to_be_clickable("md-next-button"))
            md_next_button.click()
        except:
            print("md_next_button not found")

        waitNotifyToast(self.drv)

        WebDriverWait(self.drv, 10).until(
            EC.visibility_of_element_located((By.ID, "do-proposition-tab")))

        waitNotifyToast(self.drv)
        WebDriverWait(self.drv, 1).until(
            EC.element_to_be_clickable((By.ID, "do-proposition-tab")))

        self.drv.find_element_by_id("do-proposition-tab").click()

        return bid(self.drv)

