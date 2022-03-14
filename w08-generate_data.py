import pandas
import random
import jaydebeapi
import numpy

#connect to h2
dbConnection = jaydebeapi.connect(
    "org.h2.Driver",
    "jdbc:h2:C:/projects/DB/data/h2",
    ["sa", ""],
    "C:/Java/h2/bin/h2-1.4.200.jar")

dbCursor=dbConnection.cursor()

dbCursor.execute('TRUNCATE TABLE CONVI_PRO;')
dbCursor.execute('TRUNCATE TABLE CONVI_OUT;')
dbCursor.execute('TRUNCATE TABLE CONVI_IN;')

#generate data for information
item=['water','tissue','pen','cookie','soda','candy','cake','egg','paper','siccors',
        'lemonade','juice','pasta','pizza','bread']
ran_a=[]
ran_b=[]
k=0
while k<=14:
    ran_a.append(10*random.randint(10,30))
    ran_b.append(1*random.randint(20,50))
    k+=1
for i in range(len(ran_b)):
    dbCursor.execute("INSERT INTO CONVI_PRO(PRODUCT,NAME,PRICE,STOCK) VALUES ('%s','%s',%d,%d) " %('PRODUCT',item[i],ran_a[i],ran_b[i]))

#sampling from item and creat data for saleing projects and importing projects
item_replace_out= numpy.random.choice(item, size=1200, replace=True)

#generate data for saleing projects
ran_b_out=[]
k=0
while k<=1199:
    ran_b_out.append(1*random.randint(0,10))
    k+=1
for i in range(len(item_replace_out)):
    dbCursor.execute("INSERT INTO CONVI_OUT(OUT,NAME,NUMBER) VALUES ('%s','%s',%d) " %('OUT',item_replace_out[i],ran_b_out[i]))

#generate data for importing projects
item_replace_in= numpy.random.choice(item, size=40,replace=True)
ran_b_in=[]
k=0
while k<=39:
    ran_b_in.append(1*random.randint(0,10))
    k+=1
for i in range(len(item_replace_in)):
    dbCursor.execute("INSERT INTO CONVI_IN(IN,NAME,NUMBER) VALUES ('%s','%s',%d) " %('IN',item_replace_in[i],ran_b_in[i]))

#print datas in 3 table
dbCursor.execute('SELECT * FROM CONVI_PRO;')
dbCursor.execute('SELECT * FROM CONVI_OUT;')
dbCursor.execute('SELECT * FROM CONVI_IN;')
resultSet=dbCursor.fetchall()

for row in resultSet:
  print(row)

#close h2
dbCursor.close()
dbConnection.close()
