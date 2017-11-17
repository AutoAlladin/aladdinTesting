# параметры подключения к БД
from Aladdin.DB.db import get_connection

conn_billing_test={
    '_server': '192.168.95.152',
    '_database': 'BillingTest',
    '_username': 'sergey',
    '_password': 'SEGAmega2205',
    '_driver': '{ODBC Driver 13 for SQL Server}'
}

# запрос к БД для проверки наличия счета
sql_get_new_account="select AccountNumber, CompanyUuid, CompanyEdrpo, "+ \
                     " Balance, ReservedAmount, convert(varchar(250), DateModify) as DateTimeChange "+  \
                     " from BillingTest.dbo.Accounts  where CompanyUuid ='{company_uuid}' and CompanyEdrpo='{company_edr}' "

def check_new_account(uuid, edr):
    # подключение к БД
    mssql_connection = get_connection(**conn_billing_test)
    crs_account = mssql_connection.cursor()

    sql = sql_get_new_account.format(company_uuid=uuid, company_edr=edr)
    crs_account.execute(sql)
    rows = crs_account.fetchall()

    # если есть
    if len(rows) > 0:
        return "PASS: Account {0}, edr {1} created".format(uuid, edr)
    else:
        return "FAILED: Account {0}, edr {1} NOT created".format(uuid, edr)