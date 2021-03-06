#!/usr/bin/python3 -u

import getopt
import sys
import time

from Prozorro.Procedures.Filters import testFilters
from Prozorro.Procedures.Registration import registerUserCompany
from Prozorro.Procedures.Tenders import *


def list_params():
    return "-n [below,openua,openeu, concurenrUA]  - создать тендер \n" \
           "-o [uaid or guid]         - открыть просмотр \n" \
           "-e [uaid or guid]         - открыть на редактирование\n" \
           "-b [uaid or guid]         - подать бид\n"\
           "-R                        - регистрация пользователя\n"

def check(args):

    try:
        opts, arg = getopt.getopt(args, "n:o:e:b:r")
    except getopt.GetoptError as ff:
        print(str(ff))
        list_params()
        sys.exit(2)


    for opt, arg in opts:
        if opt == '-n':

            #       0   1   2  3  4  5
            # arg below:N1:L0:I1:F0:D0:T1
            arg = str(arg).split(":")
            proc = arg[0]
            _countTenders = 1
            _countLots = 0
            _countItems = 1
            _countFeatures = 0
            _countDocs = 0
            _test_mode = True

            for k in arg[1:]:
                if k[0] == "N":
                    _countTenders = int(k[1:])
                elif k[0] == "L":
                    _countLots = int(k[1:])
                elif k[0] == "I":
                    _countItems = int(k[1:])
                elif k[0] == "F":
                    _countFeatures = int(k[1:])
                elif k[0] == "D":
                    _countDocs = int(k[1:])
                elif k[0] == "T":
                    _test_mode = int(k[1:])==1

            print("""new tender {0}  countTenders = {1}
                  countLots = {2}
                  countItems = {3}
                  countFeatures = {4}
                  countDocs = {5} 
                  testMode={6} """.format(proc,_countTenders, _countLots,
                                          _countItems, _countFeatures, _countDocs,
                                          _test_mode))
            if proc=='below':
                print(datetime.datetime.now())
                uaids=create_below(countTenders=_countTenders,
                                   countLots=_countLots,
                                   countItems= _countItems,
                                   countFeatures= _countFeatures,
                                   countDocs= _countDocs,
                                   tender_dict=True,
                                   ttest_mode= _test_mode
                                 )

                sys.exit()
            elif proc == 'openUA':
                print(datetime.datetime.now())
                uaids = create_openUA(countTenders=_countTenders,
                                           countLots=_countLots,
                                           countItems=_countItems,
                                           countFeatures=_countFeatures,
                                           countDocs=_countDocs,
                                           test_mode=_test_mode
                                           )
                print(datetime.datetime.now())
                sys.exit()

            elif proc == 'openEU':
                print(datetime.datetime.now())
                uaids = create_openEU(countTenders=_countTenders,
                                           countLots=_countLots,
                                           countItems=_countItems,
                                           countFeatures=_countFeatures,
                                           countDocs=_countDocs,
                                           test_mode=_test_mode
                                           )
                print(datetime.datetime.now())
                sys.exit()


            elif proc == 'concurentUA':
                print(datetime.datetime.now())
                uaids = create_concurentUA(countTenders=_countTenders,
                                           countLots=_countLots,
                                           countItems=_countItems,
                                           countFeatures=_countFeatures,
                                           countDocs=_countDocs,
                                           tender_dict=1,
                                           test_mode=_test_mode
                                           )

                with(
                        open(Utils.get_root()+ '\\ConcurentUA_ids.json', 'w', encoding="UTF-8")) as uaid_file:
                    json.dump(uaids, uaid_file)
                print(datetime.datetime.now())
                sys.exit()
                pass


            elif proc == 'concurentEU':
                print(datetime.datetime.now())
                uaids = create_concurentEU(countTenders=_countTenders,
                                           countLots=_countLots,
                                           countItems=_countItems,
                                           countFeatures=_countFeatures,
                                           countDocs=_countDocs,
                                           tender_dict=1,
                                           test_mode=_test_mode
                                           )

                with(
                        open(Utils.get_root()+ '\\ConcurentUA_ids.json', 'w', encoding="UTF-8")) as uaid_file:
                    json.dump(uaids, uaid_file)
                print(datetime.datetime.now())
                sys.exit()


            elif proc == 'openeu':
                pass
            sys.exit()
        elif opt == '-o':
            print("view tender " + arg)

            if(arg!=None and len(arg)>12 and arg.startswith("UA")):
                open_tender(arg)
                time.sleep(20)
            else:
                print("Неправильный номер тендера ЮАИД")
        elif opt == '-e':
            print("edit tender " + arg)
            sys.exit()
        elif opt == '-b':
            print("add bid " + arg)
            args = arg.split(":")
            proc = args[0]
            id = args[1]
            create_bid(proc, id)

        elif opt == '-r':
            print("registartion " + arg)
            start = datetime.datetime.now()
            filename = 'UserAdded_v2.json'
            print(start)
            registerUserCompany(filename)

            # with(open(os.path.dirname(os.path.abspath(__file__)) + '\\uaids.json', 'w', encoding="UTF-8")) as uaid_file:
            #     json.dump(uaids, uaid_file)
            print(datetime.datetime.now(),  (datetime.datetime.now() - start).total_seconds())
            sys.exit()
        elif opt == '-F':
            print("filters " + arg)
            start = datetime.datetime.now()
            print(start)
            testFilters()
            print(datetime.datetime.now(),  (datetime.datetime.now() - start).total_seconds())
            sys.exit()






