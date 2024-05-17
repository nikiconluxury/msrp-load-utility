import settings_vendor_load as cfg
import pandas as pd
from sqlalchemy import create_engine,text

pwd_str =f"Pwd={cfg.password};"
global conn
conn = "DRIVER={ODBC Driver 17 for SQL Server};Server=35.172.243.170;Database=luxurymarket_p4;Uid=luxurysitescraper;" + pwd_str
global engine
engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % conn)

brandID = input('''
enter BrandId:  
''')

def initialize_load(brandID):
    if int(brandID) > 0:
        connection = engine.connect()
        sql = text('Delete from utb_RetailLoadTemp Where BrandID = ' + str(brandID))
        print(sql)
        connection.execute(sql)
        connection.commit()
        connection.close()

def create_sql(brandID):

    sql = ''

    if int(brandID) == 229:
        #GUCCI BRAND
        sql = '''Insert into utb_RetailLoadTemp
            (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
            Select BrandID,  F1,   F2,    F3,     F3,        NULL,        F5,        F6,             F7,           NULL,     F22,      NULL,        F21,     NULL, NULL
            From utb_RetailLoadInitial
            Where BrandID = 229
            '''
    if int(brandID) == 26:
        #Alexander Mcqueen BRAND
        sql = '''Insert into utb_RetailLoadTemp
            (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
            Select BrandID,  F1,   F4,    F22,     F22,        NULL,        F15,        F17,             F11,           F7,     F5,      F6,           F13,     F14, F12
            From utb_RetailLoadInitial
            Where BrandID = 26
            '''
    if int(brandID) == 157:
        #Alexander Mcqueen BRAND
        sql = '''Insert into utb_RetailLoadTemp
            (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
            Select BrandID,  F1,   F2,    F5,     F3,        NULL,        F12,        F11,             NULL,           NULL,     NULL,      NULL,           F0,    NULL, NULL
            From utb_RetailLoadInitial
            Where BrandID = 157
            '''

    if int(brandID) == 93 or int(brandID) == 478 or int(brandID) == 66:
        #Bottega Venetta , YSL, BALENCIAGA
        sql = '''Insert into utb_RetailLoadTemp
            (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
            Select BrandID,  F0,   F2,   left(F26,25),   F13,     F12,        F26,        F25,           NULL,      F10,     F9,      NULL,        F21,     NULL, F3
            From utb_RetailLoadInitial
            Where BrandID = 
            ''' + str(brandID)
    return sql
def validate_temp_load(brandID):
    sql = ''

    if int(brandID) == 229:
        #GUCCI BRAND
        sql = (f"Update utb_RetailLoadTemp set Currency = 'USD' Where Currency like '$%' and BrandID ={brandID}\n"
               f"Update utb_RetailLoadTemp set MsrpPrice = Trim(Replace(Replace(MsrpPrice, '$',''), ',',''))  Where BrandID ={brandID} ")

    if int(brandID) == 26:
        #Alexander Mcqueen BRAND
        sql = (f"Update utb_RetailLoadTemp set Currency = 'USD' Where Currency like '$%' and BrandID = {brandID}\n"
               f"Update utb_RetailLoadTemp set MsrpPrice = Trim(Replace(Replace(MsrpPrice, '$',''), ',',''))  Where BrandID = {brandID}")
    if int(brandID) == 157:
        #Dolce G BRAND
        sql = f"Update utb_RetailLoadTemp set Category = Trim(Replace(Category, 'cgid%3D',''))  Where BrandID = {brandID}"

    if int(brandID) == 93:
        #Bottega Venetta
        sql = (f"Update utb_RetailLoadTemp set Currency = 'USD' Where Currency like '%/en-us/%' and BrandID ={brandID}\n"
               f"Update utb_RetailLoadTemp set ProductUrl = 'https://www.bottegaveneta.com' + Trim(ProductUrl)   where BrandID ={brandID}\n"
               f"Update utb_RetailLoadTemp set MSRPPrice  = MSRPDiscount  Where MSRPDiscount IS NOT NULL  and BrandID ={brandID}")
    if int(brandID) == 478:
        #YSL
        sql = (f"Update utb_RetailLoadTemp set Currency = 'USD' Where Currency like '%/en-us/%' and BrandID ={brandID}\n"
               f"Update utb_RetailLoadTemp set ProductUrl = 'https://www.ysl.com' + Trim(ProductUrl)   where BrandID ={brandID}\n"
               f"Update utb_RetailLoadTemp set MSRPPrice  = MSRPDiscount  Where MSRPDiscount IS NOT NULL  and BrandID ={brandID}")
    if int(brandID) == 66:
        #BALENCIAGA
        sql = (f"Update utb_RetailLoadTemp set Currency = 'USD' Where Currency like '%/en-us/%' and BrandID ={brandID}\n"
               f"Update utb_RetailLoadTemp set ProductUrl = 'https://www.balenciaga.com' + Trim(ProductUrl)   where BrandID ={brandID}\n"
               f"Update utb_RetailLoadTemp set MSRPPrice  = MSRPDiscount  Where MSRPDiscount IS NOT NULL  and BrandID ={brandID}")
    return sql



def sql_execute(sql):
    if len(sql) > 0:
        connection = engine.connect()
        sql = text(sql)
        print(sql)
        connection.execute(sql)
        connection.commit()
        connection.close()
    else:
        print('sql empty for brandi' + brandID)

initialize_load(brandID)

sql = create_sql(brandID)

sql_execute(sql)
validate_sql = validate_temp_load(brandID)
sql_execute(validate_sql)


