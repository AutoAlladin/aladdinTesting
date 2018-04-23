import concurrent
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from Auction.run import run_remote

from Auction.run_prepare import prepare_data

count = 62
id = prepare_data(count)
auction_futures =[]

def run_remote_test():
    #proc = Popen(["python", "C:\\Users\\dev2\\PycharmProjects\\AladdinTesting\\Auction\\run.py ", id], stdout=subprocess.PIPE)
    #c = proc.wait()
    #return  str(proc.communicate())
    r =  run_remote(_id=id)
    return  r


with ThreadPoolExecutor(max_workers=count, thread_name_prefix="auction_") as executor:
    auction_futures= { executor.submit(run_remote_test): i for i in range(count)}
    for f in concurrent.futures.as_completed(auction_futures):
         print(f.result())


