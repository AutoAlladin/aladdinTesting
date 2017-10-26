import pyodbc
import sys
import os



#server = "192.168.95.132"
server = "192.168.80.90"
#database = "AladdinIdentity"
database = "AladdinIdentity"
#username = 'aladdin_identity_user'
username = 'web_actini_user'
password = '18E2B855EB29411D9548FD8CA4E49DA7'
#password = '80FE7E09-8B85-4E2A-82B3-D0532B2A8E80'
driver= '{ODBC Driver 13 for SQL Server}'

cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


cursor.execute("SELECT Id, CompanyType, ContactEmail, ContactPhone, Edrpou, IsPayTax, RowVersion FROM [dbo].[Company]")

#cursor.execute("SELECT TOP 1000 Id, CompanyType, ContactEmail, ContactPhone, CreateUserId, DateCreate, DateModified, Edrpou, IsPayTax, ModifyUserId, RowVersion, SchemeEdrpouId, State, Uuid, WebSiteUrl, TaxSystem, CodeVAT FROM [AladdinIdentity].[dbo].[Company]")
#cursor.execute("SELECT top 50 prozorro_tokenc, local_object_code, prozorro_ucode, prozorro_category FROM log.Upload")
for i in range(30):
    row = cursor.fetchall() #Если Print отдельный - цикл перебирает все строки и выводит последнюю строку, если print под for выводит 30 строк, чтобы вывести первую строку цикл не используется
    print(row[1].Id, row.ContactEmail)




