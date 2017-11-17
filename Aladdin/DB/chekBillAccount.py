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
sql_uid="select AccountNumber, CompanyUuid, CompanyEdrpo, "+ \
                     " Balance, ReservedAmount, convert(varchar(250), DateModify) as DateTimeChange "+  \
                     " from BillingTest.dbo.Accounts  where CompanyUuid ='{0}'"
sql_edr="select AccountNumber, CompanyUuid, CompanyEdrpo, "+ \
                     " Balance, ReservedAmount, convert(varchar(250), DateModify) as DateTimeChange "+  \
                     " from BillingTest.dbo.Accounts  where CompanyEdrpo ='{0}'"

sql_uid_edr="select AccountNumber, CompanyUuid, CompanyEdrpo, "+ \
                     " Balance, ReservedAmount, convert(varchar(250), DateModify) as DateTimeChange "+  \
                     " from BillingTest.dbo.Accounts  where CompanyEdrpo ='{0}' and CompanyUuid ='{1}'"



mssql_connection = get_connection(**conn_billing_test)
crs_account = mssql_connection.cursor()
#
# for row in crs_account.columns(table='Accounts'):
#     print(row.column_name)


crs_account.execute(sql_edr.format('30000007'))
#  20171510824356
rows = crs_account.fetchall()

print(rows)