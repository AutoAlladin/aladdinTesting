# параметры подключения к БД

from Aladdin.DB.db import get_connection
from Aladdin.Accounting.decorators import ParamsTestCase

conn_billing_test = {
    '_server': '192.168.95.152',
    '_database': 'BillingTest',
    '_username': 'sergey',
    '_password': 'SEGAmega2205',
    '_driver': '{ODBC Driver 13 for SQL Server}'
}

# запрос к БД
sql = dict(
    uid="select AccountNumber, CompanyUuid, CompanyEdrpo, " + \
        " Balance, ReservedAmount, convert(varchar(250), DateModify) as DateTimeChange " + \
        " from BillingTest.dbo.Accounts  where CompanyUuid ='{0}'",
    edr="select AccountNumber, CompanyUuid, CompanyEdrpo, " + \
        " Balance, ReservedAmount, convert(varchar(250), DateModify) as DateTimeChange " + \
        " from BillingTest.dbo.Accounts  where CompanyEdrpo ='{0}'",

    uid_edr="select AccountNumber, CompanyUuid, CompanyEdrpo, " + \
            " Balance, ReservedAmount, convert(varchar(250), DateModify) as DateTimeChange " + \
            " from BillingTest.dbo.Accounts  where CompanyEdrpo ='{0}' and CompanyUuid ='{1}'",

    uid_balance="select AccountNumber, CompanyUuid, CompanyEdrpo, " + \
                " Balance, ReservedAmount, convert(varchar(250), DateModify) as DateTimeChange " + \
                " from BillingTest.dbo.Accounts  where  CompanyUuid ='{0}' and Balance {1}",

    balance="select AccountNumber, CompanyUuid, CompanyEdrpo, " + \
            "  Balance, ReservedAmount, convert(varchar(250), DateModify) as DateTimeChange" + \
            " from BillingTest.dbo.Accounts  where  Balance {0}",
    up_bal=" update BillingTest.dbo.Accounts set Balance=1000 where CompanyEdrpo ='{0}'",

    rezerv=" Id, ParentId, TenderDetailsId, TypeTransaction, CompanyEdrpoSender, AccountNumberSender, " \
           " CompanyEdrpoReceiver, AccountNumberReceiver, Amount, Currency, ExchangeRate, " \
           " ServiceIdentifier, DocumentId, IsInvalid " \
           " from dbo.Transactions "
)

mssql_connection = get_connection(**conn_billing_test)
crs_account = mssql_connection.cursor()
#
# for row in crs_account.columns(table='Transactions'):
#     print(row.column_name)

# crs_account.execute(sql["rezerv"])

# crs_account.execute(sql["up_bal"].format("30010001"))
# crs_account.commit()
crs_account.execute(sql["edr"].format("30000222"))


#  20171510824356

rows = crs_account.fetchmany(100)

for row in rows:
    print(row)