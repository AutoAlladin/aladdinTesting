import json
import requests
from selenium import webdriver
import webbrowser
from selenium.webdriver.common.keys import Keys
import unittest

#from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from Auction.AuctionRegistration import *
from Auction.add_participant import *

class RegistrationAuction(unittest.TestCase):

    def __init__(self):
        tp = None
        with open("par", 'r', encoding="UTF-8") as params_file:
            tp = json.load(params_file)
            # print(tp)

    def get_ar(self, tp):


        #print(tp)

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
            ar.add_position(pos["minimalStep"], pos["maximalStep"], pos_labels, idd=None)

        return ar


    def test_01_Registration_auction(self):
        data_reg = jsonpickle.encode(self.get_ar(), unpicklable=False)
        req_reg = requests.post("http://192.168."
                                "95.153:27177/api/manager/register", data=data_reg, headers={"content-type": "application/json"})
        print(req_reg.status_code)

        #id аукциона
        resp = req_reg.json()
        ID = resp['id']
        self.assertEqual(req_reg.status_code, 200)
# #id позиции
# id_item_1 = resp['positions'][0]['id']
# id_item_2 = resp['positions'][1]['id']
# id_item_3 = resp['positions'][2]['id']



    def test_02_Registration_participants(self, resp, tp, ID):
        i = 0
        arates=[]
        for pos in resp["positions"]:
            item_id = pos['id']
            r = AuctionRate(item_id, tp["positions"][i]["rate"])
            arates.append(r)
            i += 1


        get_token = resp["token"]

        ap = [AuctionParticipent(
                name="Jack Sparrow",
                email="jack@mail.com",
                rates=arates),
              AuctionParticipent(
                name="Тест Тестович",
                email="testyaka@mail.ru",
                rates=arates),
              AuctionParticipent(
                name="Ozzy Osborn",
                email="ozzyos@mail.com",
                rates=arates)
            ]

        data_reg = jsonpickle.encode(ap, unpicklable=False)



        req_add_part = requests.post("http://192.168.95.153:27177/api/manager/auction/"+ID+"/participants",
                                     data=data_reg, headers={"content-type": "application/json"})

        print(req_add_part.status_code)

        resp_partic = req_add_part.json()

        #key_particioant = str(resp_partic[0]["key"])




    def test_03_Open_page(self, ID, resp_partic, get_token):
        dom = "http://192.168.95.153:27178/#/auction/"
        dr = webdriver.Chrome()

        url_owner = dom+ID+"?key="+get_token
        dr.get(url_owner)



        for k in resp_partic:
            key = k["key"]
            print(key)
            prov = dom + ID + "?key=" + key
            print(prov)
            op_window = "window.open('{0}', '_blank');".format(prov)
            dr.execute_script(op_window)



    #if __name__ == "__main__":







#dr.get(dom+ID)



# body = dr.find_element_by_tag_name("html")
# body.send_keys(Keys.CONTROL+'T')

# dr.get(dom+ID+"?key="+get_token)
#print(dr.window_handles[0])

# body = dr.find_element_by_tag_name("body")
# body.send_keys(Keys.CONTROL, 't')





#dr.close()



