import pandas as pd
import webview
import numpy as np


data = {
    "訂單編號": ["A01", "A02", "A01", "A03", "A04", "A05"],
    "品名": ["美式咖啡", "拿鐵咖啡", "美式咖啡", "卡布奇諾", None, "焦糖瑪奇朵"],
    "數量": [2, 1, 2, np.nan, 1, 3],
    "金額": [160, 120, 160, 120, 150, np.nan]
}

df = pd.DataFrame(data)

print("--- 原始髒資料 ---")
print(df)
print()


# ==============================
# 1. 刪除重複
# ==============================

print(f"\n是否有重複資料：\n{df.duplicated()}")

df_clean = df.drop_duplicates()

print("\n--- 刪除重複後 ---")
print(df_clean)
print()


# ==============================
# 2. 補上缺失
# ==============================

df_clean["品名"] = df_clean["品名"].fillna("未分類")

median_quantity = df_clean["數量"].median()

df_clean["數量"] = df_clean["數量"].fillna(median_quantity)

avg_price = df_clean["金額"].mean()

df_clean["金額"] = df_clean["金額"].fillna(avg_price)

print("--- 補上缺失後 ---")
print(df_clean)


# ==============================
# 3. DataFrame → HTML
# ==============================

html_original = df.to_html(
    index=False,
    classes="paleBlueRows"
)

html_no_duplicates = df.drop_duplicates().to_html(
    index=False,
    classes="paleBlueRows"
)

html_completed = df_clean.to_html(
    index=False,
    classes="paleBlueRows"
)


# ==============================
# 4. HTML
# ==============================

html = f"""
<!DOCTYPE html>

<html lang="zh-TW">

<head>

<meta charset="UTF-8">

<title>Pandas 資料清理</title>

<style>

body {{
    font-family: "Microsoft JhengHei", Arial;
    text-align: center;
    background-color: #f5f7fa;
    padding: 30px;
}}

h1 {{
    color: #333333;
}}

h2 {{
    margin-top: 30px;
}}

table.paleBlueRows {{
    margin: auto;
    font-family: "Microsoft JhengHei", Arial;
    border: 1px solid #FFFFFF;
    width: 600px;
    text-align: center;
    border-collapse: collapse;
    background-color: white;
}}

table.paleBlueRows td,
table.paleBlueRows th {{
    border: 1px solid #FFFFFF;
    padding: 8px;
}}

table.paleBlueRows tbody td {{
    font-size: 15px;
}}

table.paleBlueRows tr:nth-child(even) {{
    background: #D0E4F5;
}}

table.paleBlueRows thead {{
    background: #0B6FA4;
    border-bottom: 5px solid #FFFFFF;
}}

table.paleBlueRows thead th {{
    font-size: 17px;
    font-weight: bold;
    color: #FFFFFF;
}}

.section {{
    margin-bottom: 40px;
}}

</style>

</head>


<body>

<h1>Pandas 資料清理</h1>


<div class="section">

<h2>① 原始髒資料</h2>

{html_original}

</div>


<div class="section">

<h2>② 刪除重複後</h2>

{html_no_duplicates}

</div>


<div class="section">

<h2>③ 補上缺失後</h2>

{html_completed}

</div>


</body>

</html>
"""


# ==============================
# 5. WebView 顯示
# ==============================

webview.create_window(
    "DataFrame 表格",
    html=html,
    width=800,
    height=800
)

webview.start()