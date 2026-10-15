
import pandas as pd
import numpy as np

data = {
    "訂單編號": ["1", "2", "1", "3", "4"],
    "金額": [1200, 800, 1200, np.nan, 2500],
    "狀態": ["已出貨", "處理中", "已出貨", "已出貨", "已出貨"]
}

df = pd.DataFrame(data)

# 1. 刪除訂單編號重複的列
df = df.drop_duplicates(subset=["訂單編號"])

# 2. 將金額空值補成平均值
df["金額"] = df["金額"].fillna(df["金額"].mean())

# 3. 篩選金額 > 1000 且狀態為已出貨
result = df[
    (df["金額"] > 1000) &
    (df["狀態"] == "已出貨")
]

print(result)
