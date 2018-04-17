import random
import sys

import os
from time import sleep

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
id = ""

if len(sys.argv) == 2:
    id = sys.argv[1]
else:
    count = 2
    id = prepare_data(count)




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
                command_executor = 'http://192.168.80.121:4444/wd/hub',
                desired_capabilities = {
                    'browserName': 'chrome',
                    'javascriptEnabled': True
                    })
    drv.maximize_window()
    drv.implicitly_wait(5)

    drv.get(url)
    print("open", url)

    WebDriverWait(drv, 200).until(
        expected_conditions.text_to_be_present_in_element(
            (By.TAG_NAME, "body"),"Активний"))


    drv.refresh()
    positions =  WebDriverWait(drv, 10).until(
                    expected_conditions.presence_of_all_elements_located(
                        (By.XPATH, "//tr[contains(@id,'positionTr')]")))

    print("positions count - ",len(positions))

    ready = None
    sleep(random.randint(1, 15))
    speed =  random.randint(1, 15)
    while ready is None:
        try:
            ready = WebDriverWait(drv, 1).until(
                expected_conditions.text_to_be_present_in_element(
                    (By.TAG_NAME, "body"), "Завершено"))
        except:
            pass
        for i in range(1,len(positions)+1):
            try:
                sleep(random.randint(1, 5))
                sleep(speed)

                offerEditInput = None
                try:
                    offerEditInput = WebDriverWait(drv, 5).until(
                        expected_conditions.visibility_of_element_located((By.ID, "offerEditInput" + str(i))))
                except:
                    pass

                if offerEditInput is not None:
                    offerMinimalStep = WebDriverWait(drv, 5).until(
                                expected_conditions.visibility_of_element_located((By.ID,"offerMinimalStep"+str(i))))
                    changeRate = WebDriverWait(drv, 5).until(
                                expected_conditions.visibility_of_element_located((By.ID,"changeRate"+str(i))))

                    offerMaximalStep = None
                    try:
                        offerMaximalStep = WebDriverWait(drv, 0.5).until(
                                expected_conditions.visibility_of_element_located((By.ID,"offerMaximalStep"+str(i))))
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

                    print("changeRate  "+str(i))
            except Exception as e:
                    print(e.__str__())

    # for m in range(1, secondsDiff + 10):
    #     #getstatusfrompage
    #     #is ready - go
    #     time.sleep(1)
    #     pass
    print("finish")
    sleep(20)
finally:
    drv.quit()




