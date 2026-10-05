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
plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]
file_name = "3-6-task2.csv"
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



#所有資料都被畫圖
# df_trend.plot(
#     x="分店",
#     y="營收",
#     kind="bar",
#     figsize=(10, 6),
#     color=["skyblue", "lightgreen"]
#     )


plt.ylabel("營收")
plt.xlabel("分店")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


