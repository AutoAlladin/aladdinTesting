# параметры подключения к БД

from Aladdin.DB.db import get_connection
from Aladdin.Accounting.decorators import ParamsTestCase

conn_billing_test = {
    '_server': '192.168.95.152',
    '_database': 'aladdinProzorroTest',
    '_username': 'sergey',
    '_password': 'SEGAmega2205',
    '_driver': '{ODBC Driver 13 for SQL Server}'
}

conn_prozorro_api = {
    '_server': '192.168.95.142',
    '_database': 'AladdinProzorro',
    '_username': 'sergey',
    '_password': 'SEGAmega2205',
    '_driver': '{ODBC Driver 13 for SQL Server}'
}

conn_prod = {
    '_server': '192.168.95.132',
    '_database': 'AladdinProzorro',
    '_username': 'web_actini_user',
    '_password': '18E2B855EB29411D9548FD8CA4E49DA7!',
    '_driver': '{ODBC Driver 13 for SQL Server}'
}



s_users = """
select Id, Email, EmailConfirmed, FullName, PhoneNumber, PhoneNumberConfirmed,
State, UserName, Settings, FullNameEn, IdentityCode from  AspNetUsers au 
"""

def getCompany(connection, cols=False):
    s_company = """
        select  Id,
                CompanyType,
                ContactEmail,
                ContactPhone,
                Edrpou,
                --IsPayTax,
                --SchemeEdrpouId,
                --Uuid,
                WebSiteUrl,
                convert(varchar(250), DateCreate) as DateCreate,
                --CreateUserId,
                convert(varchar(250), DateModified) as DateModified
                --ModifyUserId,
                --TaxSystem,
                --CodeVAT,
                --CodeIPN,            
                --CompanyRoleId
          from  Company cmp
          where SUBSTRING(Edrpou,1,4)!='0000'
            and SUBSTRING(WebSiteUrl,1,4)!='http'
          
    """
    crs= connection.cursor()
    if cols:
        for row in crs.columns(table='Company'):
            print(row.column_name)

    crs.execute(s_company)

    i = 0
    for row in crs.fetchall():
        i += 1
        # print(i, end="\t")
        print(str(row.Id).ljust(2), end="\t")
        #print(str(row.CompanyType).ljust(3), end="\t")
        print(str(row.ContactEmail).ljust(35), end="\t")
        #print(str(row.ContactPhone).ljust(14), end="\t")
        print(str(row.Edrpou).ljust(10), end="\t")
        print(str(row.WebSiteUrl).ljust(35), end="\t")
        # print(str(row.DateModified).ljust(20), end="\t")
        print("")

def getUserCompany(connection, cols=False):
    select = """
           select  cmp.Id,
                   au.Id as uId, 
                   au.Email, 
                   au.EmailConfirmed, 
                   au.FullName, 
                   au.PhoneNumber, 
                   au.PhoneNumberConfirmed,
                   au.UserName, 
                   au.Settings, 
                   au.FullNameEn, 
                   cmp.CompanyType,
                   cmp.ContactEmail,
                   cmp.ContactPhone,
                   cmp.Edrpou,
                   cmp.WebSiteUrl,
                   convert(varchar(250), cmp.DateCreate) as cmpDateCreate,
                   convert(varchar(250), cmp.DateModified) as cmpDateModified
             from  Company cmp 
             join  CompanyUser cu on cmp.id = cu.CompanyId                 
             join  AspNetUsers au on au.Id = cu.UserId
             where SUBSTRING(cmp.Edrpou,1,4)!='0000'
               and cmp.DateCreate >= '20171201'
              -- and cmp.DateCreate <= '20171222'
             order by cmpDateModified

       """
    crs = connection.cursor()
    if cols:
        for row in crs.columns(table='AspNetUsers'):
            print(row.column_name)

    crs.execute(select)

    i = 0
    for row in crs.fetchall():
        i += 1
        print(i, end="\t")
        print(str(row.uId).ljust(2), end="\t")
        print(str(row.Email).ljust(35), end="\t")
        print(str(row.EmailConfirmed).ljust(2), end="\t")
        print(str(row.FullName).strip().ljust(35), end="\t")
        print(str(row.cmpDateModified)[:19].ljust(20), end="\t")
        print(str(row.PhoneNumber).ljust(14), end="\t")
        print(str(row.PhoneNumberConfirmed).ljust(2), end="\t")
        print(str(row.UserName).ljust(35), end="\t")
        print(str(row.FullNameEn).ljust(38), end="\t")
        print(str(row.Id).ljust(2), end="\t")
        print(str(row.CompanyType).ljust(3), end="\t")
        print(str(row.ContactEmail).ljust(35), end="\t")
        print(str(row.ContactPhone).ljust(18), end="\t")
        print(str(row.Edrpou).ljust(10), end="\t")
        print(str(row.WebSiteUrl).ljust(40), end="\t")
        print(str(row.cmpDateCreate).ljust(20), end="\t")
        print(str(row.cmpDateModified).ljust(20), end="\t")
        print(str(row.Settings).ljust(20), end="\t")
        print("")

def getCompanyTenders(connection, cols=False):
    select = """
             select  cmp.Id,
                     au.Id as uId, 
                     au.Email, 
                     au.EmailConfirmed, 
                     au.FullName, 
                     au.PhoneNumber, 
                     au.PhoneNumberConfirmed,
                     au.UserName, 
                     au.Settings, 
                     au.FullNameEn, 
                     cmp.CompanyType,
                     cmp.ContactEmail,
                     cmp.ContactPhone,
                     cmp.Edrpou,
                     cmp.WebSiteUrl,
                     convert(varchar(250), cmp.DateCreate) as cmpDateCreate,
                     convert(varchar(250), cmp.DateModified) as cmpDateModified,
                     tnd.Id as tndId,
                     Budget,
                     Currency,
                     convert(varchar(250),tnd.Date) as tndDate,
                     convert(varchar(250),tnd.DateModified) as tndDateModified,
                     Description,
                     Description_En,
                     Description_Ru,
                     Guarantee,
                     GuaranteeCurrency,
                     Guid,
                     IsMultyLot,
                     IsVAT,
                     MinStep,
                     MinStepCurrency,
                     ProzorroId,
                     case convert(varchar(3),Status)
                        when '0'  then 'draft'
                        when '3'  then 'active.tendering'
                        when '4'  then 'active.auction'
                        when '5'  then 'active.qualification'
                        when '6'  then 'active.awarded'
                        when '7'  then 'unsuccessful'
                        when '8'  then 'complete'
                        when '9'  then 'canselled'
                        when '11' then 'active'
                        else  convert(varchar(3),status)
                     end as Status,
                     Title,
                     Title_En,
                     Title_Ru,
                     Cause,
                     CauseDescription,
                     DirectoryCauseId,
                     tnd.CreateUserId,
                     convert(varchar(250),tnd.DateCreate) as tndDateCreate,
                     tnd.ModifyUserId,
                     AuctionUrl,
                     IsBlocked,
                     Stage2TenderID,
                     DialogueID,
                     convert(varchar(250),tnd.ProzorroDateModified) as tndProzorroDateModified,
                     NBUdiscountRate,
                     FundingKind,
                     YearlyPaymentsPercentageRange,
                     convert(varchar(250),tnd.NoticePublicationDate ) as tndNoticePublicationDate,
                     MinimalStepPercentage,
                     Source,
                     Funders
               from  Company cmp 
               join  CompanyUser cu on cmp.id = cu.CompanyId                 
               join  AspNetUsers au on au.Id = cu.UserId
               join  Purchases tnd on au.Id  = tnd.CreateUserId
                                   and tnd.status !=0
              -- where  SUBSTRING(cmp.Edrpou,1,4)!='0000'

         """
    crs = connection.cursor()
    if cols:
        for row in crs.columns(table='Purchases'):
            print(row.column_name)

    crs.execute(select)

    i = 0
    for row in crs.fetchall():
        i += 1
        print(i, end="\t")
        print(str(row.uId).ljust(2), end="\t")
        print(str(row.Id).ljust(2), end="\t")
        print(str(row.tndId).ljust(6), end="\t")

        print(str(row.Email).ljust(30), end="\t")
        # print(str(row.EmailConfirmed).ljust(2), end="\t")
        # print(str(row.FullName).strip().ljust(35), end="\t")
        # print(str(row.PhoneNumber).ljust(14), end="\t")
        # print(str(row.PhoneNumberConfirmed).ljust(2), end="\t")
        # print(str(row.UserName).ljust(35), end="\t")
        # print(str(row.FullNameEn).ljust(38), end="\t")
        # print(str(row.CompanyType).ljust(3), end="\t")
        # print(str(row.ContactEmail).ljust(35), end="\t")
        # print(str(row.ContactPhone).ljust(18), end="\t")
        print(str(row.Edrpou).ljust(10), end="\t")
        # print(str(row.WebSiteUrl).ljust(40), end="\t")
        # print(str(row.cmpDateCreate).ljust(20), end="\t")
        # print(str(row.cmpDateModified).ljust(20), end="\t")
        # print(str(row.Settings).ljust(20), end="\t")
        print(str(row.Guid).ljust(32), end="\t")
        print(str(row.Status).ljust(20), end="\t")
        print(str(row.ProzorroId).ljust(22), end="\t")
        print(str(row.tndDateModified)[:19], end="\t")
        print(str(row.Title)[:40].ljust(40), end="\t")
        print(str(row.Description)[:150].ljust(150), end="\t")

        print("")

def getCompanyBids(connection, cols=False):
    select = """
             select cmp.Id as cmpId,
                    isnull(au.Id, -1) as uId, 
                    bd.Id as bidId,
                    au.Email, 
                    au.EmailConfirmed, 
                    au.FullName, 
                    au.PhoneNumber, 
                    au.PhoneNumberConfirmed,
                    au.UserName, 
                    au.Settings, 
                    au.FullNameEn, 
                    cmp.CompanyType,
                    cmp.ContactEmail,
                    cmp.ContactPhone,
                    cmp.Edrpou,
                    cmp.WebSiteUrl,
                    convert(varchar(250), cmp.DateCreate) as cmpDateCreate,
                    convert(varchar(30), cmp.DateModified) as cmpDateModified,                    
                    isnull(bd.Amount, 0) as bidAmount, 
                    bd.Currency as bidCurrency,
                    convert(varchar(30), bd.Date) as bdDate,
                    bd.Guid,
                    bd.IsVAT,
                    bd.ParticipationUrl,
                    bd.PurchaseId,
                    bd.SelfEligible,
                    bd.SelfQualified,
                    bd.Status,
                    bd.ModifyUserId,
                    bd.SubcontractingDetails,
                    bd.CreateUserId,
                    convert(varchar(30), bd.DateCreate) as bdDateCreate,
                    convert(varchar(30), bd.DateModified ) as bdDateModified,
                    bd.YearlyPaymentsPercentage,
                    bd.AmountPerformance,
                    bd.AnnualCostsReduction,
                    bd.ContractDurationYear,
                    bd.ContractDurationDays,
                    isnull(bdl.Id, 0) as bdlId,
                    bdl.Amount as bdlAmount,
                    bdl.BidId,
                    bdl.Currency,
                    convert(varchar(30),bdl.Date) as bdlDate,
                    bdl.IsVAT,
                    bdl.ParticipationUrl,
                    bdl.RelatedLot,
                    bdl.SubcontractingDetails
               from  Company cmp 
               join  CompanyUser cu on cmp.id = cu.CompanyId                 
               join  AspNetUsers au on au.Id = cu.UserId
               join  Bids bd on au.Id  = bd.CreateUserId
                            and bd.status !=0
               left join LotValue bdl on bdl.BidId = bd.Id                                 
             -- where  SUBSTRING(cmp.Edrpou,1,4)!='0000'
               order by bdl.Id

         """
    crs = connection.cursor()
    if cols:
        for row in crs.columns(table='LotValue'):
            print(row.column_name)

    crs.execute(select)

    i = 0
    for row in crs.fetchall():
        i += 1
        print(("["+str(i)+"]").ljust(4), end="\t")
        print(str(row.uId).ljust(6), end="\t")
        print(str(row.bidId).ljust(6), end="\t")
        print(str(row.bdlId).ljust(6), end="\t")

        if row.bdlId!=0:
            print(str(row.bdlAmount).ljust(10), end="\t")
        else:
            print(str(row.bidAmount).ljust(10), end="\t")

        print(str(row.bidCurrency).ljust(4), end="\t")
        print(str(row.RelatedLot).ljust(32), end="\t")
        print(str(row.bdDateCreate)[:19].ljust(6), end="\t")
        print(str(row.Guid).ljust(32), end="\t")
        print(str(row.Status).ljust(6), end="\t")
        print(str(row.ParticipationUrl).ljust(50), end="\t")




        print("")



if __name__  =="__main__":
    # mssql_connection = get_connection(**conn_prod)
    #getCompany(mssql_connection)
    # getUserCompany(mssql_connection)
    #getCompanyUser(mssql_connection,True)
    #getCompanyTenders(mssql_connection, cols=False )
    #getCompanyBids(mssql_connection,True)
    # mssql_connection.close()

    conn= get_connection(**conn_prozorro_api)

    crs = conn.cursor()
    # for row in crs.columns(table="SyncLogs"):
    #      print(row.column_name)

    res = crs.execute("""select top 500 * 
                        from ProzorroApi.SyncLogs sl 
                        order by sl.DateStart desc
                      """
                      ).fetchall()


    # crs.execute(" UPDATE [BillingTest].[dbo].[Accounts]"+
    #             " SET Balance = 500000 "+
    #             " WHERE CompanyEdrpo = '{0}' ".format("09000080"))


    for row in res:
        # print(str(row.JournalType).ljust(2), end="\t")
        print(str(row.SyncType).ljust(1), end="\t")
        print(str(row.Url).ljust(60), end="\t")
        # print(str(row.Offset).ljust(15), end="\t")
        # print(str(row.PackCount).ljust(3), end="\t")
        print(str(row.CompleteCount).ljust(3), end="\t")
        print(str(row.DateStart).ljust(15), end="\t")
        print(str(row.DateComplete).ljust(15), end="\t")
        # print(str(row.Parameters).ljust(15), end="\t")
        # print(str(row.NextDatePackage).ljust(15), end="\t")
        # print(str(row.ObjectGuids).ljust(15), end="\t")
        # print(str(row.LossObjectGuids).ljust(15), end="\t")
        print(str(row.Completed).ljust(15), end="\t")
        # print(str(row.IsRetry).ljust(15), end="\t")
        print(str(row.TestMode).ljust(15), end="\t")
        # print(str(row.Archive).ljust(15), end="\t")
        # print(str(row.SID).ljust(15), end="\t")
        print("\n")


    conn.close()