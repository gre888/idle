


##data = [ {"品名": "台積電", "股價": 800, "評等": "買進"},
##    	{"品名": "聯發科", "股價": 1000, "評等": "持有"},
##    	{"品名": "鴻海", "股價": 150, "評等": "買進"}]
##
#存取文件步驟
#1. 開啟/建立文件
#2. 讀取/寫入文件
#3. 關閉文件


# with open(file_name,mode='w',encoding='utf-8-sig',newline="") as f:
#           fieldnames=["品名","股價","評等"]
#           writer = csv.DictWriter(f,fieldnames = fieldnames)w
#           writer.writeheader()
#           writer.writerows(data)
          
# with open(file_name,mode='r',encoding='utf-8-sig') as f:
#     reader=csv.DictReader(f)
#     for row in reader:
#         print(row)

# new_data = {"品名": "新產品x", "股價": 500, "評等": "觀察"}        

# not_exists = False
# if not os.path.exists(file_name):
#   not_exists = True

# with open(file_name,mode='a',encoding='utf-8-sig',newline="") as f:
#     fieldnames=["品名","股價","評等"]
#     writer = csv.DictWriter(f,fieldnames = fieldnames)
#     if not_exists:
#       writer.writeheader()
#     writer.writerow(new_data)
    
    # 任務:
    #   自訂3個函數分別是儲存新文件save_csv,讀取文件read_csv,新增資料append_csv
    #   input() 讀取使用者輸入的資料，並呼叫函數儲存到csv文件中
    #   每次追加完新資料 都要透過read_csv()函數讀取文件內容，並印出來
    
import os
import csv

def save_csv(file_name, data):
    with open(file_name, mode='w', encoding='utf-8-sig', newline="") as f:
        fieldnames = ["品名", "股價", "評等"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
def read_csv(file_name):
    with open(file_name, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)
            
def input_data():
  input_data = {
    "品名": input("請輸入品名："),
    "股價": float(input("請輸入股價：")),
    "評等": input("請輸入評等：")
  }
  return input_data

def append_csv(file_name, input_data):
    not_exists = not os.path.exists(file_name)
    with open(file_name, mode='a', encoding='utf-8-sig', newline="") as f:
        fieldnames = ["品名", "股價", "評等"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not_exists:
            writer.writeheader()
        writer.writerow(input_data())
      
        

file_name="stocks.csv"
data = [ {"品名": "台積電", "股價": 800, "評等": "買進"},
    	{"品名": "聯發科", "股價": 1000, "評等": "持有"},
    	{"品名": "鴻海", "股價": 150, "評等": "買進"}]

###01 第一次
##save_csv(file_name, data)
##read_csv(file_name)
##
###02 單次
##
##append_csv(file_name, input_data)
##read_csv(file_name)

#03 多次
while True:
    read_csv(file_name)
    append_csv(file_name, input_data)
    read_csv(file_name)
    yes_or_no = input("是否繼續(y/n)")
    if yes_or_no=="n":
        break







