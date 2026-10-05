import pandas as pd

data = {
    "交易時間": ["2026/01/05 10:30", "2026/01/20 14:00", "2026/02/10 09:15", "2026/02/15 16:45", "2026/03/01 11:00"],
    "金額": [150, 200, 120, 350, 400]
}

df = pd.DataFrame(data)
print("--- 原始資料 (交易時間目前是字串) ---")
print("轉換之前",df.dtypes)


df['交易時間'] = pd.to_datetime(df['交易時間'])
print("轉換之後",df.dtypes)
print(df)


df['年'] = df['交易時間'].dt.year
df['月'] = df['交易時間'].dt.month
df['日'] = df['交易時間'].dt.day
df['星期'] = df['交易時間'].dt.day_name()

print(df[['交易時間','月','星期','金額']])

print("-"*50)
monthly_revenue=df.groupby('月')['金額'].sum()
print(monthly_revenue)

print("-"*50)
weekly_revenue=df.groupby('星期')['金額'].sum()
print("星期營收",weekly_revenue)


filter_data=df[df["交易時間"]>="2026-03-01"]
print("三月訂單")
print(filter_data)


filter_data=df[df["月"]==3]
print("三月訂單")
print(filter_data)

