import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Prozorro.Procedures.Tenders import init_driver
from Prozorro.Utils import waitFadeIn


def myTenders(drv):
    WebDriverWait(drv, 15).until(
        expected_conditions.
            visibility_of_element_located(
            (By.XPATH, "//div[@href='#myTendersList']")
        )
    )

    filter_root= drv.find_element_by_xpath("//div[@href='#myTendersList']")
    #filter_root.click()

    butSimpleSearch = drv.find_element_by_id('butSimpleSearch')
    butClearFilterMy= drv.find_element_by_id('butClearFilterMy')

    waitFadeIn(drv)
    butClearFilterMy.click()
    isFavorites = drv.find_element_by_xpath("//label[@for='isFavorites']")
    isFavorites.click()
    butSimpleSearch.click()
    waitFadeIn(drv)
    tendersList = drv.find_elements_by_xpath('//div[@id="purchase-page"]//h4')
    print('isFavorites',len(tendersList))

    waitFadeIn(drv)
    butClearFilterMy.click()
    time.sleep(1)
    isMyTender = drv.find_element_by_xpath("//label[@for='isMyTender']")
    isMyTender.click()
    butSimpleSearch.click()
    waitFadeIn(drv)
    tendersList = drv.find_elements_by_xpath('//div[@id="purchase-page"]//h4')
    print('isMyTender', len(tendersList))

    waitFadeIn(drv)
    butClearFilterMy.click()
    isVisited = drv.find_element_by_xpath("//label[@for='isVisited']")
    isVisited.click()
    butSimpleSearch.click()
    waitFadeIn(drv)
    tendersList = drv.find_elements_by_xpath('//div[@id="purchase-page"]//h4')
    print('isVisited', len(tendersList))


def testFilters():
    chrm, tp, mpg = init_driver()
    waitFadeIn(mpg.drv)
    mpg.open_login_form().login(tp["below"]["login"], tp["below"]["password"])

    myTenders(chrm)

    """
    МОЇ ТЕНДЕРИ
        обрані 
        мої 
        переглянуті
        
     ТИП  ПРОцедури
     purchaseType14 - еско
     purchaseType2 - відкриті
     purchaseType3 -  відкриті англ
     purchaseType1 - допорогові
     purchaseType4 - звіт
     purchaseType8 - конкурентний діалог
     purchaseType10 - конкурентний 2 єтап
     purchaseType9 - конкурентний англ
     purchaseType11  - конкурентний англ 2 єтап
     purchaseType - переговорна для потреб оборони
        
    """