import pandas as pd


# s = pd.Series([100, 200, 300], index=["台北", "台中", "高雄"])
# print(s)
# print(f"台中的數值是: {s['台中']}")


#練習 
# 1. 列出所有診間掛號人數
# 2. 找出掛號人數最多的診間
df=pd.read_csv("outpatient.csv")


# se=df["regcount_person"]
# print(se.max())
# regcount_list=list(se.items())

# for index, value in se.items():
#     if value == se.max():  #等號左右兩邊數量要一致 右邊是兩個元素tuple 
#         print(index,value)
#         break   # 找到掛號人數最多的診間後跳出迴圈 不然下面顯示會找到不一樣的
      
        
# print()

# se2 =df["deptname"]
# print(se2)
# se2=se2[index]
# print(se2)

# print()

# se3=df["roomname"]
# print(se3)
# se3=se3[index]
# print(se3)

data = {
    "日期": ["2026-04-13", "2026-04-14", "2026-04-15","2026-04-16","2026-04-17","2026-04-20","2026-04-21",None],
    "收盤價": [810, 815, 805, 820, 825, 700, 700, None],
    "漲跌": [5, 5, -10, -5, -5, -15, 0, None]
}
df = pd.DataFrame(data)

print(df[0:3])
