# import pandas as pd
# import csv
# import matplotlib.pyplot as plt

# file_name = "3-6-task2.csv"
# with open(file_name, "r", newline="", encoding="utf-8") as f:
#     reader = csv.DictReader(f)
#     data = list(reader)
# df = pd.DataFrame(data)
# df["營收"] = pd.to_numeric(df["營收"])  # 把營收從字串轉成數字
# summary = df.groupby("分店").agg({
#     "營收": ["sum", "mean", "max", "min"]
# })
# print(summary)
# 以下是另一種寫法，使用 astype 轉換營收為整數，並計算最高與最低業績
# df = pd.DataFrame(data)
# df["營收"] = df["營收"].astype(int)
# result = df.groupby("分店")["營收"].agg(
#     最高業績="max",
#     最低業績="min")
# print(result)



import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]
file_name = Path(__file__).parent / "3-6-task2.csv"
df_trend = pd.read_csv(file_name)


summary = df_trend.groupby("分店").agg({
    "營收": [ "max", "min"]
    })
print(summary)


summary["營收"][["max", "min"]].plot(
    kind="bar",
    figsize=(10, 6),
    color=["skyblue", "lightgreen"]
    )
plt.ylabel("營收")
plt.xlabel("分店")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 所有資料都被畫圖
df_trend.plot(
    x="分店",
    y="營收",
    kind="bar",
    figsize=(10, 6),
    color=["skyblue", "lightgreen"]
    )
plt.ylabel("營收")
plt.xlabel("分店")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()



print("-"*50)
import pandas as pd
import numpy as np

data = {
    "訂單編號": ["1", "2", "1", "3", "4"],
    "金額": [1200, 800, 1200, np.nan, 2500],
    "狀態": ["已出貨", "處理中", "已出貨", "已出貨", "已出貨"]
}

df = pd.DataFrame(data)
print(df)
# 1. 刪除「訂單編號」重複的列
df = df.drop_duplicates()
print(df)
# 2. 將「金額」欄位的空值填補為該欄位的平均值
df["金額"] = df["金額"].fillna(df["金額"].mean())
print(df)
# 3. 篩選「金額 > 1000」且「狀態 = 已出貨」
result = df[(df["金額"] > 1000) & (df["狀態"] == "已出貨")]
print(result)

print("-"*50)
# 3. 用loc篩選「金額 > 1000」且「狀態 = 已出貨」
result = df.loc[(df["金額"] > 1000) & (df["狀態"] == "已出貨")]
print(result)


import pandas as pd
# 原始資料
sales_data = {
    "日期": ["2026-01-10", "2026-01-15", "2026-02-05", "2026-03-12"],
    "營收": [5000, 7000, 4500, 8800],
}
df_sales = pd.DataFrame(sales_data)
# 1. 將「日期」轉為 Datetime 格式
df_sales["日期"] = pd.to_datetime(df_sales["日期"])
# 2. 新增一欄「月份」
df_sales["月份"] = df_sales["日期"].dt.month
# 3. 統計並印出「各月份」的營收總和
monthly_sales = df_sales.groupby("月份")["營收"].sum()
print(monthly_sales)