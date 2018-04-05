
import time

from selenium import webdriver

from Prozorro.Pages.LoginPage import LoginPage

drv = webdriver.Remote(
            command_executor = 'http://192.168.56.1:4444/wd/hub',
            desired_capabilities = {
                'browserName': 'chrome',
                'javascriptEnabled': True
                })
drv.maximize_window()
drv.implicitly_wait(5)
drv.get("https://test-gov.ald.in.ua")
time.sleep(10)
LoginPage(drv).login("mm@mm.mm", "123123")
time.sleep(2000)
drv.close()



