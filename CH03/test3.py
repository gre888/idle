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


# ====================================
# 1. 刪除重複資料
# ====================================

print(f"\n是否有重複資料：\n{df.duplicated()}")

df_clean = df.drop_duplicates()

print("\n--- 刪除重複後 ---")
print(df_clean)
print()


# ====================================
# 2. 補上缺失資料
# ====================================

df_clean["品名"] = df_clean["品名"].fillna("未分類")

median_quantity = df_clean["數量"].median()

df_clean["數量"] = df_clean["數量"].fillna(median_quantity)

avg_price = df_clean["金額"].mean()

df_clean["金額"] = df_clean["金額"].fillna(avg_price)

print("--- 補上缺失後 ---")
print(df_clean)


# ====================================
# 3. DataFrame → HTML table
# ====================================

# 原始資料
html_original = df.to_html(
    index=False,
    classes="paleBlueRows"
)

# 刪除重複後
html_no_duplicates = df.drop_duplicates().to_html(
    index=False,
    classes="paleBlueRows"
)

# 補上缺失後
html_completed = df_clean.to_html(
    index=False,
    classes="paleBlueRows"
)


# ====================================
# 4. HTML 網頁
# ====================================

html = f"""
<!DOCTYPE html>

<html lang="zh-TW">

<head>

    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>Pandas 資料清理</title>


    <style>

        body {{
            font-family: "Microsoft JhengHei",
                         Arial,
                         sans-serif;

            text-align: center;

            background-color: #f5f7fa;

            padding: 20px;
        }}


        h1 {{
            color: #333333;
        }}


        /* 按鈕 */

        .button-area {{
            margin: 20px;
        }}


        button {{
            padding: 10px 20px;

            margin: 5px;

            border: none;

            border-radius: 6px;

            background: #0B6FA4;

            color: white;

            font-size: 16px;

            cursor: pointer;
        }}


        button:hover {{
            background: #084f75;
        }}


        /* 表格標題 */

        .table-title {{
            font-size: 20px;

            font-weight: bold;

            margin: 20px;
        }}


        /* 表格區域預設隱藏 */

        .table-box {{
            display: none;
        }}


        /* active 才顯示 */

        .table-box.active {{
            display: block;
        }}


        /* =========================
           DataFrame 表格
           ========================= */

        table.paleBlueRows {{

            margin: auto;

            font-family:
                "Microsoft JhengHei",
                Arial,
                sans-serif;

            border: 1px solid #FFFFFF;

            width: 600px;

            text-align: center;

            border-collapse: collapse;

            background-color: white;
        }}


        table.paleBlueRows td,
        table.paleBlueRows th {{

            border: 1px solid #FFFFFF;

            padding: 8px 5px;
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

            text-align: center;

            border-left: 2px solid #FFFFFF;
        }}


        table.paleBlueRows thead th:first-child {{

            border-left: none;
        }}

    </style>

</head>


<body>


    <h1>Pandas 資料清理</h1>


    <!-- =========================
         按鈕
         ========================= -->

    <div class="button-area">

        <button onclick="showTable('original')">

            HTML 表格

        </button>


        <button onclick="showTable('duplicate')">

            刪除重複

        </button>


        <button onclick="showTable('completed')">

            補上缺失

        </button>

    </div>


    <!-- =========================
         原始資料
         ========================= -->

    <div id="original"
         class="table-box active">

        <div class="table-title">

            原始髒資料

        </div>

        {html_original}

    </div>


    <!-- =========================
         刪除重複
         ========================= -->

    <div id="duplicate"
         class="table-box">

        <div class="table-title">

            刪除重複資料後

        </div>

        {html_no_duplicates}

    </div>


    <!-- =========================
         補上缺失
         ========================= -->

    <div id="completed"
         class="table-box">

        <div class="table-title">

            補上缺失資料後

        </div>

        {html_completed}

    </div>


    <!-- =========================
         JavaScript
         ========================= -->

    <script>

        function showTable(tableName) {{

            // 找出所有表格
            const tables =
                document.querySelectorAll(".table-box");


            // 全部隱藏
            tables.forEach(function(table) {{

                table.classList.remove("active");

            }});


            // 顯示指定的表格
            document
                .getElementById(tableName)
                .classList.add("active");

        }}

    </script>


</body>

</html>
"""


# ====================================
# 5. 用 WebView 顯示
# ====================================

webview.create_window(
    "DataFrame 表格",
    html=html,
    width=800,
    height=600
)

webview.start()