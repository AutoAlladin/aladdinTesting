import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import uuid
import prozorro

run_guid = str(uuid.uuid1())
roles={"owner", "provider", "viewer"}


def get_root():
    return os.path.dirname(os.path.abspath( prozorro.__file__ ));

def paint(drv, name):
    dir = get_root()
    dir = dir+"\\Prozorro\\output\\"+name
    drv.get_screenshot_as_file(dir)

def scroll_to_element(drv, element,delta="105"):
    drv.execute_script("window.scroll(0, {0}-{1})".format(element.location.get("y"),delta))

def set_datepicker(drv, ID, value):
    drv.execute_script("SetDateTimePickerValue(\'"+ID+"\',\'"+value+"\')")


def waitFadeIn(drv):
    try:
        WebDriverWait(drv, 20).until( EC.invisibility_of_element_located ((By.XPATH, "//div[@class='page-loader animated fadeIn']")))
    except:
        pass


def waitNotifyToast(drv):
    try:
        if not WebDriverWait(drv, 2).until( EC.invisibility_of_element_located ((By.XPATH, "//div[@class='page-loader animated fadeIn']"))):
            close_toast =drv.find_element_by_xpath("//button[@class='toast-close-button']")
            waitFadeIn(drv)
            close_toast.click()
    except Exception  as e:
        pass #print("toast-close not found")

def get_dic_val(dic, _key, default = None):


    key = _key.split(".")

    if _key=="below.description" or _key == "below.title":
        return dic[key[0]][key[1]]+" - "+run_guid
    else:
        if key[0] not in dic :
            return default
        elif key[1] not in dic[key[0]] :
            return default
        else:
            return dic[key[0]][key[1]]

