import random
import sys

import os
from random import shuffle
from time import sleep

import requests

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Aladdin.Accounting.decorators.StoreTestResult import get_ip_address
from Auction.run_prepare import prepare_data

fo ="C:\\Users\\dev2\\PycharmProjects\\AladdinTesting"
sys.path.append(fo)
subdirs = [x[0] for x in os.walk(fo)
           if not x[0].startswith("_")
           and not x[0].startswith(".")
           and x[0].find(".git") == -1
           ]
sys.path.extend(subdirs)

from selenium import webdriver
from Aladdin.Accounting.AladdinUtils import MdbUtils

def run_remote(_id = ""):
    mdb = MdbUtils()
    url = ""
    id = ""

    if _id == "":
        if len(sys.argv) == 2:
            id = sys.argv[1]
        else:
            #dfgsdfgsdfgxdfg
            count = 2
            id = prepare_data(count)
    else:
        id = _id

    #  только указаннуб позицию в момент укзанный на сервере
    #logic2 =
    # по порядку по ссылке в БД
    logic2 = _id ==""

    test_a = mdb.test_auction.find_one({"_id":id})
    parts = test_a["parts"]
    for p in parts:
        if p["used"] == False:
            try:
                url = p["url"]
                if logic2:
                    p["used"] = True
                    mdb.test_auction.update({"_id":id, "parts.url": url},
                                        {"$set": {"parts.$.used": True}})
                break
            except Exception as e:
                url = ""
                print(e.__str__())
                continue

    if url == "": exit()

    nodeId  =""
    drv = None
    try:
        drv = webdriver.Remote(
                    command_executor = 'http://192.168.80.139:4444/wd/hub',
                    desired_capabilities = {
                        'browserName': 'chrome',
                        'javascriptEnabled': True
                        # 'chromeOptions': {
                        #         "args": ["headless"]
                        #     }
                    }

        )

        ss_id = drv.session_id
        ss_info = requests.get("http://192.168.80.139:4444/grid/api/testsession?session="+ss_id)

        nodeId = ss_info.json()["proxyId"][7:]

        drv.maximize_window()
        drv.implicitly_wait(5)

        drv.get(url)
        print("open URL", nodeId)
        #todo показвать браузер с указанным в  БД ИД

        drv.refresh()
        WebDriverWait(drv, 200).until(
            expected_conditions.text_to_be_present_in_element(
                (By.TAG_NAME, "body"),"Активний"))


        positions =  WebDriverWait(drv, 10).until(
                        expected_conditions.presence_of_all_elements_located(
                            (By.XPATH, "//tr[contains(@id,'positionTr')]")))

        ready = None

        # lots = WebDriverWait(drv, 10).until(
        #                 expected_conditions.presence_of_all_elements_located(
        #                     (By.XPATH, "//tr[contains(@id,'positionTr')]")))
        #
        # click_order_lots  = [x for x in range(1,len(lots)+1)]

        while ready is None:
            try:
                ready = WebDriverWait(drv, 1).until(
                    expected_conditions.text_to_be_present_in_element(
                        (By.TAG_NAME, "body"), "Завершено"))

                break
            except:
                pass
            if not logic2:   shuffle(positions)
            #shuffle(click_order_lots)
            #
            for pos in positions:
                try:
                    #sleep(random.randint(1, ))
                    offerEditInput = None
                    try:
                        offerEditInput = pos.find_element_by_xpath("//input[contains(@id,'offerEditInput')]")
                    except:
                        pass

                    if offerEditInput is not None:
                        offerMinimalStep = pos.find_element_by_xpath("//span[contains(@id, 'offerMinimalStep')]")
                        changeRate = pos.find_element_by_xpath("//i[contains(@id,'changeRate')]")

                        offerMaximalStep = None
                        try:
                            offerMaximalStep = pos.find_element_by_xpath("//span[contains(@id,'offerMaximalStep')]")
                        except:
                            pass

                        sm=0
                        smmin = float(offerMinimalStep.text.replace(",", "").replace(" ", ""))

                        if offerMaximalStep is not None:
                            smmax=round(float(offerMaximalStep.text.replace(",","").replace(" ","")))
                            if smmin == smmax:
                                sm = smmin
                            else:
                                sm = smmin + round(smmax-smmin)-1
                                if sm < smmin : sm = smmin

                            offerEditInput.send_keys(str(sm).replace(",", "").replace(" ", ""))
                        else:
                            sm= smmin
                            offerMinimalStep.click()

                        changeRate.click()

                        try:
                            WebDriverWait(drv, 0.1).until(
                                expected_conditions.visibility_of_element_located((By.ID, "toast-container")))

                            toast_close_button = WebDriverWait(drv, 0.1).until(
                                expected_conditions.visibility_of_element_located((By.CLASS_NAME, "toast-close-button")))

                            toast_close_button.click()

                            WebDriverWait(drv, 0.1).until(
                                expected_conditions.invisibility_of_element_located((By.ID, "toast-container")))
                        except:
                            pass

                        print(nodeId+": changeRate  "+str(sm))
                except Exception as e:
                        print(nodeId+": "+e.__str__())

        if logic2: ready = True
        # for m in range(1, secondsDiff + 10):
        #     #getstatusfrompage
        #     #is ready - go
        #     time.sleep(1)
        #     pass
        sleep(1)
    except Exception as e:
        return nodeId + ": " + e.__str__()
    finally:
        if drv is not None:
            drv.quit()

    return nodeId+": finish FUTURE"

if __name__ == "__main__":
    run_remote()

