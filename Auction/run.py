import sys

import os
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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

mdb = MdbUtils()
url = ""

count = 2
id = prepare_data(count)

#id = sys.argv[1]


test_a = mdb.test_auction.find_one({"_id":id})
parts = test_a["parts"]
for p in parts:
    if p["used"] == False:
        try:
            p["used"] = True
            url = p["url"]
            mdb.test_auction.update({"_id":id, "parts.url": url},
                                    {"$set": {"parts.$.used": True}})
            break
        except Exception as e:
            url = ""
            print(e.__str__())
            continue

if url == "": exit()
try:
    drv = webdriver.Remote(
                command_executor = 'http://192.168.56.1:4444/wd/hub',
                desired_capabilities = {
                    'browserName': 'chrome',
                    'javascriptEnabled': True
                    })
    drv.maximize_window()
    drv.implicitly_wait(5)

    drv.get(url)
    print("open", url)

    WebDriverWait(drv, 120).until(
        expected_conditions.text_to_be_present_in_element(
            (By.TAG_NAME, "body"),"Активний"))


    positions =  WebDriverWait(drv, 5).until(
                    expected_conditions.visibility_of_all_elements_located(
                        (By.XPATH, "//tr[contains(@id,'positionTr')]")))

    print("positions count - ",len(positions))

    for i in range(1,len(positions)):
        offerMinimalStep = WebDriverWait(drv, 5).until(
                    expected_conditions.visibility_of_element_located((By.ID,"offerMinimalStep"+str(i))))
        offerEditInput = WebDriverWait(drv, 5).until(
                    expected_conditions.visibility_of_element_located((By.ID,"offerEditInput"+str(i))))
        changeRate = WebDriverWait(drv, 5).until(
                    expected_conditions.visibility_of_element_located((By.ID,"changeRate"+str(i))))

        offerMaximalStep = None
        try:
            offerMaximalStep = WebDriverWait(drv, 5).until(
                    expected_conditions.visibility_of_element_located((By.ID,"offerMaximalStep"+str(i))))
        except:
            pass

        sm=0
        if offerMaximalStep is not None:
            sm=round(float(offerMaximalStep.text.replace(",","").replace(" ","")))
            print("max step - "+str(sm))

        sm= round((sm + float(offerMinimalStep.text.replace(",","").replace(" ","")).is_integer())/2 )+10
        print("middle step - "+str(sm))

        offerEditInput.send_keys(str(sm))
        print("send "+str(sm))

        changeRate.click()
        print("changeRate  "+str(i))

    # for m in range(1, secondsDiff + 10):
    #     #getstatusfrompage
    #     #is ready - go
    #     time.sleep(1)
    #     pass
    print("finish")
finally:
    drv.quit()




