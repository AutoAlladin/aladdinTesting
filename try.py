import json
import time

import os

import requests
from copy import deepcopy

from Prozorro import Utils
from Prozorro.Procedures.Registration import registerUserCompany
from Prozorro.Procedures.Tenders import init_driver
import xmltodict



def try_driver():
    a,b,mpg = init_driver(False)
    Utils.waitFadeIn(mpg.drv)
    lf = mpg.open_login_form()
    lf.login("mm@mm.mm", "123123")
    time.sleep(2)
    mpg.drv.execute_script("$('#butLogoutPartial').click()")

def get_by_edr(_edr=""):
    ald_regions = {
        'Крим ': 'Автономна Республіка Крим',
        'Вінницька обл.': 'Вінницька',
        'Волинська обл.': 'Волинська',
        'Дніпропетровська обл.': 'Дніпропетровська',
        'Донецька обл.': 'Донецька',
        'Житомирська обл.': 'Житомирська',
        'Закарпатська обл.': 'Закарпатська',
        'Запорізька обл.': 'Запорізька',
        'Івано-Франківська обл.': 'Івано-Франківська',
        'Київська обл.': 'Київська',
        'Кіровоградська обл.': 'Кіровоградська',
        'Луганська обл.': 'Луганська',
        'Львівська обл.': 'Львівська',
        'Миколаївська обл.': 'Миколаївська',
        'Одеська обл.': 'Одеська',
        'Полтавська обл.': 'Полтавська',
        'Рівненська обл.': 'Рівненська',
        'Севастополь обл.': 'Севастополь',
        'Сумська обл.': 'Сумська',
        'Тернопільська обл.': 'Тернопільська',
        'Харківська обл.': 'Харківська',
        'Херсонська обл.': 'Херсонська',
        'Хмельницька обл.': 'Хмельницька',
        'Черкаська обл.': 'Черкаська',
        'Чернівецька обл.': 'Чернівецька',
        'Чернігівська обл.': 'Чернігівська'
    }


    edr = _edr.strip()
    rs = requests.get("https://docs.aps-tender.com/edr?id="+edr)
    if rs.text=="" and len(edr)<8 :
        edr = edr.rjust(8,"0")
        rs = requests.get("https://docs.aps-tender.com/edr?id=" + edr)

    if rs.text=="":
        raise  Exception("EDR {0} not found in https://docs.aps-tender.com".format(edr))

    dt = None
    try:
        dt = xmltodict.parse(rs.text.strip())
        dt = dt["RECORD"]
    except Exception as e:
        print("PARSE ERROR - "+rs.text+" - " +e.__str__())

    try:
        addr = ""+dt["ADDRESS"]
        tmps,s,rests = addr.partition(",")
        index = tmps.strip()

        tmps, s, rests = rests.partition(",")
        if tmps.strip() in ald_regions:
            region = ald_regions[ tmps.strip()]
        else:
            region = "Київська"
            print( tmps.strip() +"not in ald_regions")

        tmps, s, rests = rests.partition(",")
        raion = tmps.strip()

        tmps, s, rests = rests.partition(",")
        city =tmps.strip()
        addr = rests.strip()

        dt.update({"ADDRESS":{"index":index, "region":region, "city":city, "addr":addr, "raion":raion}})

    except Exception as e:
        print("PARSE ADDREES - "+str(dt)+" - " +e.__str__())

    return dt

def make_full_liac_json():
    cmp =[]
    liac_mail=[]
    liac ={ "Company":[]}
    with open(os.path.dirname(os.path.abspath(__file__)) + '\\Prozorro\\CompanyUsers.json', 'r',
              encoding="UTF-8") as company_file:
        cmp = json.load(company_file)

    with open(os.path.dirname(os.path.abspath(__file__)) + '\\Prozorro\\liac_companies.json', 'r',
              encoding="UTF-8") as company_file:
        liac_mail = json.load(company_file)

    for lic in liac_mail:
        if lic["c_email"] == "":
            print("Нету почты", str(lic))
            continue

        if lic["c_email"].startswith("no@mail"):
            print("Фейковая почта", str(lic))
            continue

        if lic["c_edrpou"] == "":
            print("Нету EDRPOU", str(lic))
            continue

        tc = dict(cmp["Company"][0])
        tc["subj_ident_code"] = lic["c_edrpou"].strip()
        tc["subj_legal_name"] = lic["c_name"].strip()
        tc["subj_email"] = lic["c_email"].strip()
        tc["addr_region"] = "Київська"
        tc["company_role"] = "owner"
        tc["Users"][0]["login"] = lic["c_email"]

        try:
            attr = get_by_edr(lic["c_edrpou"])
            if attr is not None:
                tc["subj_ident_code"] = attr["EDRPOU"].strip()
                tc["subj_short_name"] = attr["SHORT_NAME"]
                tc["subj_legal_name"] =  attr["NAME"]
                tc["addr_street"] = attr["ADDRESS"]["addr"]
                tc["addr_locality"] = attr["ADDRESS"]["city"]
                tc["addr_region"] = attr["ADDRESS"]["region"]
                tc["addr_post_code"] = attr["ADDRESS"]["index"]
        except Exception as e:
            print(e.__str__())
            continue

        liac["Company"].append(deepcopy(tc))

    with open(os.path.dirname(os.path.abspath(__file__)) + '\\Prozorro\\liac.json', 'w',encoding='utf-8') as outfile:
        json.dump(liac, outfile,  indent=4, sort_keys=True, ensure_ascii=False)



if __name__ =="__main__":
    #make_full_liac_json()
    registerUserCompany(os.path.dirname(os.path.abspath(__file__)) + '\\Prozorro\\liac.json',
                        testMode=False)
