import numpy as np
import jaydebeapi
#array=np.column_stack(array(a,b,c))
#print(array)

dbConnection = jaydebeapi.connect(
    "org.h2.Driver",
    "jdbc:h2:C:/projects/DB/data/h2",
    ["sa", ""],
    "C:/Java/h2/bin/h2-1.4.200.jar")

dbCursor = dbConnection.cursor()


def stock(a):
    stock=[]

    "SELECT COLUMN STOCK FROM CONVI_PRO WHERE COLUMN NAME='%S'"
    stock_in=dbCursor.execute("SELECT COLUMN STOCK FROM CONVI_PRO WHERE COLUMN(NAME)='%S'" %a)
    stock_in="SELECT COLUMN STOCK FROM CONVI_PRO WHERE "
    stock_out="SELECT COLUMN STOCK FROM CONVI_PRO"


#sql=["SELECT COLUMN STOCK FROM CONVI_PRO WHERE COLUMN NAME VALUES('%S')" %'appele']

for
name=dbCursor.execute("SELECT NAME FROM CONVI_PRO ;")
#stock_in=dbCursor.execute("SELECT COLUMN STOCK FROM CONVI_PRO WHERE COLUMN NAME VALUES('%s')" %'appele')
print(name)
