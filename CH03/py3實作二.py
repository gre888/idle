
import pandas as pd

sales_data = {
    "日期": [
        "2026-01-10",
        "2026-01-15",
        "2026-02-05",
        "2026-03-12"
    ],
    "營收": [5000, 7000, 4500, 8800]
}

df_sales = pd.DataFrame(sales_data)

# 1. 將日期轉成 Datetime 格式
df_sales["日期"] = pd.to_datetime(df_sales["日期"])

# 2. 新增月份欄位
df_sales["月份"] = df_sales["日期"].dt.month

# 3. 統計各月份營收總和
monthly_sales = df_sales.groupby("月份")["營收"].sum()

print(monthly_sales)
