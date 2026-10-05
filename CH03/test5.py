import pandas as pd
import webview
import numpy as np

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs


# ==========================================
# 1. 原始資料
# ==========================================

data = {
    "訂單編號": ["A01", "A02", "A01", "A03", "A04", "A05"],
    "品名": ["美式咖啡", "拿鐵咖啡", "美式咖啡", "卡布奇諾", None, "焦糖瑪奇朵"],
    "數量": [2, 1, 2, np.nan, 1, 3],
    "金額": [160, 120, 160, 120, 150, np.nan]
}

df = pd.DataFrame(data)


# ==========================================
# 2. HTML CSS
# ==========================================

css = """
<style>

body {
    font-family: "Microsoft JhengHei", Arial;
    text-align: center;
    background-color: #f5f7fa;
    padding: 30px;
}

h1 {
    color: #333333;
}

button {
    padding: 12px 25px;
    margin: 8px;
    border: none;
    border-radius: 6px;
    background-color: #0B6FA4;
    color: white;
    font-size: 16px;
    cursor: pointer;
}

button:hover {
    background-color: #084f75;
}

table.paleBlueRows {
    margin: 30px auto;
    font-family: "Microsoft JhengHei", Arial;
    border: 1px solid #FFFFFF;
    width: 600px;
    text-align: center;
    border-collapse: collapse;
    background-color: white;
}

table.paleBlueRows td,
table.paleBlueRows th {
    border: 1px solid #FFFFFF;
    padding: 8px;
}

table.paleBlueRows tbody td {
    font-size: 15px;
}

table.paleBlueRows tr:nth-child(even) {
    background: #D0E4F5;
}

table.paleBlueRows thead {
    background: #0B6FA4;
    border-bottom: 5px solid #FFFFFF;
}

table.paleBlueRows thead th {
    font-size: 17px;
    font-weight: bold;
    color: #FFFFFF;
}

</style>
"""


# ==========================================
# 3. 建立 HTML
# ==========================================

def make_html(title, table_html=""):

    return f"""
    <!DOCTYPE html>

    <html lang="zh-TW">

    <head>

        <meta charset="UTF-8">

        <title>Pandas 資料清理</title>

        {css}

    </head>

    <body>

        <h1>Pandas 資料清理</h1>


        <form method="POST">

            <button name="action" value="original">
                ① HTML 表格
            </button>

            <button name="action" value="duplicate">
                ② 刪除重複
            </button>

            <button name="action" value="missing">
                ③ 補上缺失
            </button>

        </form>


        <h2>{title}</h2>

        {table_html}

    </body>

    </html>
    """


# ==========================================
# 4. Python Web Server
# ==========================================

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        html = make_html(
            "請選擇要執行的資料清理功能"
        )

        self.send_response(200)

        self.send_header(
            "Content-type",
            "text/html; charset=utf-8"
        )

        self.end_headers()

        self.wfile.write(
            html.encode("utf-8")
        )


    def do_POST(self):

        # 取得按鈕資料

        content_length = int(
            self.headers["Content-Length"]
        )

        post_data = self.rfile.read(
            content_length
        )

        data = parse_qs(
            post_data.decode("utf-8")
        )

        action = data["action"][0]


        # ==================================
        # ① HTML 表格
        # ==================================

        if action == "original":

            print("\n--- 執行：HTML 表格 ---")

            print(df)

            table_html = df.to_html(
                index=False,
                classes="paleBlueRows"
            )

            html = make_html(
                "① 原始 HTML 表格",
                table_html
            )


        # ==================================
        # ② 刪除重複
        # ==================================

        elif action == "duplicate":

            print("\n--- 執行：刪除重複 ---")

            print(
                "是否有重複資料："
            )

            print(df.duplicated())


            df_clean = df.drop_duplicates()


            print("\n刪除重複後：")

            print(df_clean)


            table_html = df_clean.to_html(
                index=False,
                classes="paleBlueRows"
            )

            html = make_html(
                "② 刪除重複後",
                table_html
            )


        # ==================================
        # ③ 補上缺失
        # ==================================

        elif action == "missing":

            print("\n--- 執行：補上缺失 ---")


            # 先刪除重複

            df_clean = df.drop_duplicates().copy()


            # 品名

            df_clean["品名"] = (
                df_clean["品名"]
                .fillna("未分類")
            )


            # 數量 → 中位數

            median_quantity = (
                df_clean["數量"].median()
            )

            df_clean["數量"] = (
                df_clean["數量"]
                .fillna(median_quantity)
            )


            # 金額 → 平均數

            avg_price = (
                df_clean["金額"].mean()
            )

            df_clean["金額"] = (
                df_clean["金額"]
                .fillna(avg_price)
            )


            print("\n補上缺失後：")

            print(df_clean)


            table_html = df_clean.to_html(
                index=False,
                classes="paleBlueRows"
            )


            html = make_html(
                "③ 補上缺失後",
                table_html
            )


        # ==================================
        # 回傳 HTML
        # ==================================

        self.send_response(200)

        self.send_header(
            "Content-type",
            "text/html; charset=utf-8"
        )

        self.end_headers()

        self.wfile.write(
            html.encode("utf-8")
        )


# ==========================================
# 5. 啟動 Python Server
# ==========================================

server = HTTPServer(
    ("127.0.0.1", 8080),
    MyHandler
)


# ==========================================
# 6. WebView
# ==========================================

webview.create_window(
    "Pandas 資料清理",
    "http://127.0.0.1:8080",
    width=800,
    height=650
)


webview.start(
    server.serve_forever
)