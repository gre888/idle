
# # #2-2-1：建立 Series 物件

# import pandas as pd
# idx = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
# data = [1, 4, 5, 6, 3]
# series = pd.Series(data, index=idx)
# print(series)




# series.shape




# import pandas as pd
# data = [1, 4, 5, 6, 3]
# series = pd.Series(data)
# print(series)




# import pandas as pd
# fruits = {"orange": 2, "banana": 3}
# print(pd.Series(fruits))




# # #2-2-2：取出 Series 當中的元素

# import pandas as pd
# fruits = {"banana": 3, "orange": 4, "grape": 1, "peach": 5}
# series = pd.Series(fruits)
# print(series[0:2])




# print(series[["orange", "peach"]])




# # #2-2-3：單取出「索引值」或者「內容值」-.index、.values

# import pandas as pd
# index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
# data = [10, 5, 8, 12, 3]
# series = pd.Series(data, index=index)
# print(series)




# series_index = series.index
# series_values = series.values
# print(series_index)
# print(series_values)




# # #2-2-4：新增 Series 物件的元素 – 修正為 pd.concat()

# import pandas as pd
# idx = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
# data = [10, 5, 8, 12, 3]
# series = pd.Series(data, index=idx)
# print(series)




# pineapple = pd.Series([12], index=["pineapple"])
# # pineapple = pd.Series( {"pineapple":12})
# series = pd.concat([series, pineapple])
# print(series)




# # #2-2-5：刪除 Series 物件的元素 – drop()

# import pandas as pd
# index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
# data = [10, 5, 8, 12, 3]
# series = pd.Series(data, index=index)
# print(series)




# series = series.drop("strawberry")
# print(series)




# # #2-2-6：從 Series 物件篩選出想要的元素

# import pandas as pd
# index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
# data = [10, 5, 8, 12, 3]
# series = pd.Series(data, index=index)
# print(series)




# conditions = [True, True, False, False, False]
# print(series[conditions])




# import pandas as pd
# index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
# data = [10, 5, 8, 12, 3]
# series = pd.Series(data, index=index)
# print(series[series >= 5])

# series = series[series >= 5][series < 10]
# print(series)




# #2-2-7：將 Series 的元素排序 – sort_index()、sort_values()

# import pandas as pd
# index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
# data = [10, 5, 8, 12, 3]
# series = pd.Series(data, index=index)
# print(series)

# items1 = series.sort_index()
# items2 = series.sort_values()
# print(items1)
# print()
# print(items2)




# # #2-3-1：建立 DataFrame 物件 – pd.DataFrame()

# import pandas as pd
# index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
# data1 = [10, 5, 8, 12, 3]
# data2 = [30, 25, 12, 10, 8]
# series1 = pd.Series(data1, index=index)
# series2 = pd.Series(data2, index=index)
# print(series1)
# print(series2)
# df = pd.DataFrame([series1, series2])
# print(df)




# import pandas as pd
# data = {"fruits": ["apple", "orange", "banana", "strawberry","kiwifruit"],
#         "time": [1, 4, 5, 6, 3],
#         "year": [2001, 2002, 2001, 2008, 2006]}
# df = pd.DataFrame(data)
# # print(df)

# max=0
# i=0
# for key in data:
#   if i ==0:
#     max = len(data[key])
#     i=i+1
#     continue
  
#   if len(data[key]) != max:
#     print(f"{key}: {len(data[key])}")
#   i=i+1

    



# import pandas as pd
# order_df = pd.DataFrame( [[1000, 2546, 103],
#                 [1001, 4352, 101],
#                 [1002, 342, 101]],
# columns=["id", "item_id", "customer_id"])
# print(order_df)




# #2-3-2：修改 index 和 column 的名稱 –.index、.column

# import pandas as pd
# import openpyxl
# index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
# data1 = [10, 5, 8, 12, 3]
# data2 = [30, 25, 12, 10, 8]
# series1 = pd.Series(data1, index=index)
# series2 = pd.Series(data2, index=index)
# df = pd.DataFrame([series1, series2])
# print(df)
# df.index = [1, 2]
# print(df)

# df.to_excel("output.xlsx")




# # #2-3-3：加入新的資料列 – 修正為 pd.concat()

# import pandas as pd
# data = {"fruits": ["apple", "orange", "banana", "strawberry",
#     "kiwifruit"],
#      "year": [2001, 2002, 2001, 2008, 2006],
#     "time": [1, 4, 5, 6, 3]}
# df = pd.DataFrame(data)
# series = pd.Series(["mango", 2008, 7], index=["fruits", "year", "time"])

# df = pd.concat([df, pd.DataFrame([series])], ignore_index=True)
# print(df)




# import pandas as pd
# index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
# data1 = [10, 5, 8, 12, 3]
# data2 = [30, 25, 12, 10, 8]
# data3 = [30, 12, 10, 8, 25, 3]

# series1 = pd.Series(data1, index=index)
# series2 = pd.Series(data2, index=index)

# df = pd.DataFrame([series1, series2])

# index.append("pineapple")

# series3 = pd.Series(data3, index=index)
# df = pd.concat([df, pd.DataFrame([series3])], ignore_index=True)
# print(df)




# # #2-3-4：加入新的欄位

import pandas as pd
# data = {"fruits": ["apple", "orange", "banana", "strawberry",
#   "kiwifruit"],
#   "year": [2001, 2002, 2001, 2008, 2006],
#   "time": [1, 4, 5, 6, 3]}
# df = pd.DataFrame(data)
# df["price"] = [150, 120, 100, 300, 150]
# print(df)




# import pandas as pd

# index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
# data1 = [10, 5, 8, 12, 3]
# data2 = [30, 25, 12, 10, 8]
# series1 = pd.Series(data1, index=index)
# series2 = pd.Series(data2, index=index)

# df = pd.DataFrame([series1, series2])

# new_column = pd.Series([15, 7], index=[0, 1])

# df["mango"] = new_column
# print(df)




# # #2-3-5：取出 DataFrame 當中的元素 –df.loc[]、df.iloc[]

# data = {"fruits": ["apple", "orange", "banana", "strawberry",
#   "kiwifruit"],
#   "year": [2001, 2002, 2001, 2008, 2006],
#   "time": [1, 4, 5, 6, 3]}
# df = pd.DataFrame(data)
# print(df)

# print(df.loc[1,"fruits"])
# print(df.loc[[1,2],"fruits"])

# df = df.loc[[1,2],["time","year"]]
# print(df)



# import numpy as np
# import pandas as pd
# np.random.seed(0)

# df = pd.DataFrame()

# columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
# for column in columns:
#   df[column] = np.random.choice(range(1, 11), 10)
# print(df)




# df = df.loc[range(2,6),["banana","kiwifruit"]]
# print(df)








# #2-3-6：刪除 df 物件的列或行 – drop()

# import pandas as pd
# data = {"fruits": ["apple", "orange", "banana", "strawberry",
# "kiwifruit"],
# "time": [1, 4, 5, 6, 3] ,
# "year": [2001, 2002, 2001, 2008, 2006]}
# df = pd.DataFrame(data)
# print(df)




# df_1 = df.drop([0,1])
# print(df_1)
# print()
# print(df)
# print()





# df_2 = df_1.drop("year", axis=1)
# print(df_2)




# import numpy as np
# import pandas as pd
# np.random.seed(0)

# df = pd.DataFrame()
# columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
# for column in columns:
#   df[column] = np.random.choice(range(1, 11), 10)
# print(df)




# df = df.drop(np.arange(0, 9, 2))
# df = df.drop("strawberry", axis=1)
# print(df)




# #2-3-7：將欄位值依大小排序 – sort_values()

# import pandas as pd
# data = {"fruits": ["apple", "orange", "banana", "strawberry",
#   "kiwifruit"],
#   "time": [1, 4, 3, 6, 3],
#   "year": [2001, 2002, 2001, 2008, 2006]}
# df = pd.DataFrame(data)
# print(df)




# df = df.sort_values(by="year", ascending = True)
# print(df)




# df = df.sort_values(by=["time", "year"] , ascending = True)
# print(df)




# #2-3-8：從 df 物件篩選出想要的資料

import pandas as pd
data = {"fruits": ["apple", "orange", "banana", "strawberry",
  "kiwifruit"],
  "time": [1, 4, 5, 6, 3] ,
  "year": [2001, 2002, 2001, 2008, 2006] }
df = pd.DataFrame(data)
print(df)




print(df.index % 2 == 0)
print(df[df.index % 2 == 0])




# import numpy as np
# import pandas as pd
# np.random.seed(0)
# df = pd.DataFrame()
# columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
# for column in columns:
#   df[column] = np.random.choice(range(1, 11), 10)
# print(df)




# df = df[df["apple"] >= 5]
# df = df[df["kiwifruit"] >= 5]

# # df = df.loc[df["apple"] >= 5][df["kiwifruit"] >= 5]
# print(df)

