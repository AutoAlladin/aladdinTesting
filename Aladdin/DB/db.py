import pyodbc
import sys
import os

def_args={
    'server': '192.168.80.90',
    'database': 'ApsMarketWork',
    'username': 'web_actini_user',
    'password': '18E2B855EB29411D9548FD8CA4E49DA7',
    'driver': '{ODBC Driver 13 for SQL Server}'
}

def get_connection(_server,_database,_username,_password,_driver):
    costr="DRIVER={driver};SERVER={server};PORT=1443;DATABASE={database};UID={username};PWD={password}"\
                          .format(driver=_driver,
                                  server=_server,
                                  database=_database,
                                  username=_username,
                                  password=_password
                                  )
    return pyodbc.connect(costr)


# cursor = get_connection(**def_args).cursor()
#
#
# cursor.execute("SELECT ContactEmail FROM [AladdinIdentity].[dbo].[Company]")
# row = cursor.fetchone()
# for i in range(30):   # Если Принт стоит под фор, то выводит только одну последнюю строку
#     row = cursor.fetchone()
#     print(row.ContactEmail)

# cursor.execute("SELECT ContactEmail FROM [AladdinIdentity].[dbo].[Company]")
# row = cursor.fetchall()
# for i in range(30):   # Если Принт стоит под фор, то выводит только одну последнюю строку
#     row = cursor.fetchone()
#     print(row.ContactEmail)



