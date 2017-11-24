import json
from concurrent.futures import ProcessPoolExecutor
import unittest
import requests
from decimal import Decimal

from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from Aladdin.DB.billing import get_db_reserve, get_db_balance


# service_fix_money     = "http://192.168.95.153:91/api/balance/WriteOffMoney"
# service_add_reserv    = "http://192.168.95.153:91/api/balance/reserve"
# service_cansel_reserv = "http://192.168.95.153:91/api/balance/CancelReserve"
# service_return_money = "http://192.168.95.153:91/api/balance/ReturnMonies"
#
# empty_acc="2F6D3BCD-8898-44EB-9C0D-9969E5776C66"
# full_acc  = "28DAE9EC-6D86-417C-AC22-46F73EC1EB44"
# full_acc1 = "FBF3CF0B-4226-4367-9A40-B4CB10C882F7"
#


# rezerv=dict(
#     TenderId = 700,                 # any
#     LotId =9,                       # any
#     Amount =789000.0,               # any
#     Currency = 'UAH',               # UAH only
#     Descriptions ="chupakabra",     # any
#     TotalMoney =100.0,              # сумма для снятия
#     CompanyUuid = full_acc          # company guid
#    # ServiceIdentifierUuid = None
#    )  # now it is Prozorro
#
# cansel_reserv = dict(
#     TenderId = rezerv["TenderId"],
#     LotId = rezerv["LotId"],
#     CompanyUuid = rezerv["CompanyUuid"]
# )
#
# fix_money = dict(
#     TenderId = 600,
#     #ServiceIdentifierUuid = 1  # Prozorro
#     SiteType= 1  # Prozorro
# )
#
#
# def rezerv_fix(rzv, runRserv=True, runCanselResrv=True, runReturn=True):
#
#
#     if runRserv:
#         try:
#             prev_amount_db = get_db_reserve(rzv["CompanyUuid"])
#
#             rq = requests.post(service_add_reserv,
#                                data=json.dumps(rzv),
#                                headers={'Content-type': 'application/json'}
#                                )
#             amount = rzv["TotalMoney"]
#             print(":", prev_amount_db)
#             amount_db = get_db_reserve(rezerv["CompanyUuid"]) - prev_amount_db
#             print("add_reserv ", amount, "prev_amount_db", prev_amount_db, "amount_db", amount_db)
#         except Exception as e:
#             print(e.__str__())
#
#     if runCanselResrv:
#         try:
#             cabb_reserv= dict(
#                 TenderId=rzv["TenderId"],
#                 LotId=rzv["LotId"],
#                 CompanyUuid=rzv["CompanyUuid"]
#             )
#             rq = requests.post(service_cansel_reserv,
#                                data=json.dumps(cabb_reserv),
#                                headers={'content-type': 'application/json'})
#             print("HTTP: ", rq.text, rq.reason)
#             print("runCanselResrv")
#         except Exception as e:
#             print(e.__str__())
#
#     if runReturn:
#         try:
#             returnMoney = dict(
#                 TenderId=rzv["TenderId"]
#                 # LotId=rzv["LotId"],
#                 # CompanyUuid=rzv["CompanyUuid"]
#             )
#             rq = requests.post(service_return_money,
#                                data=json.dumps(returnMoney),
#                                headers={'content-type': 'application/json'})
#             print("HTTP: ", rq.text, rq.reason)
#             print("service_return_money")
#         except Exception as e:
#             print(e.__str__())
#


    # service_fix_money
    # try:
    #     print()
    #     print("service_fix_money")
    #
    #
    #     prev_amount_db = get_db_reserve(rezerv["CompanyUuid"])
    #
    #     rq = requests.post(service_fix_money,
    #                        data=json.dumps(fix_mon),
    #                        headers={'Content-type': 'application/json'}
    #                        )
    #     print("HTTP: ", rq.text, rq.reason)
    #     amount_db = get_db_reserve(rezerv["CompanyUuid"])
    #     print("fixed ", amount, "prev_amount_db", prev_amount_db, "amount_db", amount_db)
    # except Exception as e:
    #     print(e.__str__())

#if __name__ == "__main__":

    # #  создать нормальный резерв
    # try:
    #     prev_amount_db = get_db_reserve(rezerv["CompanyUuid"])
    #
    #     rq = requests.post(service_add_reserv,
    #                        data=json.dumps(rezerv),
    #                        headers={'Content-type': 'application/json'}
    #      )
    #     print("HTTP: ", rq.text, rq.reason)
    #     amount = rezerv["TotalMoney"]
    #     print("prev_amount_db:",prev_amount_db)
    #     amount_db = get_db_reserve(rezerv["CompanyUuid"])-prev_amount_db
    #     print("positiv", amount, amount_db, amount== amount_db )
    # except Exception as e:
    #     print(e.__str__())
    #
    # #  отменить нормальный резерв
    # try:
    #     prev_amount_db = get_db_reserve(rezerv["CompanyUuid"])
    #     rq = requests.post( service_cansel_reserv,
    #                         data=json.dumps(cansel_reserv) ,
    #                         headers={'content-type': 'application/json'})
    #     print("HTTP: ", rq.text, rq.reason)
    #     amount = rezerv["TotalMoney"]
    #     print("prev_amount_db:", prev_amount_db)
    #     amount_db = prev_amount_db-get_db_reserve(rezerv["CompanyUuid"])
    #     print("positiv", amount, amount_db, amount== amount_db )
    # except Exception as e:
    #     print(e.__str__())
    #
    # #  отменить нормальный резерв - еще раз



class CheckReserv(ParamsTestCase):

    def test_01_add_rezerv(self):
        # до резервирования  1000
        prev_amount_db = get_db_reserve(self.params["rezerv"]["CompanyUuid"])

        rq = requests.post(self.params["service_add_reserv"],
                           data=json.dumps(self.params["rezerv"]),
                           headers={'Content-type': 'application/json'}
                        )
        self.assertEqual(rq.json()["result"],
                         1,
                         "POST"+self.params["service_add_reserv"]+" response "+ rq.text)
        amount = self.params["rezerv"]["TotalMoney"]

        if prev_amount_db is not None:
            amount_db = get_db_reserve(self.params["rezerv"]["CompanyUuid"])
            print("add_reserv ", amount, "prev_amount_db", prev_amount_db, "amount_db", amount_db)

        self.assertEqual(prev_amount_db-amount_db,
                         amount,
                         "Сумма резерва не равна разнице суммы до и после резервирования")

    def test_02_cansel_rezerv(self):
        prev_amount_db = get_db_reserve(self.params["cabb_reserv"]["CompanyUuid"])

        rq = requests.post(self.params["service_cansel_reserv"],
                           data=json.dumps(self.params["cabb_reserv"]),
                           headers={'content-type': 'application/json'})

        self.assertEqual(rq.json()["result"],
                         1,
                         "POST" + self.params["service_add_reserv"] + " response " + rq.text)

        if prev_amount_db is not None:
            amount_db = get_db_reserve(self.params["cabb_reserv"]["CompanyUuid"])

        self.assertGreater(amount_db, prev_amount_db,
                         "Сумма резерва не изменилась после отмены резервирования")



    # rezerv_fix(rezerv)

    #

    #
        # rezerv1 = dict(rezerv)
        # rezerv1["TenderId"] = 900
        # rezerv1["TotalMoney"] = 10
        # rezerv1["CompanyUuid"] ="C30E1D89-9D1D-4958-B3DE-5093D0B2886F"
        #
        # rezerv2 =dict(self.rezerv)
        # rezerv2["TenderId"] = 900
        # rezerv2["TotalMoney"] = 20
        # rezerv2["CompanyUuid"] = "28DAE9EC-6D86-417C-AC22-46F73EC1EB44"
        #
        # rezerv3 = dict(self.rezerv)
        # rezerv3["TenderId"] = 900
        # rezerv3["TotalMoney"] = 30
        # rezerv3["CompanyUuid"] = "436DB272-CCB3-456D-8101-F7B537A75181"

    # rezerv4 = rezerv.copy()
    # rezerv5 = rezerv.copy()

    #
        #rezerv_fix(rezerv1,runRserv=True, runCanselResrv=True, runReturn =True)
        #rezerv_fix(rezerv2,runRserv=True, runCanselResrv=False, runReturn =True)
        #rezerv_fix(rezerv3,runRserv=True, runCanselResrv=False, runReturn =True)

    # list_zrv = [rezerv1,rezerv2, rezerv3]
    # ex = ProcessPoolExecutor(max_workers=3)
    # results = ex.map(rezerv_fix, list_zrv)
    #
    # for g in results:
    #     if g != None:
    #         print(g)

    def test_02_cansel_rezerv(self):
        prev_amount_db = get_db_reserve(self.params["cabb_reserv"]["CompanyUuid"])

        rq = requests.post(self.params["service_cansel_reserv"],
                           data=json.dumps(self.params["cabb_reserv"]),
                           headers={'content-type': 'application/json'})

        self.assertEqual(rq.json()["result"],
                         1,
                         "POST" + self.params["service_add_reserv"] + " response " + rq.text)

        if prev_amount_db is not None:
            amount_db = get_db_reserve(self.params["cabb_reserv"]["CompanyUuid"])

        self.assertGreater(amount_db, prev_amount_db,
                         "Сумма резерва не изменилась после отмены резервирования")

    def test_03_return_money(self):
        prev_amount_db = get_db_balance(self.params["returnMoney"]["CompanyUuid"])

        rq = requests.post(self.params["service_return_money"],
                           data=json.dumps(self.params["returnMoney"]),
                           headers={'content-type': 'application/json'})

        self.assertEqual(rq.json()["result"],
                         1,
                         "POST" + self.params["service_add_reserv"] + " response " + rq.text)

        if prev_amount_db is not None:
            amount_db = get_db_balance(self.params["returnMoney"]["CompanyUuid"])

        self.assertGreater(amount_db, prev_amount_db,
                         "Баланс не изменился после возврата денег")

    # списание денег
    def test_04_charge_off(self):
        prev_amount_db = get_db_balance(self.params["returnMoney"]["CompanyUuid"])

        rq = requests.post(self.params["service_return_money"],
                           data=json.dumps(self.params["returnMoney"]),
                           headers={'content-type': 'application/json'})

        self.assertEqual(rq.json()["result"],
                         1,
                         "POST" + self.params["service_add_reserv"] + " response " + rq.text)

        if prev_amount_db is not None:
            amount_db = get_db_balance(self.params["returnMoney"]["CompanyUuid"])

        self.assertGreater(amount_db, prev_amount_db,
                         "Баланс не изменился после возврата денег")