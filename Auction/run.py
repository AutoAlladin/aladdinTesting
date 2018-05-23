import random
import sys

import os
from datetime import datetime
from time import sleep

import requests

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


fo = os.path.dirname(os.path.abspath(__file__))
sys.path.append(fo)
subdirs = [x[0] for x in os.walk(fo)
           if not x[0].startswith("_")
           and not x[0].startswith(".")
           and x[0].find(".git") == -1
           ]

sys.path.extend(subdirs)

from selenium import webdriver

def wait_until(specified_dt: datetime):
    refresh = 0.01
    current_dt = datetime.now()

    while current_dt < specified_dt:
        current_dt = datetime.now()
        if (specified_dt - current_dt).microseconds>10:
            sleep(refresh) 

def run_remote(part):
    stepCount = part["stepCount"]
    time_start = part["time_start"]
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


        drv.implicitly_wait(2)

        drv.get(part["part"]["url"])
        drv.maximize_window()
        drv.execute_script("window.scroll(2000,0)")
        print("open URL", nodeId, datetime.now().isoformat())
        #todo показвать браузер с указанным в  БД ИД

        WebDriverWait(drv, 200).until(
            expected_conditions.text_to_be_present_in_element(
            (By.TAG_NAME, "body"),"Активний"))

        sleep(10)
        positions =  WebDriverWait(drv, 10).until(
                        expected_conditions.presence_of_all_elements_located(
                            (By.XPATH, "//tr[contains(@id,'positionTr')]")))



        for step in range(stepCount):
            # try:
            #     ready = WebDriverWait(drv, 0.2).until(
            #         expected_conditions.text_to_be_present_in_element(
            #             (By.TAG_NAME, "body"), "Завершено"))
            #
            #     break
            # except:
            #     pass

            positionsRes=[]
            for p in part["part"]["position_id"]:
                positionsRes.append(positions[p])

            if time_start is not None:
               wait_until(time_start)

            for pos in positionsRes:
                clicker(drv, nodeId, pos)

    except Exception as e:
        return nodeId + ": " + e.__str__()
    finally:
        sleep(20)
        if drv is not None:
            drv.quit()

    return nodeId+": finish FUTURE"

def clicker(drv, nodeId, pos):
    try:
        # sleep(random.randint(1, ))
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

            sm = 0
            smmin = float(offerMinimalStep.text.replace(",", "").replace(" ", ""))

            if offerMaximalStep is not None:
                smmax = round(float(offerMaximalStep.text.replace(",", "").replace(" ", "")))
                if smmin == smmax:
                    sm = smmin
                else:
                    sm = smmin + round(smmax - smmin) - 1
                    if sm < smmin: sm = smmin

                offerEditInput.send_keys(str(sm).replace(",", "").replace(" ", ""))
            else:
                sm = smmin
                offerMinimalStep.click()

            changeRate.click()

            try:
                WebDriverWait(drv, 0.1).until(
                    expected_conditions.invisibility_of_element_located((By.ID, "toast-container")))
            except:
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

            print(nodeId + ": changeRate  " + str(sm), datetime.now().isoformat())
    except Exception as e:
        print(nodeId + ": " + e.__str__())


if __name__ == "__main__":
    run_remote()

