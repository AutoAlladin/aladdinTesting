# параметры подключения к БД
import pyodbc

from Aladdin.DB.db import get_connection

conn_billing_test={
    '_server': '192.168.95.152',
    '_database': 'BillingTest',
    '_username': 'sergey',
    '_password': 'SEGAmega2205',
    '_driver': '{ODBC Driver 13 for SQL Server}'
}

# запрос к БД для проверки наличия счета
SQL = dict(new_account="select AccountNumber, CompanyUuid, CompanyEdrpo, "+ \
                     " Balance, ReservedAmount, convert(varchar(250), DateModify) as DateModify "+  \
                     " from BillingTest.dbo.Accounts  where CompanyUuid ='{company_uuid}' and CompanyEdrpo='{company_edr}' ",

           uid_get_balance="select AccountNumber, CompanyUuid, CompanyEdrpo, "+ \
                    " Balance, ReservedAmount, convert(varchar(250), DateModify) as DateModify " +  \
                    " from BillingTest.dbo.Accounts  where  CompanyUuid ='{0}'",

           edr_get_balance="select AccountNumber, CompanyUuid, CompanyEdrpo, "+ \
                            " Balance, ReservedAmount, convert(varchar(250), DateModify) as DateModify " +  \
                            " from BillingTest.dbo.Accounts  where  CompanyEdrpo ='{0}'"

           )

def check_new_account(uuid, edr):
    # подключение к БД
    mssql_connection = get_connection(**conn_billing_test)
    crs_account = mssql_connection.cursor()
    sql=None


    try:
        sql = SQL["new_account"].format(company_uuid=uuid, company_edr=edr)
        crs_account.execute(sql)
    except pyodbc.ProgrammingError as kukuber:
        errtext=str(kukuber)
        if errtext.find('uniqueidentifier') < 0:
            raise Exception(kukuber)
        else:
            return "FAILED: Account {0}, edr {1} NOT created".format(uuid, edr)
    rows = crs_account.fetchall()
    # если есть
    if len(rows) > 0:
        return "PASS: Account {0}, edr {1} created".format(uuid, edr)
    else:
        return "FAILED: Account {0}, edr {1} NOT created".format(uuid, edr)

def get_db_balance(uuid=None, edr=None ):
    mssql_connection = get_connection(**conn_billing_test)
    crs_account = mssql_connection.cursor()

    if uuid is not None:
        crs_account.execute(SQL["uid_get_balance"].format(uuid))
    elif edr is not None:
        crs_account.execute(SQL["edr_get_balance"].format(edr))

    row = crs_account.fetchone()

    # если есть
    if row is None:
        return None
    else:
        if row.Balance is None:
            return 0.0
        else:
            return float(row.Balance)  #(row.Balance)

def get_db_reserve(uuid):
    mssql_connection = get_connection(**conn_billing_test)
    crs_account = mssql_connection.cursor()

    sql = SQL["uid_get_balance"].format(uuid)
    crs_account.execute(sql)
    row = crs_account.fetchone()

    # если есть
    if row is None:
        return  None
    else:
        if row.ReservedAmount is None:
            return 0.0
        else:
            return float(row.ReservedAmount)
