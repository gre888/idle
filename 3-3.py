import pandas as pd
#iloc的使用
df=pd.read_csv("outpatient.csv")
print(df)
print()

# print(df.iloc[0,1])
# print(df.iloc[3,4])
# print(df.iloc[1:5,1:5])

#loc的使用
# print(df.loc[2,"roomname"])


#根據deptname為眼科 找出診室還掛號人數 ,資料清洗
repot= df.loc[df["deptname"].str.strip()=="板橋_眼科",["roomname","regcount_person"]]
print(repot)

print(df.loc[2,["roomname","regcount_person"]])

