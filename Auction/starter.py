import subprocess
from subprocess import Popen, run
from time import sleep

from Auction.run_prepare import prepare_data

count = 33
id = prepare_data(count)

completed =[]

for i in range(count):
    completed.append(Popen(["python", "C:\\Users\\dev2\\PycharmProjects\\AladdinTesting\\Auction\\run.py ", id],  stdout=subprocess.PIPE))


completed[0].wait(5000)

for i in completed:
    outs, errs = i.communicate()
    print(outs)
    print(errs)