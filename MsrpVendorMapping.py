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

    if int(brandID) == 93 or int(brandID) == 66:
        #Bottega Venetta , BALENCIAGA
        sql = '''Insert into utb_RetailLoadTemp
            (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
            Select BrandID,  F0,   F2,   left(F26,25),   F13,     F12,        F26,        F25,           NULL,      F10,     F9,      NULL,        F21,     NULL, F3
            From utb_RetailLoadInitial
            Where BrandID = 
            ''' + str(brandID)
    if int(brandID) == 93:
        #Versace
        sql = '''Insert into utb_RetailLoadTemp
            (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
            Select BrandID,  F0,   F5,   left(F13,30),   F4  ,   F6,        F13,        F3,            NULL,       NULL,       NULL,      NULL,     ISNULL(F2, F20) ,NULL, NULL
            From utb_RetailLoadInitial
            Where BrandID =
            ''' + str(brandID)
    if int(brandID) == 481:
        #Ferragamo
        sql = '''Insert into utb_RetailLoadTemp
            (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
            Select BrandID,  F0,   F2,   left(F1,40),   F4  ,   F3,        F1,        F5,            NULL,       NULL,       NULL,      NULL,            F7 ,NULL, NULL
            From utb_RetailLoadInitial
            Where BrandID =
            ''' + str(brandID)
    if int(brandID) == 68:
        #Balmain
        sql = '''Insert into utb_RetailLoadTemp
            (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
            Select BrandID,  F0,   F2,   left(F15,25),   F6  ,   F5,        F15,        F14,            NULL,       NULL,       NULL,      NULL,    ISNULL(F12, F1) ,NULL, NULL
            From utb_RetailLoadInitial
            Where BrandID =
            ''' + str(brandID)
    if int(brandID) == 201:
        #Fendi
        sql = '''Insert into utb_RetailLoadTemp
            (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
            Select BrandID,  F0,   F3,   left(F7,40),   F4  ,   NULL,        F7,        F5,            F6,       NULL,       NULL,      NULL,   F1 ,F2, NULL
            From utb_RetailLoadInitial
            Where BrandID =
            ''' + str(brandID)
    if int(brandID) == 363:
        #Moncler
        sql = '''Insert into utb_RetailLoadTemp
            (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
            Select BrandID,  F0,   F1,   left(F3,40),   ISNULL(F4, F6)  ,   NULL,        F3,      left(F7,300),      left(F7,1000),       NULL,       NULL,          NULL,      NULL ,NULL, NULL
            From utb_RetailLoadInitial
            Where BrandID =
            ''' + str(brandID)
    if int(brandID) == 227:
        # Givenchy
        sql = '''Insert into utb_RetailLoadTemp
                    (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
                    Select BrandID,  F1,   F3,         F7,   F4  ,       NULL,        F2,      left(F5,300),   left(F5,1000),    NULL,   NULL,       NULL,   NULL ,  NULL,  NULL
                    From utb_RetailLoadInitial
                    Where BrandID =
                    ''' + str(brandID)
    if int(brandID) == 498:
        # Stella Mccartney
        sql = '''Insert into utb_RetailLoadTemp
                    (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
                    Select BrandID,  F0,   F2,     left(F6,40),   F3  ,    NULL,      F6,      F4,        left(F5,1000),    NULL,   NULL,       NULL,   NULL ,  NULL,  NULL
                    From utb_RetailLoadInitial
                    Where BrandID =
                    ''' + str(brandID)
    if int(brandID) == 187:
        # Etro
        sql = '''Insert into utb_RetailLoadTemp
                    (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
                    Select BrandID,  F1,   F3,     left(F2,40),   F4  ,    F5,      F2,      left(F6,1000),    left(F6,1000),    NULL,   NULL,       NULL,   F0 ,  NULL,  NULL
                    From utb_RetailLoadInitial
                    Where BrandID =
                    ''' + str(brandID)
    if int(brandID) == 101:
        # Burberry
        sql = '''Insert into utb_RetailLoadTemp
                    (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
                    Select BrandID,  F2,   F1,  left(F3,40),   F5  ,    F6,        F3,          F4,            NULL,            NULL,   NULL,       NULL,       F0 ,  NULL,  NULL
                    From utb_RetailLoadInitial
                    Where BrandID =
                    ''' + str(brandID)
    if int(brandID) == 252:
        # Isabel Marant
        sql = '''Insert into utb_RetailLoadTemp
                    (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
                    Select BrandID, left(F1,50), F2, left(F5,10),  F3  , F4,   F1,               F5,            F5,       NULL,   NULL,       NULL,     F0 ,  NULL,  NULL
                    From utb_RetailLoadInitial
                    Where BrandID =
                    ''' + str(brandID)

    if int(brandID) == 601:
        # Brunello Cucinelli
        sql = '''Insert into utb_RetailLoadTemp
                    (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
                    Select BrandID,    F2,   F3,  left(F1,10),   F4  ,    F5,          F1,       left(F6,1000),    left(F6,1000), NULL,     NULL,       NULL,          F0 ,  NULL,  NULL
                    From utb_RetailLoadInitial
                    Where BrandID =
                    ''' + str(brandID)
    if int(brandID) == 67:
        # Bally
        sql = '''Insert into utb_RetailLoadTemp
                    (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
                    Select BrandID,    RIGHT(F7,50),   F2,    F4,        F5  ,   F3,          F6,       F7,    left(F8,1000),      NULL,     NULL,       NULL,          F9 ,  F10,  NULL
                    From utb_RetailLoadInitial
                    Where BrandID =
                    ''' + str(brandID)
    if int(brandID) == 228:
        # Golden Goose
        sql = '''Insert into utb_RetailLoadTemp
                    (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
                    Select BrandID,   F1,   F3,  LEFT(F2,10),   F4  ,   F5,          F2,       left(F6,1000) , left(F6,1000),  NULL,   NULL,       NULL,         F0 ,  NULL,  NULL
                    From utb_RetailLoadInitial
                    Where BrandID =
                    ''' + str(brandID)
    if int(brandID) == 275:
        # Kenzo
        sql = '''Insert into utb_RetailLoadTemp
                    (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
                    Select BrandID,   F2,   F1,  LEFT(F3,30),   F6  ,   F7,          F3,      F4 ,                F5,       NULL,     NULL,          NULL,      F0 ,  NULL,  NULL
                    From utb_RetailLoadInitial
                    Where BrandID =
                    ''' + str(brandID)
    if int(brandID) == 110:
        # Canada Goose
        sql = '''Insert into utb_RetailLoadTemp
                    (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
                    Select BrandID,   F0,   F2,  LEFT(F1,45),  F3  ,   NULL,          F1,        LEFT(F4,1000) ,  LEFT(F4,1000),       NULL,     NULL,          NULL,      F6 ,  NULL,  NULL
                    From utb_RetailLoadInitial
                    Where BrandID =
                    ''' + str(brandID)
    if int(brandID) == 165:
        # D2rd Dsquared
        sql = '''Insert into utb_RetailLoadTemp
                    (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
                    Select BrandID,   F0,   F1,  LEFT(F7,45),  F2  ,   F4,          F7,        LEFT(F8,1000) ,  LEFT(F8,1000),  NULL,     NULL,     NULL,     F6 ,  NULL,  NULL
                    From utb_RetailLoadInitial
                    Where BrandID =
                    ''' + str(brandID)

    if int(brandID) == 343:
        # MCM
        sql = '''Insert into utb_RetailLoadTemp
                    (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
                    Select BrandID,   F1,   F3,  LEFT(F2,45),  F4  ,   F5,          F2,        LEFT(F6,1000) ,  LEFT(F6,1000),  NULL,     NULL,     NULL,     F0 ,  NULL,  NULL
                    From utb_RetailLoadInitial
                    Where BrandID =
                    ''' + str(brandID)
    if int(brandID) == 478:
        ###YSL
        sql = '''Insert into utb_RetailLoadTemp
                    (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
                    Select BrandID,   F4,   F11,  F25,  F29  ,   F27,               F1,     LEFT(F13,1000),  LEFT(F14,1000),F2,       F12,     NULL,         F0 ,      NULL, F10
                    From utb_RetailLoadInitial
                    Where BrandID =
                    ''' + str(brandID)
    if int(brandID) == 310:
        ###LOEWE
        sql = '''Insert into utb_RetailLoadTemp
                    (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
                    Select BrandID,   F6,   F3,  F13,       F18  ,   NULL,         F38,     LEFT(F27,1000),  NULL,          NULL,       F5,     NULL,         F1 ,      NULL, NULL
                    From utb_RetailLoadInitial
                    Where BrandID =
                    ''' + str(brandID)
    if int(brandID) == 358:
        ###Miu Miu
        sql = '''Insert into utb_RetailLoadTemp
                    (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
                    Select BrandID,   F2,   F1,  F5,       F5  ,   NULL,         F3,     LEFT(F4,1000),  LEFT(F4,1000),          NULL,       NULL,     NULL,         F0 ,      NULL, NULL
                    From utb_RetailLoadInitial
                    Where BrandID =
                    ''' + str(brandID)
    if int(brandID) == 118:
        ###Celine
        '''Insert into utb_RetailLoadTemp
                    Select BrandID,   F0,   F2,  F4,       F3  ,   NULL,         F8,     LEFT(F7,1000),  LEFT(F7,1000),          F1,       F5,     NULL,         F6 ,      NULL, NULL
                    From utb_RetailLoadInitial
                    Where BrandID =
                    ''' + str(brandID)
    if int(brandID) == 336:
        ###Marni
        sql = '''Insert into utb_RetailLoadTemp
                     (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
                     Select BrandID,   F0,   F1,  F2,       F2  ,   F3,         F6,     LEFT(F5,1000),  LEFT(F5,1000),          NULL,       NULL,     NULL,  F7 ,      NULL, NULL
                     From utb_RetailLoadInitial
                     Where BrandID =
                     ''' + str(brandID)
    if int(brandID) == 314:
        ###Loro Piana
        sql = '''Insert into utb_RetailLoadTemp
                     (BrandID,       Style, Title, Currency,MsrpPrice,MsrpDiscount,ProductUrl,ProductImageUrl,ExtraImageUrl,ColorCode,ColorName,MaterialCode,Category,Type,Season)
                     Select BrandID,   F0,   F16,  F7,       F8  ,   NULL,         F21,     LEFT(F14,1000),  LEFT(F14,1000), F1,       F19,     NULL,       F23 ,      NULL, NULL
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
        sql = (f"Update utb_RetailLoadTemp set ProductUrl = 'https://www.ysl.com' + Trim(ProductUrl)   where BrandID ={brandID}\n"
               f"Update utb_RetailLoadTemp set MsrpPrice = Trim(Replace(Replace(MsrpPrice, '$',''), ',',''))  Where BrandID ={brandID}")
                f"Update utb_RetailLoadTemp set MSRPPrice  = MSRPDiscount  Where MSRPDiscount IS NOT NULL  and BrandID ={brandID}")
    if int(brandID) == 66:
        #BALENCIAGA
        sql = (f"Update utb_RetailLoadTemp set Currency = 'USD' Where Currency like '%/en-us/%' and BrandID ={brandID}\n"
               f"Update utb_RetailLoadTemp set ProductUrl = 'https://www.balenciaga.com' + Trim(ProductUrl)   where BrandID ={brandID}\n"
               f"Update utb_RetailLoadTemp set MSRPPrice  = MSRPDiscount  Where MSRPDiscount IS NOT NULL  and BrandID ={brandID}")

    if int(brandID) == 544:
        #Versace
        sql = (f"Update utb_RetailLoadTemp set Currency = 'USD' Where Currency like '%/us/en/%' and BrandID ={brandID}\n")
    if int(brandID) == 481:
        #ferragamo
        sql = (
            f"Update utb_RetailLoadTemp set Currency = 'USD' Where Currency like '%/us/en/%' and BrandID ={brandID}\n"
            f"Update utb_RetailLoadTemp set MSRPPrice  = MSRPDiscount  Where MSRPPrice IS NULL  and BrandID ={brandID}\n"
            f"Update utb_RetailLoadTemp set MsrpPrice = Trim(Replace(Replace(MsrpPrice, '$',''), ',',''))  Where BrandID = {brandID}"
        )

    if int(brandID) == 68:
        #balmain
        sql = (
            f"Update utb_RetailLoadTemp set Currency = 'USD' Where Currency like '%us.bal%' and BrandID ={brandID}\n"
            f"Update utb_RetailLoadTemp set MSRPPrice  = MSRPDiscount  Where MSRPPrice IS NULL  and BrandID ={brandID}\n"
            f"Update utb_RetailLoadTemp set ProductUrl = 'https://'+ Trim(ProductUrl)   where BrandID ={brandID}")

    if int(brandID) == 201:
        #fendi
        sql = (
            f"Update utb_RetailLoadTemp set Currency = 'USD' Where Currency like '%/us-en/%' and BrandID ={brandID}\n"
        f"Update utb_RetailLoadTemp set MsrpPrice = Trim(Replace(Replace(MsrpPrice, '$',''), ',',''))  Where BrandID ={brandID} ")

    if int(brandID) == 363:
        #moncler
        sql = (
            f"Update utb_RetailLoadTemp set Currency = 'USD' Where Currency like '%/en-us/%' and BrandID ={brandID}\n"
            f"UPDATE utb_RetailLoadTemp\n"
           f"SET ProductImageUrl = CASE\n"
           f"WHEN CHARINDEX(',', ProductImageUrl, CHARINDEX(',', ProductImageUrl) + 1) > 0 THEN \n"
           f"REPLACE(LTRIM(RTRIM(SUBSTRING(ProductImageUrl, CHARINDEX(',', ProductImageUrl) + 1,\n "
           f"CHARINDEX(',', ProductImageUrl, CHARINDEX(',', ProductImageUrl) + 1) - CHARINDEX(',', ProductImageUrl) - 1))), '''', '')\n"
           f"ELSE NULL END\n "
           f"WHERE BrandID = {brandID}\n"
            f"Update utb_RetailLoadTemp set MsrpPrice = Trim(Replace(Replace(MsrpPrice, '$',''), ',',''))  Where BrandID = {brandID};")

    if int(brandID) == 227:
         #Givenchy
         sql = (f"Update utb_RetailLoadTemp set MsrpPrice = Trim(Replace(Replace(MsrpPrice, '$',''), ',',''))  Where BrandID ={brandID}\n"

                f"UPDATE utb_RetailLoadTemp\n"
                f"SET ProductImageUrl = CASE\n"
                f"WHEN CHARINDEX(',', ProductImageUrl) > 0 THEN \n"
                f"LTRIM(RTRIM(SUBSTRING(ProductImageUrl, 1, CHARINDEX(',', ProductImageUrl) - 1)))\n "
                f"ELSE ProductImageUrl\n"
                f"END\n "
                f"WHERE BrandID = {brandID}\n"
                )
    if int(brandID) == 498:
        # Stella Mccartney
        sql = (f"Update utb_RetailLoadTemp set MsrpPrice = Trim(Replace(Replace(MsrpPrice, '$',''), ',',''))  Where BrandID ={brandID}\n"
               f"Update utb_RetailLoadTemp set Currency = 'USD' Where Currency like '%/us/%' and BrandID ={brandID}")
    if int(brandID) == 187:
         #Etro
         sql = (f"Update utb_RetailLoadTemp set MsrpPrice = Trim(Replace(Replace(MsrpPrice, '$',''), ',',''))  Where BrandID ={brandID}\n"
                f"UPDATE utb_RetailLoadTemp\n"
                f"SET ProductImageUrl = CASE\n"
                f"WHEN CHARINDEX(',', ProductImageUrl) > 0 THEN \n"
                f"LTRIM(RTRIM(SUBSTRING(ProductImageUrl, 1, CHARINDEX(',', ProductImageUrl) - 1)))\n "
                f"ELSE ProductImageUrl\n"
                f"END\n "
                f"WHERE BrandID = {brandID}\n"
                f"Update utb_RetailLoadTemp set Currency = 'USD' Where Currency like '%/us-en/%' and BrandID ={brandID}")
    if int(brandID) == 101:
        # Burberry
        sql = (f"Update utb_RetailLoadTemp set MsrpPrice = Trim(Replace(Replace(MsrpPrice, '$',''), ',',''))  Where BrandID ={brandID}\n"
               f"Update utb_RetailLoadTemp set Currency = 'USD' Where Currency like '%us.burberry%' and BrandID ={brandID}")


    if int(brandID) == 252:
         #Isabel Marant
         sql = (f"Update utb_RetailLoadTemp set MsrpPrice = Trim(Replace(Replace(MsrpPrice, '$',''), ',',''))  Where BrandID ={brandID}\n"
                f"Update utb_RetailLoadTemp\n"
                f"SET Style = UPPER(SUBSTRING(Style,CHARINDEX('/products/', Style) + LEN('/products/'),\n"
                f"CHARINDEX('-', Style, CHARINDEX('/products/', Style) + LEN('/products/')) - (CHARINDEX('/products/', Style) + LEN('/products/'))))\n"
                f"WHERE Style LIKE '/products/%-%' AND BrandID ={brandID}"
                f"UPDATE utb_RetailLoadTemp\n"
                f"SET ProductImageUrl = CASE\n"
                f"WHEN CHARINDEX(',', ProductImageUrl) > 0 THEN \n"
                f"LTRIM(RTRIM(SUBSTRING(ProductImageUrl, 1, CHARINDEX(',', ProductImageUrl) - 1)))\n "
                f"ELSE ProductImageUrl\n"
                f"END\n "
                f"WHERE BrandID = {brandID}\n"
                f"Update utb_RetailLoadTemp\n"
                f"SET ProductImageUrl = REPLACE(ProductImageUrl, '//', '')\n"
                f"WHERE ProductImageUrl LIKE '%//%' and BrandID ={brandID}\n"
                f"Update utb_RetailLoadTemp set ProductUrl = 'https://us.isabelmarant.com' + Trim(ProductUrl)   where BrandID ={brandID}\n"
                f"Update utb_RetailLoadTemp set ProductImageUrl = 'https://' + Trim(ProductImageUrl)   where BrandID ={brandID}\n"
                f"Update utb_RetailLoadTemp set Currency = 'USD' Where Currency like '%//us.isabe%' and BrandID ={brandID}")

    if int(brandID) == 601:
         #Brunello Cucinelli
         sql = (f"Update utb_RetailLoadTemp set MsrpPrice = Trim(Replace(Replace(MsrpPrice, '$',''), ',',''))  Where BrandID ={brandID}\n"
                
                f"UPDATE utb_RetailLoadTemp\n"
                f"SET ProductImageUrl = CASE\n"
                f"WHEN CHARINDEX('AG,', ProductImageUrl) > 0 THEN \n"
                f"LTRIM(RTRIM(SUBSTRING(ProductImageUrl, 1, CHARINDEX('AG,', ProductImageUrl) + 1)))\n "
                f"ELSE ProductImageUrl\n"
                f"END\n "
                f"WHERE BrandID = {brandID}\n"

                f"Update utb_RetailLoadTemp\n"
                f"SET ColorCode = UPPER(SUBSTRING(ProductImageUrl, CHARINDEX('-', ProductImageUrl, CHARINDEX('/original/', ProductImageUrl) + LEN('/original/')) + 1,\n"
                f"                        CASE WHEN CHARINDEX('-', ProductImageUrl, CHARINDEX('-', ProductImageUrl, CHARINDEX('/original/', ProductImageUrl) + LEN('/original/')) + 1) > 0 \n"
                f"                             THEN CHARINDEX('-', ProductImageUrl, CHARINDEX('-', ProductImageUrl, CHARINDEX('/original/', ProductImageUrl) + LEN('/original/')) + 1) - \n"
                f"                                  CHARINDEX('-', ProductImageUrl, CHARINDEX('/original/', ProductImageUrl) + LEN('/original/')) - 1\n"
                f"                             ELSE 0 \n"
                f"                        END))\n"
                f"WHERE BrandID ={brandID}\n"

                f"Update utb_RetailLoadTemp set ProductUrl = 'https://shop.brunellocucinelli.com' + Trim(ProductUrl)   where BrandID ={brandID}\n"
                
                
                f"Update utb_RetailLoadTemp set Style = Trim(Style) + TRIM(ColorCode)  where BrandID ={brandID}\n"
                
                
                f"Update utb_RetailLoadTemp set Currency = 'USD' Where Currency like '%/en-us/%' and BrandID ={brandID}")

    if int(brandID) == 67:
         #BALLY
         sql = f"""
                UPDATE utb_RetailLoadTemp
                SET Style = SUBSTRING(
                    Style,
                    CHARINDEX('BALLY_', Style) + 6, 
                    LEN(Style) - CHARINDEX('BALLY_', Style) - CHARINDEX('_', REVERSE(Style), CHARINDEX('.', REVERSE(Style))) - 6  -- Length up to the last '_' before '.jpg'
                )
                WHERE CHARINDEX('BALLY_', Style) > 0
                  AND CHARINDEX('.', Style) > 0
                """+ f"AND BrandID = {brandID};"

    if int(brandID) == 228:
         #goldengoose
         sql = (f"Update utb_RetailLoadTemp set MsrpPrice = Trim(Replace(Replace(MsrpPrice, '$',''), ',',''))  Where BrandID ={brandID}\n"
                
     
                f"UPDATE utb_RetailLoadTemp\n"
                f"SET ProductImageUrl = CASE\n"
                f"WHEN CHARINDEX(',', ProductImageUrl) > 0 THEN \n"
                f"LTRIM(RTRIM(SUBSTRING(ProductImageUrl, 1, CHARINDEX(',', ProductImageUrl) - 1)))\n "
                f"ELSE ProductImageUrl\n"
                f"END\n "
                f"WHERE BrandID = {brandID}\n"
                

                f"Update utb_RetailLoadTemp set ProductUrl = 'https://www.goldengoose.com' + Trim(ProductUrl)   where BrandID ={brandID}\n"
                
                f"Update utb_RetailLoadTemp set Currency = 'USD' Where Currency like '%/us/en/%' and BrandID ={brandID}")

    if int(brandID) == 275:
         #Kenzo


        sql = (f"Update utb_RetailLoadTemp set Currency = 'USD' Where Currency like '%/en-us/%' and BrandID ={brandID}\n"
               f"Update utb_RetailLoadTemp set MsrpPrice = Trim(Replace(Replace(MsrpPrice, '$',''), ',',''))  Where BrandID ={brandID} ")


    if int(brandID) == 110:
        #Canada Goose
        sql = (
            f"Update utb_RetailLoadTemp set Currency = 'USD' Where Currency like '%/us/en/%' and BrandID ={brandID}\n"
            
            f"UPDATE utb_RetailLoadTemp\n"
            f"SET ProductImageUrl = CASE\n"
            f"WHEN CHARINDEX('jpg,', ProductImageUrl) > 0 THEN \n"
            f"LTRIM(RTRIM(SUBSTRING(ProductImageUrl, 1, CHARINDEX('jpg,', ProductImageUrl) + 2)))\n "
            f"ELSE ProductImageUrl\n"
            f"END\n "
            f"WHERE BrandID = {brandID}\n"
            
            
            
            f"Update utb_RetailLoadTemp set MsrpPrice = Trim(Replace(Replace(MsrpPrice, '$',''), ',',''))  Where BrandID = {brandID};")

    if int(brandID) == 165:
        # Canada Goose
        sql = (
            f"Update utb_RetailLoadTemp set Currency = 'USD' Where Currency like '%/us/%' and BrandID ={brandID}\n"

            f"UPDATE utb_RetailLoadTemp\n"
            f"SET ProductImageUrl = CASE\n"
            f"WHEN CHARINDEX(',', ProductImageUrl) > 0 THEN \n"
            f"LTRIM(RTRIM(SUBSTRING(ProductImageUrl, 1, CHARINDEX(',', ProductImageUrl) - 1)))\n "
            f"ELSE ProductImageUrl\n"
            f"END\n "
            f"WHERE BrandID = {brandID}\n"



            f"Update utb_RetailLoadTemp set MsrpPrice = Trim(Replace(Replace(MsrpPrice, '$',''), ',',''))  Where BrandID = {brandID};")

    if int(brandID) == 343:
        #MCM
        sql = (
            f"Update utb_RetailLoadTemp set Currency = 'USD' Where Currency like '%/en_US/%' and BrandID ={brandID}\n"
            
           f"UPDATE utb_RetailLoadTemp\n"
           f"SET ProductImageUrl = CASE\n"
           f"WHEN CHARINDEX(',', ProductImageUrl, CHARINDEX(',', ProductImageUrl) + 1) > 0 THEN \n"
           f"REPLACE(LTRIM(RTRIM(SUBSTRING(ProductImageUrl, CHARINDEX(',', ProductImageUrl) + 1,\n "
           f"CHARINDEX(',', ProductImageUrl, CHARINDEX(',', ProductImageUrl) + 1) - CHARINDEX(',', ProductImageUrl) - 1))), '''', '')\n"
           f"ELSE NULL END\n "
           f"WHERE BrandID = {brandID}\n"
 
            f"UPDATE utb_RetailLoadTemp\n"
            f"SET MsrpPrice = RTRIM(LTRIM(LEFT(MsrpPrice, CHARINDEX('-', MsrpPrice) - 1)))\n"
            f"WHERE CHARINDEX('-', MsrpPrice) > 0\n"
            f"AND BrandID = {brandID}\n"
            f"Update utb_RetailLoadTemp set MsrpPrice = Trim(Replace(Replace(MsrpPrice, '$',''), ',',''))  Where BrandID = {brandID};")

    if int(brandID) == 358:
        # Miu Miu
        sql = (
            f"Update utb_RetailLoadTemp set Currency = 'USD' Where Currency like '%$%' and BrandID ={brandID}\n"

            f"UPDATE utb_RetailLoadTemp\n"
            f"SET ProductImageUrl = CASE\n"
            f"WHEN CHARINDEX(',', ProductImageUrl) > 0 THEN \n"
            f"LTRIM(RTRIM(SUBSTRING(ProductImageUrl, 1, CHARINDEX(',', ProductImageUrl) - 1)))\n "
            f"ELSE ProductImageUrl\n"
            f"END\n "
            f"WHERE BrandID = {brandID}\n"
            f"Update utb_RetailLoadTemp set MsrpPrice = Trim(Replace(Replace(MsrpPrice, '$',''), ',',''))  Where BrandID = {brandID};")


    if int(brandID)==118:
        #Celine
        sql = (f"Update utb_RetailLoadTemp set ProductUrl = 'https://www.celine.com' + Trim(ProductUrl)   where BrandID ={brandID}\n"
                f"UPDATE utb_RetailLoadTemp\n"
                f"SET ProductImageUrl = CASE\n"
                f"WHEN CHARINDEX(',', ProductImageUrl) > 0 THEN \n"
                f"LTRIM(RTRIM(SUBSTRING(ProductImageUrl, 1, CHARINDEX(',', ProductImageUrl) - 1)))\n "
                f"ELSE ProductImageUrl\n"
                f"END\n "
                f"WHERE BrandID = {brandID}\n")

    if int(brandID)==336:
        #Marni
        sql = (f"Update utb_RetailLoadTemp set ProductUrl = 'https://www.marni.com' + Trim(ProductUrl)   where BrandID ={brandID}\n"
               f"UPDATE utb_RetailLoadTemp\n"
               f"SET ProductImageUrl = CASE\n"
               f"  WHEN CHARINDEX(',', ProductImageUrl) > 0 THEN \n"
               f"    CASE\n"
               f"     WHEN CHARINDEX(',', ProductImageUrl, CHARINDEX(',', ProductImageUrl) + 1) > 0 THEN \n"
               f"       LTRIM(RTRIM(SUBSTRING(ProductImageUrl, \n"
               f"                            CHARINDEX(',', ProductImageUrl) + 1, \n"
               f"                            CHARINDEX(',', ProductImageUrl, CHARINDEX(',', ProductImageUrl) + 1) - CHARINDEX(',', ProductImageUrl) - 1)))\n"
               f"  ELSE \n"
               f"     LTRIM(RTRIM(SUBSTRING(ProductImageUrl, \n"
               f"                          CHARINDEX(',', ProductImageUrl) + 1, \n"
               f"                         LEN(ProductImageUrl))))\n"
               f"   END\n"
               f" ELSE ProductImageUrl\n"
               f"END\n"
               f"Where BrandID ={brandID}\n"
               f"Update utb_RetailLoadTemp set Currency = 'USD' Where Currency like '%$%' and BrandID ={brandID}\n"
               f"Update utb_RetailLoadTemp set MsrpPrice = Trim(Replace(Replace(MsrpPrice, '$',''), ',',''))  Where BrandID ={brandID}\n"
               f"Update utb_RetailLoadTemp set MsrpDiscount = Trim(Replace(Replace(MsrpDiscount, '$',''), ',',''))  Where BrandID ={brandID}"
               )
    if int(brandID) == 314:
        # Loro Piana
        sql = (
            f"Update utb_RetailLoadTemp set ProductUrl = 'https://us.loropiana.com' + Trim(ProductUrl)   where BrandID ={brandID}\n"
            f"UPDATE utb_RetailLoadTemp\n"
            f"SET ProductImageUrl = CASE\n"
            f"  WHEN CHARINDEX('|', ProductImageUrl) > 0 THEN \n"
            f"    CASE\n"
            f"     WHEN CHARINDEX('|', ProductImageUrl, CHARINDEX('|', ProductImageUrl) + 1) > 0 THEN \n"
            f"       LTRIM(RTRIM(SUBSTRING(ProductImageUrl, \n"
            f"                            CHARINDEX('|', ProductImageUrl) + 1, \n"
            f"                            CHARINDEX('|', ProductImageUrl, CHARINDEX('|', ProductImageUrl) + 1) - CHARINDEX('|', ProductImageUrl) - 1)))\n"
            f"  ELSE \n"
            f"     LTRIM(RTRIM(SUBSTRING(ProductImageUrl, \n"
            f"                          CHARINDEX('|', ProductImageUrl) + 1, \n"
            f"                         LEN(ProductImageUrl))))\n"
            f"   END\n"
            f" ELSE ProductImageUrl\n"
            f"END\n"
            f"Where BrandID ={brandID}\n"
            )

            f"Update utb_RetailLoadTemp set MsrpPrice = Trim(Replace(Replace(MsrpPrice, '$',''), ',',''))  Where BrandID = {brandID};")

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



