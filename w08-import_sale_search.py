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


print('+--------------------------------+')
print('|  Goods management System 1.0   |')
print('|       copyright:Kong QL        |')
print('|  1.Goods information entering  |')
print('|  2.Goods Query                 |')
print('|  3.Purchase                    |')
print('|  4.exit                        |')
print('|  Please select : (1/2/3/4)     |')
print('+--------------------------------+')
while True:
    Info = input('系統主介面(1錄入/2查詢/3購買/4退出):')
    if Info == '1':
    	while True:
	        warning1 = input('您正在錄入商品資訊,按回車開始(繼續)，輸入*返回上級選單：')
	        if warning1 == '*':
	            break
	        goodsName = input('請輸入商品的名稱：')
	        goodsName = str(goodsName)

	        goodsPrice = input('請輸入商品的價格：')
	        goodsPrice = int(goodsPrice)

	        goodsStock = input('請輸入商品的數量：')
	        goodsStock = int(goodsStock)
	        print('商品名稱：',Name)
	        print('商品價格：',Price)
	        print('商品數量：',Stock)

            dbCursor.execute("INSERT INTO CONVI_PRO(PRODUCT,NAME,PRICE,STOCK) VALUES ('%s','%s',%d,%d) " %('PRODUCT',goodsName,goodsPrice,goodsStock))
            dbCursor.execute("INSERT INTO CONVI_IN(IN,NAME,NUMBER) VALUES ('%s','%s',%d) " %('IN',goodsName,goodsStock))
            dbCursor.execute("SELET NAME,COUNT(NAME) FROM CONVI_PRO GROUPBY NAME HAVING (COUNT(NAME) > 1);")

    elif Info == '2':
    	while True:
	        warning2 = input('您正在查詢商品資訊,輸入l檢視，輸入*返回上級選單：')
	        if warning2 == '*':
	            break
	        elif warning2 == 'l':
	            print('商品名稱   價格   庫存')
                item=input('您想搜尋的商品:')
                dbCursor.execute("SELET * FROM CONVI_PRO WHERE NAME='%s'" %item)
	        else:
	            print('系統無法識別您的請求，請重新輸入')

    elif Info == '3':
	    print('您正在購買倉庫內商品\n目前倉庫裡的商品有：\n商品名  價格  庫存量')
        dbCursor.execute('SELECT * FROM CONVI_PRO;')

        warning3 = input('請輸入b進入購買介面,或輸入任意鍵退出：')
        while warning3 == 'b':
            buyName = input('請輸入您要購買的商品名稱：')
            buyNum = input('請輸入您要購買的商品數量：')
            buyNum = int(buyNum)
            p = dbCursor.execute("SELET PRICE FROM CONVI_PRO WHERE NAME='%s'" %item)
            n = buyNum
            sump = n * p
            print('商品名稱  價格   庫存   總價格')
            print(buyName,'\t',p,'\t',n,'\t',sump)
            cho = input('您是否同意購買並付款？輸入y或n,或按任意鍵返回上級選單（是y/否n）')
            if cho == 'n':
                print('您放棄購買)
	        #print('您放棄購買，該商品庫存剩餘：',stock())
	        elif cho == 'y':
                dbCursor.execute("INSERT INTO CONVI_OUT(OUT,NAME,NUMBER) VALUES ('%s','%s',%d) " %('OUT',buyName,buyNum))
                dbCursor.execute("SELET NAME,COUNT(NAME) FROM CONVI_IN GROUPBY NAME HAVING (COUNT(NAME) > 1);")
                dbCursor.execute("SELECT CONVI_PRO(NAME,STOCK) VALUES ('%s',%d) " %(buyName,buyNum))
                print('您選擇購買')
	                    #print('您選擇購買，該商品庫存剩餘：',stock())
	        else:
	            break
    elif Info == '4':
	    break
    else:
	    print('系統無法識別您的請求，請輸入正確的數字！')

dbCursor.close()
dbConnection.close()
