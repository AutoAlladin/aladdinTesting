import getopt
import sys
import time

from Prozorro.Procedures.Registration import registerUserCompany
from Prozorro.Procedures.Tenders import *


def list_params():
    return "-n [below,openua,openeu, concurenrUA]  - создать тендер \n" \
           "-o [uaid or guid]         - открыть просмотр \n" \
           "-e [uaid or guid]         - открыть на редактирование\n" \
           "-b [uaid or guid]         - подать бид\n"\
           "-R [uaid or guid]         - регистрация пользователя\n" \

def check(args):

    try:
        opts, arg = getopt.getopt(args, "n:o:e:b:R")
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
                                   countDocs = _countDocs,
                                   tender_dict=True
                                 )

                with(open(os.path.dirname(os.path.abspath(__file__))+'\\uaids.json', 'w', encoding="UTF-8")) as uaid_file:
                    json.dump(uaids, uaid_file)
                print(datetime.datetime.now())
                sys.exit()
            elif proc == 'openUA':
                print(datetime.datetime.now())
                uaids = create_openUA(countTenders=_countTenders,
                                           countLots=_countLots,
                                           countItems=_countItems,
                                           countFeatures=_countFeatures,
                                           countDocs=_countDocs,
                                           tender_dict=1
                                           )
                with(open(Utils.get_root() + '\\uaids.json', 'w', encoding="UTF-8")) as uaid_file:
                    json.dump(uaids, uaid_file)
                print(datetime.datetime.now())
                sys.exit()
            elif proc == 'concurentUA':
                print(datetime.datetime.now())
                uaids = create_concurentUA(countTenders=_countTenders,
                                           countLots=_countLots,
                                           countItems=_countItems,
                                           countFeatures=_countFeatures,
                                           countDocs=_countDocs,
                                           tender_dict=1
                                           )

                with(
                        open(Utils.get_root()+ '\\ConcurentUA_ids.json', 'w', encoding="UTF-8")) as uaid_file:
                    json.dump(uaids, uaid_file)
                print(datetime.datetime.now())
                sys.exit()
                pass
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
            if arg == "add_one":
                create_bids(arg)
                sys.exit()
            elif arg == "add_many":
                print(create_bids(fin=os.path.dirname(os.path.abspath(__file__))+'\\uaids.json',prepare=1))
            elif arg == "on_time":
                print(send_bids(fin=os.path.dirname(os.path.abspath(__file__))+'\\uaids.json',prepare=0))
        elif opt == '-R':
            print("registartion " + arg)
            start = datetime.datetime.now()
            filename = 'CompanyUsers.json'
            print(start)
            registerUserCompany(filename)

            # with(open(os.path.dirname(os.path.abspath(__file__)) + '\\uaids.json', 'w', encoding="UTF-8")) as uaid_file:
            #     json.dump(uaids, uaid_file)
            print(datetime.datetime.now(),  (datetime.datetime.now() - start).total_seconds())
            sys.exit()






































