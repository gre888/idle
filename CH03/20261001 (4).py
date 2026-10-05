# import tkinter as tk

# def click():
#     print("發生按下事件")
#     label4['text'] = "發生按下事件"

# root = tk.Tk()

# root.geometry("600x500")

# label = tk.Label(root, text="這是我的第一個視窗")
# label2 = tk.Label(root, text="這是第二個Label")
# label3 = tk.Label(root, text="這是第三個Label")
# label4 = tk.Label(root, text="顯示結果")

# button = tk.Button(root, text="按下", width= 20, command=click)

# label.pack(pady = (20, 0)) # 上距, 下距
# label2.pack(pady = (20, 0))
# label3.pack(pady = (20, 0))
# button.pack(pady = (20, 0))
# label4.pack(pady = (20, 0))

# # padx = (a, b) # 左距=a， 右距=b

# root.mainloop()


#P3
# import tkinter as tk

# def click():
#     print("發生按下事件")
#     result['text'] = entry1.get()+entry2.get()


# root = tk.Tk()

# root.geometry("500x300")

# tk.Label(root, text="First Name").grid(row=0, column=0, padx = (10, 0), pady=(10,0))
# tk.Label(root, text="Last Name").grid(row=1, column=0, padx = (10, 0), pady=(10,0))

# result = tk.Label(root, text="Result", width= 30)
# result.grid(row=3, column=0, columnspan=2, padx = (10, 0), pady=(10,0))


# entry1 = tk.Entry(root)
# entry2 = tk.Entry(root)

# entry1.grid(row=0, column=1, padx = (10, 0), pady=(10,0))
# entry2.grid(row=1, column=1, padx = (10, 0), pady=(10,0))

# button = tk.Button(root, text="Click Me", width= 30, command=click)
# button.grid(row=2, column=0, columnspan=2, padx = (10, 0), pady=(10,0))

# root.mainloop()


# import tkinter as tk

# # 計算BMI
# def click():
#     print("發生按下事件")
#     h = float(entry1.get())/100
#     w = float(entry2.get())
#     BMI = round(w/(h*h),1)
#     print(BMI)
#     result['text'] = "BMI = "+ str(BMI)
    

# root = tk.Tk()
# root.geometry("600x400")


# tk.Label(root, text="身高(cm)", font=("微軟正黑體", 16)).grid(row=0, column=0, padx = (10, 0), pady=(10,0), sticky="W")
# tk.Label(root, text="體重(kg)", font=("微軟正黑體", 16)).grid(row=1, column=0, padx = (10, 0), pady=(10,0), sticky="W")

# result = tk.Label(root, text="結果", font=("微軟正黑體", 16), width= 25)
# result.grid(row=3, column=0, columnspan=2, padx = (10, 0), pady=(10,0))


# entry1 = tk.Entry(root, font=("微軟正黑體", 16))
# entry2 = tk.Entry(root, font=("微軟正黑體", 16))

# entry1.grid(row=0, column=1, padx = (10, 0), pady=(10,0), sticky="W")
# entry2.grid(row=1, column=1, padx = (10, 0), pady=(10,0), sticky="W")

# button = tk.Button(root, text="計算", font=("微軟正黑體", 16), width= 25, command=click)
# button.grid(row=2, column=0, columnspan=2, padx = (10, 0), pady=(10,0))

# root.mainloop()


# pandas+視窗表格
# import tkinter as tk
# from tkinter import ttk
# import pandas as pd

# df = pd.DataFrame({
#     "姓名": ["小明", "小華", "小美"],
#     "年齡": [20, 25, 22],
#     "城市": ["台北", "桃園", "台中"]
# })

# print(df.columns)

# root = tk.Tk()
# root.geometry("500x300")

# # Treeview
# tree = ttk.Treeview(
#     root,
#     columns=list(df.columns),
#     show="headings"
# )

# # 建立欄位
# for col in df.columns:
#     tree.heading(col, text=col)
#     tree.column(col, width=80, anchor="center")

# # 填入 DataFrame
# for _, row in df.iterrows():
#     tree.insert("", "end", values=list(row))

# # 垂直捲軸
# scrollbar = ttk.Scrollbar(
#     root,
#     orient="vertical",
#     command=tree.yview
# )

# tree.configure(yscrollcommand=scrollbar.set)

# tree.pack(side="left", fill="both", expand=True)
# scrollbar.pack(side="right", fill="y")

# root.mainloop()

# # 自訂完整 HTML + webview
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
print("列數",len(df))
print("列數",df.shape[0])
print("行數",df.shape[1])
print("總元素個數", df.size)


# 1. 
print(f"\n是否有重複資料：\n{df.duplicated( )}")

if df.duplicated( ).any():
    df_clean = df.drop_duplicates()
    print(df_clean)

print()
df_clean['品名'] = df_clean['品名'].fillna("未分類")

# avg_price = df_clean['數量'].mean() # 平均數
# df_clean['數量'] = df_clean['數量'].fillna(round(avg_price, 0))

median_quantity = df_clean['數量'].median() # 中位數
df_clean['數量'] = df_clean['數量'].fillna(median_quantity)

avg_price = df_clean['金額'].mean()
df_clean['金額'] = df_clean['金額'].fillna(avg_price)

print(df_clean)






# DataFrame → HTML table
table_html = df.to_html(
    index=False,
    classes="paleBlueRows"
)

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



html =  f"""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    https://divtable.com/table-styler/

    <style>
        table.paleBlueRows {{
            font-family: "Times New Roman", Times, serif;
            border: 1px solid #FFFFFF;
            width: 350px;
            height: 200px;
            text-align: center;
            border-collapse: collapse;
        }}

        table.paleBlueRows td,
        table.paleBlueRows th {{
            border: 1px solid #FFFFFF;
            padding: 3px 2px;
        }}

        table.paleBlueRows tbody td {{
            font-size: 13px;
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

        table.paleBlueRows tfoot {{
            font-size: 14px;
            font-weight: bold;
            color: #333333;
            background: #D0E4F5;
            border-top: 3px solid #444444;
        }}

        table.paleBlueRows tfoot td {{
            font-size: 14px;
        }}
    </style>


</head>

<body>
    

    {html_original}
    {html_no_duplicates}
    {html_completed}
    
    
    
    
</body>

</html>
"""


webview.create_window(
    "DataFrame 表格",
    html=html,
    width=600,
    height=400
)

webview.start()


