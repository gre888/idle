

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def set_age(self, age):
#         self.age = age
#     def get_age(self):
#         return self.age
# s1 =Student("Alice", 20)
# print(s1.get_age())

# s2=s1
# s2.set_age(25)

# print("s2.age=",s2.get_age())
# print("s1.age=",s1.get_age())
# print(s1 is s2)



# raw_data = [
#     {"item": "iPhone 15", "price": "$29,900"},
#     {"item": "iPhone 15", "price": "$29,900"},
#     {"item": "iPad Air", "price": "$19,500"},
#     {"item": "MacBook", "price": "None"} # 缺失值
# ]

# s="$29,900" #python字串immutalbe不可變的特性
# # s="abcd"
# # s2="xyz"
# # print(s is s2)
# print(s.replace("$","")) 
# print(s.replace(",",""))
# print(s.replace("$", "").replace(",","")) # replace字串是副本所以可以再一次replace 但是s依然不變
# print(s) # 原始字串依然不變
# s=s.replace("$", "").replace(",","") #用s指定儲存才能改變
# print(s) # 現在s已經被更新
# print("---------")
# for item in raw_data:
#   item["price"] = item["price"].replace("$", "").replace(",","")
#   print(item["price"])
    
# print("---------")

# raw_data=[10,10,20,20,20,30,30]
# #去除重複
# raw_data = list(set(raw_data))
# print(raw_data)

# for item in raw_data:
#   count = raw_data.count(item)
#   if count > 2:
#     for i in range(count - 1):
#       raw_data.remove(item)
# print(raw_data)

#-----------------------
# import pandas as pd
# raw_data = [
#     {"item": "iPhone 15", "price": "$29,900"},
#     {"item": "iPhone 15", "price": "$29,900"},
#     {"item": "iPad Air", "price": "$19,500"},
#     {"item": "MacBook", "price": "None"} # 缺失值
# ]
# df = pd.DataFrame(raw_data) #list + dict -> DataFrame適合處理
# print(df)
# df=df.drop_duplicates() #DataFrame和字串一樣不可變,所以要指定儲存才能改變
# print(df)
# df=df.reset_index(drop=True) # 重置索引，並丟棄原索引
# df["price"] = df["price"].str.replace("$", "").str.replace(",","") 
# df["price"] = pd.to_numeric(df["price"], errors="coerce") 
# print(df)



# df2 = pd.DataFrame([{"item": "iPhone 15", "price": "$29,900"}]) # 單一資料列的DataFrame
# print(df2)
# df3 = pd.DataFrame([10,30,60,50,40]) # 對list都可以 字典不行
# print(df3)

# 3-1 ----------
# import pandas as pd

# df = pd.DataFrame(
#     [
#         {"城市": "台北", "溫度": 25},
#         {"城市": "台中", "溫度": 28},
#         {"城市": "高雄", "溫度": 30},
#     ]
# )

# print(df)
# print("平均溫度=", df["溫度"].mean())



# import pandas as pd
# import json

# with open("F-C0032-027.json", encoding="utf-8") as f:
#     data27 = json.load(f)
#     print(data27)
#     print()
#     print(data27["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1])
#     print("--------------------------------")
# df27 = pd.DataFrame(data27)
# print(df27["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1])
# print(df27["cwaopendata"]["Dataset"]["Locations"]["Location"]["LocationName"])


# with open("F-C0032-027.json", encoding="utf-8") as f:
#     data27 = json.load(f)
# df27 = pd.DataFrame(data27)





# # list1=[10,30,20,50,40]
# # print(list1.index(50))
# # s="abcdefg"
# # print(s.index("d"))

# temp_data27=df27["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1]
# print("溫度",temp_data27)
# start=temp_data27.index("溫")+1
# end=temp_data27.index("至")
# print("最小溫度",temp_data27[start:end])
# start=temp_data27.index("至")
# end=temp_data27.index("度",start)
# print("最大溫度",temp_data27[start:end])

# print("--------------------------------")

# import pandas as pd
# import json

# file_list = [
#     "F-C0032-027.json",
#     "F-C0032-010.json",
#     "F-C0032-013.json",
#     "F-C0032-018.json",
#     "F-C0032-026.json"
# ]

# for file_name in file_list:
#     with open(file_name, encoding="utf-8") as f:
#         data = json.load(f)
#     df = pd.DataFrame(data)
#     temp_data = df[
#         "cwaopendata"
#     ]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1]
#     print(df["cwaopendata"]["Dataset"]["Locations"]["Location"]["LocationName"])

#     start = temp_data.index("溫") + 1
#     end = temp_data.index("至")
#     min_temp = temp_data[start:end]
    
#     start = temp_data.index("至") + 1
#     end = temp_data.index("度", start)
#     max_temp = temp_data[start:end]

#     avg_temp = (int(min_temp) + int(max_temp)) / 2

#     print("最小溫度：", min_temp)
#     print("最大溫度：", max_temp)
#     print("平均溫度：", avg_temp)
#     print("--------------------------------")

#3-1-3-----------------
import pandas as pd
df1=pd.DataFrame({"title":["新聞A"],"clicks":[100]})
print(df1)
df2=pd.DataFrame({"title":["新聞B"],"clicks":[250]})
print(df2)

all_news = pd.concat([df1, df2],ignore_index=True)
print(all_news)




