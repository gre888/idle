import csv
import os
data = [ {"品名": "台積電", "股價": 800, "評等": "買進"},
    	{"品名": "聯發科", "股價": 1000, "評等": "持有"},
    	{"品名": "鴻海", "股價": 150, "評等": "買進"}]


file_name="stocks.csv"

#存取文件步驟
#1. 開啟/建立文件
#2. 讀取/寫入文件
#3. 關閉文件


##with open(file_name,mode='w',encoding='utf-8-sig',newline="") as f:
##          fieldnames=["品名","股價","評等"]
##          writer = csv.DictWriter(f,fieldnames = fieldnames)
##          writer.writeheader()
##          writer.writerows(data)
##          
##with open(file_name,mode='r',encoding='utf-8-sig') as f:
##    reader=csv.DictReader(f)
##    for row in reader:
##        print(row)










  
