import datetime
import dateutil.parser
import json
from Prozorro.Utils import get_root
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import pytz as pytz
import requests


def get_tendering_id(guid):
    turl = 'https://lb.api-sandbox.openprocurement.org/api/2.3/tenders/{0}'
    tender = requests.get(turl.format(guid)).json()["data"]
    if tender["status"] == "active.tendering" and "features" in tender and len(tender["features"])>1:
        endDate = dateutil.parser.parse(tender["tenderPeriod"]["endDate"])
        diff = endDate - datetime.datetime.now(tz=pytz.utc)
        minutes = diff // datetime.timedelta(seconds=60)
        if minutes >= 200:
            return tender["tenderID"]


if __name__ == '__main__':

    list_id = []
    next_page = 'https://lb.api-sandbox.openprocurement.org/api/2.3/tenders?descending=1'

    for count in range(20):
        http_t_list = requests.get(next_page)
        t_list = http_t_list.json()
        print(t_list["next_page"]["uri"])
        next_page = t_list["next_page"]["uri"]

        for tender in t_list["data"]:
            list_id.append(tender["id"])

        http_t_list = requests.get(next_page)
        t_list = http_t_list.json()

    guid_list = []
    ex = ProcessPoolExecutor(max_workers=10)
    results = ex.map(get_tendering_id, list_id)

    for g in results:
        if g!=None:
            guid_list.append(g)
            print(g)
