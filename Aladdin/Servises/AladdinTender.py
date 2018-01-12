from datetime import datetime

import requests
import pyodbc

from Aladdin.DB.db import get_connection

conn_aladdin_test={
    '_server': '192.168.80.90',
    '_database': 'AladdinTender',
    '_username': 'sergey',
    '_password': 'SEGAmega22051989',
    '_driver': '{ODBC Driver 13 for SQL Server}'
}


service_url = "http://192.168.80.169:130/api/tender/gettenderbyid/{0}"


def get_db_data(tender_id):
    mssql_connection = get_connection(**conn_aladdin_test)
    crs = mssql_connection.cursor()
    sql="{CALL Tender_GetById(?)}"

    params = (7)
    crs.execute(sql, params)

    rows = crs.fetchall()
    return rows

def get_api_data(tender_id):
    rq = requests.get(service_url.format(tender_id))
    return rq.json()


def compare_date(db_value,api_value, msg):
    d_string,v= "", ""
    if db_value==None:
        v='none'
    else:
        v = datetime.strftime(db_value, '%Y-%m-%dT%H:%M:%S.%f %z')
        d_string, tz_string = v.rsplit(' ', 1)
        v = d_string + tz_string[:-2] + ":" + tz_string[-2:]

    if api_value[msg]==None:
        d_string ="none"
    else:
        d_string, tz_string = api_value[msg].rsplit('+', 1)
        d_string = d_string[:-1] + "+" + tz_string

    if d_string == v:
        print(msg+" OK", v)
    else:
        print(msg+" FAIL", api_value, v)


if __name__ =="__main__":
    api =  get_api_data(7)
    dt = get_db_data(7)[0]

    v=dt.Id
    if api["id"] ==v : print("id OK",v)
    else:  print("id FAIL ", api["id"],v)

    v=dt.Guid
    if api["guid"] == dt.Guid: print("guid OK", v)
    else:  print("guid FAIL", api["id"],v)

    v=dt.AladdinId
    if api["aladdinId"] == v: print("aladdinId OK", v)
    else:  print("aladdinId FALL ", api["aladdinId"],v)

    v=dt.Status
    if api["status"] ==v : print("status OK", v)
    else:  print("status FAIL", api["status"],v)

    v=dt.Title
    if api["title"] == v: print("title OK", v)
    else:  print("title FAIL", api["title"],v)

    v=dt.Description
    if api["description"] ==v : print("description OK", v)
    else:  print("description FAIL", api["description"],v)

    v=dt.Budget
    if api["budget"] == v: print("budget OK", v)
    else:  print("budget FAIL", api["budget"],v)

    v=dt.Currency
    if api["currency"] ==v : print("currency OK", v)
    else:  print("currency FAIL", api["currency"],v)

    v=dt.IsVat
    if api["isVat"] ==v : print("isVat OK", v)
    else:  print("isVavt FAIL", api["isVat"],v)

    v=dt.IsMultiLot
    if api["isMultilot"] == v: print("isMultilot OK", v )
    else:  print("isMultilot FAIL", api["isMultilot"],v)

    v=dt.InfoCompany
    if api["infoCompany"] ==v : print("infoCompany OK", v)
    else:  print("infoCompany FAIL", api["infoCompany"],v)

    v=dt.ContactPerson
    if api["contactPerson"] ==v : print("contactPerson OK", v)
    else:  print("contactPerson FAIL", api["contactPerson"],v)

    v=dt.TenderType
    if api["tenderType"] ==v : print("tenderType OK", v)
    else:  print("tenderType FAIL", api["tenderType"],v)

    v=dt.AdditionalAttributes
    if api["additionalAttributes"] == v: print("additionalAttributes OK", v)
    else:  print("additionalAttributes FAIL", api["additionalAttributes"],v)

    v=dt.IsRemoved
    if api["isRemoved"] == v: print("isRemoved OK", v)
    else:  print("isRemoved FAIL", api["isRemoved"],v)

    v= dt.EndBid
    if api["endBid"] ==v: print("endBid OK",v)
    else:  print("endBid FAIL", api["endBid"],v)

    compare_date(dt.DateCreate,api,"dateCreate")
    compare_date(dt.DateModified, api, "dateModified")

    # "startTender"
    # v = dt.StartTender
    # if api["startTender"] == v:  print("startTender OK", v)
    # else:   print("startTender FAIL", api["startTender"], v)
    compare_date(dt.StartTender, api, "startTender")

    # "endTender"
    v = dt.EndTender
    if api["endTender"] == v:  print("endTender OK", v)
    else:   print("endTender FAIL", api["endTender"], v)

    # "startBid"
    v = dt.StartBid
    if api["startBid"] == v:  print("startBid OK", v)
    else:   print("startBid FAIL", api["startBid"], v)
