import logging

# create logger
from operator import itemgetter

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger('try')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug

ch = logging.FileHandler("try.log")
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('[%(asctime)s-%(name)s-%(levelname)s]: %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)



import time

from selenium import webdriver

from Prozorro.Pages.LoginPage import LoginPage

drv = webdriver.Chrome()
drv.maximize_window()
drv.implicitly_wait(5)
drv.get("https://novaposhta.ua/ru")

input_for_nom_nakladnoi = drv.find_element_by_id("cargo_number")
input_for_nom_nakladnoi.send_keys("10029844700")
input_for_nom_nakladnoi.send_keys(Keys.ENTER)

time.sleep(100)

drv.quit()


