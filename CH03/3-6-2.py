import pandas as pd

# 模擬連鎖店銷售明細
data = {
    "區域": ["北區", "北區", "中區", "南區", "北區", "中區"],
    "店名": ["台北店", "新北店", "台中店", "高雄店", "台北店", "台中店"],
    "營收": [5000, 3000, 4500, 6000, 5200, 4800],
    "客數": [50, 40, 45, 70, 55, 50]
}
df = pd.DataFrame(data)

# 任務：計算每個「區域」的「營收總和」與「平均每客單價」
summary = df.groupby("區域").agg({
    "營收": ["sum", "mean",'max','min'],
    "客數": ["sum", "mean", "max", "min"]
})

print("--- 區域營收摘要 ---")
print(summary)

df.to_csv("daily_report.csv", index=False, encoding="utf-8")
df.to_excel("daily_report.xlsx", index=False, sheet_name="4月銷售")


