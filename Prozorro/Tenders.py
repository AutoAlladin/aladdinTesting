import json

import os
from selenium import webdriver
from Prozorro.Pages.MainPage import MainPage


def init_driver():
    with open(os.path.dirname(os.path.abspath(__file__))+'\\test_params.json', 'r', encoding="UTF-8") as test_params_file:
       tp = json.load(test_params_file)
    chrm = webdriver.Chrome()
    chrm.implicitly_wait(10)
    chrm.get(tp["main"]["url"])
    return chrm, tp, MainPage(chrm)


def create_below(countLots, countFeatures, countDocs=0, countTenders=1, countItems=1, tender_dict=None):
    chrm, tp,mpg = init_driver()
    mpg.open_login_form().login(tp["below"]["login"], tp["below"]["password"]);
    return mpg.create_tender(procurementMethodType="belowThreshold", lots=0, items=1, docs=0, features=0)


def open_tender(id):
    chrm,tp, mpg=init_driver()
    mpg.open_login_form().login(tp["bids"]["login"], tp["bids"]["password"]);
    mpg.open_tender(id)

