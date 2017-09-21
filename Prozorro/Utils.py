import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

roles=["owner", "provider", "viewer"]

def paint(drv, name):
    drv.get_screenshot_as_file(os.path.dirname(os.path.abspath(__file__)+"\\output\\"+name))

def set_datepicker(drv, ID, value):
    drv.execute_script("SetDateTimePickerValue(\'"+ID+"\',\'"+value+"\')")


def waitFadeIn(drv):
    WebDriverWait(drv, 20).until( EC.invisibility_of_element_located ((By.XPATH, "//div[@class='page-loader animated fadeIn']")))


def waitNotifyToast(drv):
    try:
        close_toast = WebDriverWait(drv, 2).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='toast-close-button']")))
        waitFadeIn(drv)
        close_toast.click()
    except Exception  as e:
        pass #print("toast-close not found")

def get_dic_val(dic, _key):
    key = _key.split(".")
    return dic[key[0]][key[1]]

