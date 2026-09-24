import pandas as pd

data = {
    "日期": ["2026-04-13", "2026-04-14", "2026-04-15","2026-04-16","2026-04-17"],
    "收盤價": [810, 815, 805, 820, 825],
    "漲跌": [5, 5, -10, -5, -5]
}

df = pd.DataFrame(data)




print(f"資料形狀 (列, 欄): {df.shape}")
print(f"欄位名稱: {df.columns}")
print(f"資料型態: \n{df.dtypes}")
