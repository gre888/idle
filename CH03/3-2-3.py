import pandas as pd

data = {
    "日期": ["2026-04-13", "2026-04-14", "2026-04-15","2026-04-16","2026-04-17","2026-04-20","2026-04-21",None],
    "收盤價": [810, 815, 805, 820, 825, 700, 700, None],
    "漲跌": [5, 5, -10, -5, -5, -15, 0, None]
}

df = pd.DataFrame(data)

print(df)
print()
print(df.head(2))
print()
print(df.tail(1))
print()
print(df.describe( ))

# help(df.describe)


