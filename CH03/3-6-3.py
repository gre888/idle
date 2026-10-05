import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']


data = {
    "區域": ["北區", "北區", "中區", "南區", "北區", "中區"],
    "店名": ["台北店", "新北店", "台中店", "高雄店", "台北店", "台中店"],
    "營收": [5000, 3000, 4500, 6000, 5200, 4800],
    "客數": [50, 40, 45, 70, 55, 50]
}
df = pd.DataFrame(data)




trend_data = {
    "日期": pd.to_datetime(["2026-04-06", "2026-04-07", "2026-04-08", "2026-04-09", "2026-04-10"]),
    "業績": [12000, 15000, 11000, 18000, 22000]
}
df_trend = pd.DataFrame(trend_data)
# 開始畫圖
df_trend.plot(x="日期", y="業績", kind="line", marker='o', title="本週業績趨勢圖")
plt.ylabel("新台幣")
plt.grid(True)
plt.show( ) 


# 長條圖
df.plot(
    x="區域",
    y="營收",
    kind="bar",
    title="各區域營收"
)

plt.ylabel("營收")
plt.show()


# 圓餅圖
df.groupby("區域")["營收"].sum().plot(
    kind="pie",
    autopct="%1.1f%%",
    title="各區域營收占比"
)

plt.ylabel("")
plt.show()

#散佈圖 
df.plot(
    x="廣告費",
    y="營收",
    kind="scatter",
    title="廣告費與營收關係"
)

plt.show()



# 直方圖
df["消費金額"].plot(
    kind="hist",
    bins=10,
    title="客戶消費金額分布"
)

plt.xlabel("消費金額")
plt.show()