import json
import uuid

import os

import time

from Aladdin.DB.db import get_connection
import pika


#{"companyAccount":{"uuid":"fbf3cf0b-4226-4367-9a40-b4cb10c882f7","edrpou":"12345636"},
#  "id":"8c26f9be-3aef-4c2d-b061-5bd957f7a79e","creationDate":"2017-11-01T09:59:11.1108451Z"}

#  входные парамемеры для теста
in_dic = dict()
# загрузка из файла в той же папке
with open(os.path.dirname(os.path.abspath(__file__)) + '\\input.json', 'r',
          encoding="UTF-8") as test_params_file:
    in_dic = json.load(test_params_file)

# параметры подключения к БД
conn_billing_test={
    '_server': '192.168.95.152',
    '_database': 'BillingTest',
    '_username': 'sergey',
    '_password': 'SEGAmega2205',
    '_driver': '{ODBC Driver 13 for SQL Server}'
}

# запрос к БД для проверки наличия счета
sql_get_new_account="select AccountNumber, CompanyUuid, CompanyEdrpo, "+ \
                     " Balance, ReservedAmount, convert(varchar(250), DateTimeChange) as DateTimeChange "+  \
                     " from BillingTest.dbo.Accounts  where CompanyUuid ='{company_uuid}'"

# тело месседжа в шину  для создания счета
msg_create_company_account = {'companyAccount': in_dic["new_account"] }
# генерация нового уникального кода
msg_create_company_account["companyAccount"]["uuid"]=str(uuid.uuid4())

str_json=""
# словарь в json
str_json = json.dumps(msg_create_company_account)

# параметры подключения к шине
parameters = pika.ConnectionParameters(host='192.168.80.169',
                                       port=5672,
                                       credentials= pika.PlainCredentials(
                                                'AutoTest',
                                                '66596659'
                                            )
                                       )
# имя очереди для создания счета
que = 'need_create_company_account'
con_rabbit = None

try:
    # собственно подключаемся к шине
    con_rabbit = pika.BlockingConnection(parameters)
    ch_create_company_account = con_rabbit.channel()
    ch_create_company_account.queue_declare(queue=que, durable=True)

    # кидаем сообщение
    ch_create_company_account.basic_publish(exchange='',
                                            routing_key=que,
                                            body=str_json)

    print(" [x] Sent "+str_json)

    # подключение к БД
    mssql_connection = get_connection(**conn_billing_test)
    crs_account = mssql_connection.cursor()

    try:
        time.sleep(5)
        # выполняем запрос на проверку наличия счета запрошеного через шину
        sql =  sql_get_new_account.format(company_uuid=in_dic["new_account"]["uuid"])
        crs_account.execute(sql)
        rows = crs_account.fetchall()

        # если есть
        if len(rows)>0:
            print("PASS: Account {0}, edr {1} created" \
                   .format( in_dic["new_account"]["uuid"],  in_dic["new_account"]["edrpou"]))

            in_dic["new_account"]["edrpou"] = str(int(in_dic["new_account"]["edrpou"]) + 1)
        else:
            print("FAILED: Account {0}, edr {1} NOT created"\
                  .format(in_dic["new_account"]["uuid"], in_dic["new_account"]["edrpou"]))

    except Exception as e:
        # если нету счета
        print("FAILED: Account {0}, edr {1} NOT created"
              .format(in_dic["new_account"]["uuid"], in_dic["new_account"]["edrpou"]))
        raise Exception("DB "+ e.__str__())
    finally:
        #  влюбом случае сохраняем попытку
        in_dic["used_data"]["accounts"].append(dict(uuid=in_dic["new_account"]["uuid"],
                                                    edrpou=in_dic["new_account"]["edrpou"]))

        with(open(os.path.dirname(os.path.abspath(__file__)) + '\\input.json', 'w', encoding="UTF-8")) as out_dic:
            json.dump(in_dic, out_dic)

except Exception as e :
    print(e)
finally:
    con_rabbit.close()








