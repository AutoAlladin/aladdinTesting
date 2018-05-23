import json

import os
import datetime
import time
import dateutil.parser

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Prozorro.Pages.MainPage import MainPage
from Prozorro import Utils




def init_driver(test_mode=True):
    file_name=""
    if test_mode :
        file_name = os.path.dirname(os.path.abspath(__file__))+'\\..\\test_params.json'
    else:
        file_name = os.path.dirname(os.path.abspath(__file__)) + '\\..\\prod_params.json'

    with open(file_name, 'r', encoding="UTF-8") as test_params_file:
       tp = json.load(test_params_file)

    chrm = webdriver.Chrome()

    chrm.maximize_window()
    chrm.implicitly_wait(5)
    chrm.get(tp["main"]["url"])
    return chrm, tp, MainPage(chrm)


def create_below(countLots=0,
                 countFeatures=0,
                 countDocs=0,
                 countTenders=1,
                 countItems=1,
                 tender_dict=True,
                 ttest_mode=True,
                 test_log=None):
    chrm, tp, mpg = init_driver(ttest_mode)
    if tender_dict is not None and isinstance(tender_dict, dict):
        tp = tender_dict

    mpg.open_login_form().login(tp["below"]["login"], tp["below"]["password"])

    uaid = []
    d = webdriver.Chrome
    dr = d.current_url
    #print(dr)

    args=dict(procurementMethodType='belowThreshold',
              lots=countLots,
              items=countItems,
              docs=countDocs,
              features=countFeatures,
              dic=tp,
              log = test_log
              )

    for i in range(countTenders):
            uaid.append(mpg.create_tender(**args,nom=str(i)))


    return uaid





def create_openUA(countLots, countFeatures, countDocs=0, countTenders=1, countItems=1, tender_dict=None):
    chrm, tp, mpg = init_driver()
    mpg.open_login_form().login(tp["below"]["login"], tp["below"]["password"])
    uaid = []

    args=dict(procurementMethodType='aboveThresholdUA',
              lots=countLots,
              items=countItems,
              docs=countDocs,
              features=countFeatures,
              dic=tp
              )
    for i in range(countTenders):
        uaid.append(mpg.create_tender(**args, nom=str(i)))

    return uaid

def create_bids(uaids=[],fin=None, prepare=0, test_mode=True):
    print("start bids", datetime.datetime.now())
    chrm, tp,mpg = init_driver(test_mode)
    mpg.open_login_form().login(tp["billing_ui"]["bids"]["login"], tp["billing_ui"]["bids"]["password"])
    bid_uaids=[]

    if(os.path.isfile(fin)):
        with open(fin, 'r', encoding="UTF-8") as bids_uid_file:
            uaids = json.load(bids_uid_file)


        for i in uaids:
            print(i)
            if prepare == 0:
                bid_uaids.append(mpg.create_bid(i[0],prepare))
            else:
                bid_uaids.append(mpg.create_bid(i[1],prepare))

    body =  mpg.drv.find_element_by_tag_name("html")
    body.send_keys(Keys.CONTROL+'2')
    time.sleep(6000)
    print("finish bids", datetime.datetime.now())
    return bid_uaids


def create_bid(link, test_mode=True):
    print("start bids", datetime.datetime.now())
    chrm, tp,mpg = init_driver(test_mode)
    mpg.open_login_form().login(tp["billing_ui"]["bids"]["login"], tp["billing_ui"]["bids"]["password"])
    bid_uaids=[]


    bid_uaids.append(mpg.create_bid(link, 1))


    print("finish bids", datetime.datetime.now())
    return bid_uaids

def open_tender(id,role, test_mode=True):
    chrm,tp, mpg=init_driver(test_mode)
    print("mpg.open_tender in open" + id)
    if str(role) in Utils.roles and role == "provider":
        mpg.open_login_form().login(tp["billing_ui"]["bids"]["login"], tp["billing_ui"]["bids"]["password"])

    mpg.open_tender(id)



def create_concurentUA(countLots, countFeatures, countDocs=0, countTenders=1, countItems=1, tender_dict=None):
    chrm, tp,mpg = init_driver()
    mpg.open_login_form().login(tp["below"]["login"], tp["below"]["password"]);
    uaid = []

    args = dict(procurementMethodType='concurentUA',
                lots=countLots,
                items=countItems,
                docs=countDocs,
                features=countFeatures,
                dic=tp
                )

    for i in range(countTenders):
        uaid.append(mpg.create_tender(*args, dic=tp))

    return uaid

def send_bids(uaids=[],fin=None, prepare=0):
    print("start bids", datetime.datetime.now())
    chrm, tp,mpg = init_driver()
    mpg.open_login_form().login(tp["bids"]["login"], tp["bids"]["password"])
    startTime=  dateutil.parser.parse(tp["bids"]["startTime"])

    bid_uaids=[]

    if(os.path.isfile(fin)):
        with open(fin, 'r', encoding="UTF-8") as bids_uid_file:
            uaids = json.load(bids_uid_file)


        while datetime.datetime.now()<startTime:
            time.sleep(1)
        print(datetime.datetime.now())
        for i in uaids:
            print(i)
            bid_uaids.append(mpg.create_bid(i[1],2))

    body =  mpg.drv.find_element_by_tag_name("html")
    body.send_keys(Keys.CONTROL+'2')
    print("finish bids", datetime.datetime.now())

    return bid_uaids