import uuid
from datetime import datetime, timedelta

import requests

from Aladdin.Accounting.AladdinUtils import  MdbUtils

mdb = MdbUtils()
test_auction = {"_id":"",
                "date_start": "",
                "owner_url":"",
                "parts":[]
                }

def prepare_data(part_count=3):
    response = requests.get("http://192.168.95.164:27010/api/Auction/test",
                            params={"participantCount":part_count,
                                    "startSeconds":20,
                                    "auctionTime":2,
                                    "additionalStepLimit":3,
                                    "additionalStepTime":2
                                     #,"prodJson":"true" ns.antitheft.module
                                    },
                            headers ={"Authorization":"Basic U21hcnRGb3Jlc3RTeW5jOjhCMzk0RDkwLTRGNTAtNEY1Ri1BQTg4LTJFNjUyOTk5QUYzMA=="})
    test_a = response.json()
    parts = test_a["invitedCompanies"]

    for p in parts:
        print("PARTI - "+ p["suppUrl"])
        test_auction["parts"].append({"used":False, "url":p["suppUrl"]})

    test_auction["_id"] = uuid.uuid4().__str__()
    test_auction["owner_url"] = test_a["lots"][0]["ownerUrl"]

    test_auction["date_start"] = datetime.now() + timedelta(minutes = 3)

    mdb.test_auction.insert(test_auction)

    print("OWNER - " + test_auction["owner_url"])

    return(test_auction["_id"])

if __name__ == "__main__":
    prepare_data()