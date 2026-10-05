import pandas as pd

# #iloc的使用
# df=pd.read_csv("outpatient.csv")
# print(df)
# print()

# print(df.iloc[0,1])
# print(df.iloc[3,4])
# print(df.iloc[1:5,1:5])

#loc的使用
# print(df.loc[2,"roomname"])

df=pd.read_csv("data_3-3-1.csv",header=None)
print(df)
print("-"*50)

print(df[0]) #第0欄 column
print("-"*50)
print(df.values[0]) #第0列row
print("-"*50)
print(df.iloc[0]) #第0列row  變直的排列 因為得到series
print("-"*50)
print(*df.iloc[0]) #用*號拆開變成單獨的元素 第0列row  變直的排列 因為得到series
print("-"*50)
print(df.iloc[0,1])
print("-"*50)

for i in range(len(df)):
    for j in range(len(df.iloc[i])):
        print(df.iloc[i][j], end="\t")
    print()
print("-"*50)

for i in range(len(df)):
    for j in range(len(df.iloc[i])):
        print(df.iloc[i,j], end="\t")
    print()
print("-"*50)

r,c=df.shape
for i in range(r):
    for j in range(c):
        print(df.iloc[i,j], end="\t")
    print()
print("-"*50)

#iloc子集範圍
# 50 60
# 80 90
print(df.iloc[1:3,1:3])
print("-"*50)


##iloc的使用範例
print(df.iloc[0:2, 0:2])
print("-"*50)

##loc的使用範例
print(df.loc[0:1, 0:1])
print("-"*50)


##loc的使用
print(df.loc[0]) #使用loc選取子集範圍
print("-"*50)
print(df.loc[0, 1])
print("-"*50)

#看不出iloc 和loc的差別 因為要為df設定欄名列名 數字索引，若是有自訂索引，loc會依照索引標籤選取，而iloc依照位置選取
df.columns=["col1","col2","col3"]
df.index=["row1","row2","row3"]
print(df)
print("-"*50)
print("使用自訂索引後的loc選取範例")
print(df.loc["row1"]) #使用自訂索引選取第一列
print("-"*50)
print(df.loc["row1", "col2"]) #使用自訂索引選取特定元素
print("-"*50)
print("使用自訂索引後的iloc選取範例")
print(df.iloc[0]) #使用iloc選取第一列
print("-"*50)
print(df.iloc[0, 1]) #使用iloc選取特定元素
print("-"*50)

s1="ABCDEFG"
s1[:3]
s1[3:] #效果s1[3:len(s1)]
#針對某些列且欄位階大於50的情況 col2裡面只有row3 80>50再選出所有欄 所以只會選出row3
print(df.loc[df["col2"]>50, :])
print()
#.loc , 某一列,欄 針對某些列且第三欄大於50的情況,範圍在第三欄 搜尋結果為60 90

print(df.loc[df["col2"]>40,"col3"])
# loc 只能標籤 print(df.loc[df["col2"]>40,2:3])



