import json

import os
from selenium import webdriver
from Prozorro.Pages.MainPage import MainPage
from Prozorro import Utils



def init_driver():
    with open(os.path.dirname(os.path.abspath(__file__))+'\\..\\test_params.json', 'r', encoding="UTF-8") as test_params_file:
       tp = json.load(test_params_file)
    chrm = webdriver.Chrome()
    chrm.implicitly_wait(10)
    chrm.get(tp["main"]["url"])
    return chrm, tp, MainPage(chrm)


def create_below(countLots, countFeatures, countDocs=0, countTenders=1, countItems=1, tender_dict=None):
    chrm, tp,mpg = init_driver()
    mpg.open_login_form().login(tp["below"]["login"], tp["below"]["password"]);
    uaid = []
    for i in range(countTenders):
        uaid.append(mpg.create_tender(procurementMethodType="belowThreshold", lots=0, items=1, docs=0, features=0))
    return uaid


def create_bids(uaids=[],fin=None):
    chrm, tp,mpg = init_driver()
    mpg.open_login_form().login(tp["bids"]["login"], tp["bids"]["password"])
    bid_uaids=[]

    if(os.path.isfile(fin)):
        with open(fin, 'r', encoding="UTF-8") as bids_uid_file:
            uaids = json.load(bids_uid_file)

    for i in uaids:
        bid_uaids.append(mpg.create_bid(i))

    return bid_uaids



def open_tender(id,role):
    chrm,tp, mpg=init_driver()
    if str(role) in Utils.roles and role=="provider":
        mpg.open_login_form().login(tp["bids"]["login"], tp["bids"]["password"])

    mpg.open_tender(id)

