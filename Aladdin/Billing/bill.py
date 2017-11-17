import datetime
import json
import os
import time
import uuid

from Aladdin.DB.billing import check_new_account
from Aladdin.Rabbit.sender import send_simple


def new_account(que, str_json,in_dic):
    send_simple(que,str_json)
    res=""
    try:
        time.sleep(7)
        # выполняем запрос на проверку наличия счета запрошеного через шину
        res= check_new_account(in_dic["new_account"]["uuid"], in_dic["new_account"]["edrpou"])

        if res.startswith("PASS"):
            in_dic["used_data"]["accounts"].append(dict(uuid=in_dic["new_account"]["uuid"],
                                                edrpou=in_dic["new_account"]["edrpou"],
                                                status="PASS"
                                                )
                                           )
        elif res.startswith("FAIL"):
            in_dic["used_data"]["accounts"].append(dict(uuid=in_dic["new_account"]["uuid"],
                                                    edrpou=in_dic["new_account"]["edrpou"],
                                                    status="FAIL"))

    except Exception as e:
        in_dic["used_data"]["accounts"].append(dict(uuid=in_dic["new_account"]["uuid"],
                                                    edrpou=in_dic["new_account"]["edrpou"],
                                                    status="FAIL",
                                                    error_msg=e.__str__()))
        raise Exception("DB " + e.__str__())
    finally:
        #  влюбом случае сохраняем попытку
        with(open(os.path.dirname(os.path.abspath(__file__)) + '\\input.json', 'w', encoding="UTF-8")) as out_dic:
            json.dump(in_dic, out_dic)

    return res



if __name__ == "__main__":
    #  входные парамеры для теста
    in_dic = dict()
    with open(os.path.dirname(os.path.abspath(__file__)) + '\\input.json', 'r',
              encoding="UTF-8") as test_params_file:
        in_dic = json.load(test_params_file)

    in_dic["new_account"]["uuid"] = str(uuid.uuid4())
    msg_create_company_account = json.dumps({'companyAccount': in_dic["new_account"] })
    old_id = in_dic["new_account"]["uuid"]
    old_edr = in_dic["new_account"]["edrpou"]


    print("new ACC, new EDR")
    start_test_method = datetime.datetime.now()
    print(new_account(que='need_create_company_account',
                str_json=msg_create_company_account,
                in_dic=in_dic))
    final_test_method = datetime.datetime.now()
    print("duration",(final_test_method - start_test_method).total_seconds())


    in_dic["new_account"]["uuid"] = str(uuid.uuid4())
    in_dic["new_account"]["edrpou"] = old_edr
    msg_create_company_account = json.dumps({'companyAccount': in_dic["new_account"]})
    print("new ACC, old EDR")
    print(new_account(que='need_create_company_account',
                str_json=msg_create_company_account,
                in_dic=in_dic))

    in_dic["new_account"]["uuid"] = old_id
    in_dic["new_account"]["edrpou"] =str(int(old_edr)+1)
    msg_create_company_account = json.dumps({'companyAccount': in_dic["new_account"]})
    print("old ACC, new EDR")
    print(new_account(que='need_create_company_account',
                      str_json=msg_create_company_account,
                      in_dic=in_dic))

    in_dic["new_account"]["uuid"] = old_id
    in_dic["new_account"]["edrpou"]=old_edr
    msg_create_company_account = json.dumps({'companyAccount': in_dic["new_account"]})
    print("old ACC, old EDR")
    print(new_account(que='need_create_company_account',
                str_json=msg_create_company_account,
                in_dic=in_dic))











