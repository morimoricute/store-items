import pandas
import jaydebeapi

#connect h2
dbConnection = jaydebeapi.connect(
    "org.h2.Driver",
    "jdbc:h2:C:/projects/DB/data/h2",
    ["sa", ""],
    "C:/Java/h2/bin/h2-1.4.200.jar")
dbCursor = dbConnection.cursor()

#creat table of importing product
_sql=[
   "CREATE TABLE IF NOT EXISTS",
   "CONVI_IN(IN VARCHAR(100),NAME VARCHAR(100),",
   "NUMBER NUMBER);",
]

sql=' '.join(_sql)
dbCursor.execute(sql)
print(sql)

#creat table of saleing out product
_sql=[
   "CREATE TABLE IF NOT EXISTS",
   "CONVI_OUT(OUT VARCHAR(100),NAME VARCHAR(100),",
   "NUMBER NUMBER);",
]

sql=' '.join(_sql)
dbCursor.execute(sql)
print(sql)

#creat table of product information
_sql=[
   "CREATE TABLE IF NOT EXISTS",
   "CONVI_PRO(PRODUCT VARCHAR(100),NAME VARCHAR(100),",
   "PRICE NUMBER, STOCK NUMBER);",
]

sql=' '.join(_sql)
dbCursor.execute(sql)
print(sql)


#dbCursor.execute('DROP TABLE STOCKINFO;')
#dbCursor.execute('CREATE UNIQUE INDEX ON CONVI(NAME);')

dbCursor.close()
dbConnection.close()
