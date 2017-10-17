import datetime
import dateutil.parser
import json
from Prozorro.Utils import get_root
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import pytz as pytz
import requests

def below(tender):
    tender_id = tender["tenderID"]
    if tender["procurementMethodType"] == "belowThreshold":
        return tender_id
        #if tender["awards"][0]["status"]:
         #   if tender["awards"]["status"] == "active":
          #      return tender_id


#def canceled_award(tender):
    #tender_id = tender["tenderID"]
    #aw_status = tender.awards["status"]
    #if tender == aw_status["active"]:
     #   return tender_id



    #awards = tender["awards"]
    #if awards["status"] == "active":
     #   return tender_id

def get_tendering_id(guid):
    turl = 'https://lb.api-sandbox.openprocurement.org/api/2.3/tenders/{0}'
    rq = requests.get(
        turl.format(guid)
    )
    tender_data = rq.json()["data"]
    #if "awards" in tender_data:
     #   awards=tender_data["awards"]
      #  if len(awards)>0:
       #     award = awards[0]
        #    if award["status"]=="active":
         #       return tender_data["tenderID"]
    if "owner" in tender_data:
        own=tender_data["owner"]
        ald='ald.in.ua'
        if own==ald:
            return tender_data["tenderID"]




    # if tender["status"] == "active.tendering" and "features" in tender and len(tender["features"])>1:
    #     endDate = dateutil.parser.parse(tender["tenderPeriod"]["endDate"])
    #     diff = endDate - datetime.datetime.now(tz=pytz.utc)
    #     minutes = diff // datetime.timedelta(seconds=60)
    #     if minutes >= 200:
    #         return tender["tenderID"]




if __name__ == '__main__':

    list_id = []
    next_page = 'https://lb.api-sandbox.openprocurement.org/api/2.3/tenders?descending=1'


    for count in range(5):
        http_t_list = requests.get(next_page)
        t_list = http_t_list.json()
        print(t_list["next_page"]["uri"])
        next_page = t_list["next_page"]["uri"]

        for tender in t_list["data"]:
            list_id.append(tender["id"])

    guid_list = []
    ex = ProcessPoolExecutor(max_workers=20)
    results = ex.map(get_tendering_id, list_id)

    for g in results:
        if g!=None:
            guid_list.append(g)
            print(g)
