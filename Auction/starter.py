import concurrent
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from datetime import datetime, timedelta

from Aladdin.Accounting.AladdinUtils import MdbUtils
from Auction.run import run_remote

from Auction.run_prepare import prepare_data

#count = 3
# если указать ИД то даные берутся сразу из БД - сейчас это логика - 1 участник по всем позициям одновременно

id = prepare_data(5)
#id = "580"
#id = "580_next"
auction_futures =[]
urls=[]

mdb = MdbUtils()
test_a = mdb.test_auction.find_one({"_id":id})



parts = []
for t in test_a["parts"]:
    parts.append({"part":t,
                  "stepCount": 1,
                  "time_start": datetime.now() + timedelta(seconds=15)
                  })


count = len(parts)

# если position_id  1 число -*  то его,  если массив - то все из массива,  сли не указано - все позиции
#stepCount  - количество повторов
#part - берем из БД


with ThreadPoolExecutor(max_workers=count, thread_name_prefix="auction_") as executor:
    auction_futures= {
        executor.map(run_remote, parts)}
    # for f in concurrent.futures.as_completed(auction_futures):
    #      print(f.result())


