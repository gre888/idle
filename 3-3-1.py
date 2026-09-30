import pandas as pd
# #iloc的使用
df=pd.read_csv("outpatient.csv")
# print(df)
# print()

# print(df.iloc[0,1])
# print(df.iloc[3,4])
# print(df.iloc[1:5,1:5])

#loc的使用
# print(df.loc[2,"roomname"])


  # 根據deptname為眼科 找出診室還掛號人數 ,資料清洗
print(df.loc[2,['roomname','regcount_person']])
# 篩選 df["deptname"].str.strip()=="板橋_眼科

result= df.loc[df["deptname"].str.strip()=="板橋_眼科",["roomname","regcount_person"]]
print(result)
# 篩選
print(df.loc[2,["roomname","regcount_person"]])

#這種方式會顯示多餘部分
print("眼科診室:",result['roomname'], "掛號人數:", result['regcount_person'])
print()

#正確寫法用loc 欄根據欄的名稱 轉成list
print(df.index)
print(list(result.index))
print(result.index)
i = list(result.index)[0]
print("列號",i)
print("眼科診室:", result.loc[i, 'roomname'], "掛號人數:", result.loc[i, 'regcount_person'])


# print("眼科診室:", result.loc[2, 'roomname'], "掛號人數:", result.loc[12, 'regcount_person'])
#眼科診室B230診
#掛號人數30
#用loc取得特定列的值


# for i in range(1,10):
#     for j in range(1,10):
#         print(f"{i}*{j}={i*j}", end="\t")
#     print()
    
# list1=[[10,20,30]
#        ,[40,50,60]
#        ,[70,80,90]
#        ]    


# for i in list1[0]:
#     print(i, end="\t")
# print()
# for i in list1[1]:
#     print(i, end="\t")
# print()
# for i in list1[2]:
#     print(i, end="\t")
# print()

# #法1
# for i in range(len(list1)):
#     for j in list1[i]:
#         print(j, end="\t")
#     print()
    
# #法2
# for i in range(len(list1)):
#     for j in range(len(list1[i])):
#         print(list1[i][j], end="\t")
#     print()
    
# #法3
# for row in list1:
#     for item in row:
#         print(item, end="\t")
#     print()



#3-3實作
# raw_data={
#   "產品": ["拿鐵","卡布奇諾","美式","摩卡","焦糖瑪奇朵"],
#   "價格": [120,130,100,150,160],
#   "庫存": [50,30,80,20,10]
# }
# #任務1 精準定位修改 請用loc將美式咖啡的庫存改為120並且列印出修改結果
# df=pd.DataFrame(raw_data)
# df.loc[df["產品"]=="美式", "庫存"] = 120
# print(df)

# result = df.loc[df["產品"]=="美式"]
# print(result)
# print()
# print(result['庫存'].values)
# result['庫存']=120
# print(result['庫存'])

import tkinter as tk
root=tk.Tk()

def click():
    print("Button clicked!")
    label4['text']='發生按下事件'
    
    
root.geometry("300x200")

label=tk.Label(root, text="Hello, World!")
label2=tk.Label(root, text="Hello, World2!")
label3=tk.Label(root, text="Hello, World3!")
label4=tk.Label(root, text="顯示結果")  # 用於顯示按鈕點擊事件

label.pack(pady=(5,0))
label2.pack(pady=(5,0))
label3.pack(pady=(5,0))
label4.pack(pady=(5,0))



#padx=(a,b)  # a表示左邊距離, b表示右邊距離


# button=tk.Button(root, text="Click Me",width=20,command=click)
# button.pack()



# tk.Label(root, text="First Name").grid(row=0,column=0)
# tk.Label(root, text="Last Name").grid(row=1,column=0)
# tk.Entry(root).grid(row=0,column=1)
# tk.Entry(root).grid(row=1,column=1)








root.mainloop()
