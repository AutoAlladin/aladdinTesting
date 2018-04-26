import logging

# create logger
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



#import time
#
# from selenium import webdriver
#
# from Prozorro.Pages.LoginPage import LoginPage
#
# drv = webdriver.Remote(
#             command_executor = 'http://192.168.56.1:4444/wd/hub',
#             desired_capabilities = {
#                 'browserName': 'chrome',
#                 'javascriptEnabled': True
#                 })
# drv.maximize_window()
# drv.implicitly_wait(5)
# drv.get("https://test-gov.ald.in.ua")
# time.sleep(10)
# LoginPage(drv).login("mm@mm.mm", "123123")
# time.sleep(2000)
# drv.close()
import random



def r(x):
    w = ""
    for i in range(random.randint(3, 7)):
        w = w + x
    return {"id":x, "tree":w}

#tree = [ r(li) for li in "abcde" ]


tree = map(r,"sdfsdfs")
print(list(tree))

