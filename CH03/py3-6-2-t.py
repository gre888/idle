import matplotlib.pyplot as plt
import pandas as pd


plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
# 模擬連鎖店銷售明細
data = {
    "區域": ["北區", "北區", "中區", "南區", "北區", "中區"],
    "店名": ["台北店", "新北店", "台中店", "高雄店", "台北店", "台中店"],
    "廣告費":[1000, 600, 900, 1200, 1040, 960], 
    "營收": [5000, 3000, 4500, 6000, 5200, 4800],
    "客數": [50, 40, 45, 70, 55, 50],
    "消費金額":[3500, 2500, 3200, 4500, 3600, 3300], 
}
df = pd.DataFrame(data)

# 任務：計算每個「區域」的「營收總和」與「平均每客單價」
summary = df.groupby("區域").agg({
    "營收": ["sum", "mean", "max", "min"],
    "客數": ["sum", "mean"]
})

print("--- 區域營收摘要 ---")
print(summary)

summary.to_csv("daily_report.csv", encoding="utf-8-sig")

summary.to_excel("daily_report.xlsx", sheet_name="4月銷售")


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

print("完成")




