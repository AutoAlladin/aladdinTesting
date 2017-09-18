import datetime
import getopt
import sys
import time

from Prozorro.Procedures.Tenders import *


def list_params():
    return "-n [below,openua,openeu]  - создать тендер \n" \
           "-o [uaid or guid]         - открыть просмотр \n" \
           "-e [uaid or guid]         - открыть на редактирование\n" \
           "-b [uaid or guid]         - подать бид\n"

def check(args):

    try:
        opts, arg = getopt.getopt(args, "n:o:e:b:")
    except getopt.GetoptError:
        list_params()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-n':

            #       0   1   2  3  4  5
            # arg below:N1:L0:I1:F0:D0
            arg = str(arg).split(":")
            proc = arg[0]
            _countTenders = 1
            _countLots = 0
            _countItems = 1
            _countFeatures = 0
            _countDocs = 0

            if len(arg) >= 2:
                _countTenders = int(arg[1][1:])
            if len(arg) >= 3:
                _countLots = int(arg[2][1:])
            if len(arg) >= 4:
                _countItems = int(arg[3][1:])

            print("""new tender {0}  countTenders = {1}
                  countLots = {2}
                  countItems = {3}
                  countFeatures = {4}
                  countDocs = {5} """.format(proc,_countTenders, _countLots, _countItems, _countFeatures, _countDocs))
            if proc=='below':
                print(datetime.datetime.now())
                uaids=create_below(countTenders=_countTenders,
                                   countLots =_countLots,
                                   countItems = _countItems,
                                   countFeatures = _countFeatures,
                                   countDocs = _countDocs
                                 )

                with(open(os.path.dirname(os.path.abspath(__file__))+'\\uaids.json', 'w', encoding="UTF-8")) as uaid_file:
                    json.dump(uaids, uaid_file)
                print(datetime.datetime.now())
                sys.exit()
            elif arg=='openua':
                pass
            elif arg=='openeu':
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
            if arg == "add_one":
                create_bids(arg)
            elif arg == "add_many":
                print(create_bids(fin=os.path.dirname(os.path.abspath(__file__))+'\\uaids.json'))
            sys.exit()





































