import json
import requests

from Auction.AuctionRegistration import *
from Auction.add_participant import *

tp=None
with open("par", 'r', encoding="UTF-8") as params_file:
    tp = json.load(params_file)

print(tp)

au_labels = [Label_UA_Title("auction ua title"),
             Label_UA_Description("auction ua label description"),
             Label_EN_Title("auction en label title"),
             Label_EN_Description("auction en label description"),
             ]

pos_labels = [Label_UA_Title("position ua title"),
              Label_UA_Description("position ua label description"),
              Label_EN_Title("position en label title"),
              Label_EN_Description("position en label description"),
              ]

ar = AuctionRegistration(
    type="SmartClose",
    reverse=True,
    budget=10000,
    currency="UAH",
    dateStart=datetime.strptime(tp["dateStart"], '%Y-%m-%dT%H:%M:%S%z'),
    dateEnd=datetime.strptime(tp["dateEnd"], '%Y-%m-%dT%H:%M:%S%z'),
    additionalStepTime=tp["additionalStepTime"],
    additionalStepLimit=tp["additionalStepLimit"],
    labels=au_labels,
    positions=[],
    ownerEmail="owner@mail.com"

)

for pos in tp["positions"]:
    ar.add_position(pos["minimalStep"], pos["maximalStep"], pos_labels, idd)

print(jsonpickle.encode(ar, unpicklable=False))

data_reg = jsonpickle.encode(ar, unpicklable=False)

req_reg =None

req_reg = requests.post("http://192.168."
                        "95.153:27177/api/manager/register", data=data_reg, headers={"content-type": "application/json"})

print(req_reg.json())

print((tp["positions"][0]["rate"]))

arates=[]

# arates.append(AuctionRate('sdfgsdfg-45g65sd4fg64dg-dfgd',tp["positions"][0]["rate"]))
# arates.append(AuctionRate('sdfgsdfg-45g65sd4fg64dg-dfgd',tp["positions"][1]["rate"]))
# arates.append(AuctionRate('sdfgsdfg-45g65sd4fg64dg-dfgd',tp["positions"][2]["rate"]))

for p in tp["positions"]:
    arates.append(AuctionRate('yfiufihgfihgfgy',p["rate"]))

add_participant = AuctionParticipent(
    name="Jack Sparrow",
    email="jack@mail.com",
    rates=arates)

print(jsonpickle.encode(add_participant, unpicklable=False))




