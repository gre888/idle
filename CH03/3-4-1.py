
import pandas as pd
import numpy as np

data = {
    "訂單編號": ["A01", "A02", "A01", "A03", "A04", "A05"],
    "品名": ["美式咖啡", "拿鐵咖啡", "美式咖啡", "卡布奇諾", None, "焦糖瑪奇朵"],
    "數量": [2, 1, 2, np.nan, 1, 3],
    "金額": [160, 120, 160, 120, 150, np.nan]
}

df = pd.DataFrame(data)
print(df)


#duplicated 是回傳series 只要有物件就是true

# 
print(f"\n是否有重複資料:\n{df.duplicated( )}")

if df.duplicated().any():
  df_clean = df.drop_duplicates()
  print("\n--- 去除重複資料後 ---")
  print(df_clean)

df_clean['品名']=df_clean['品名'].fillna("未分類")
# 訂單可以填0 df_clean['數量']=df_clean['數量'].fillna(0)
# avg_price=df_clean['數量'].mean()   
# df_clean['數量']=df_clean['數量'].fillna(round(avg_price,0))


median_price=df_clean['數量'].median()

# df_clean['數量']=df_clean['數量'].fillna(median_price,0)

avg_price_金額=df_clean['金額'].mean() 
# df_clean['金額']=df_clean['金額'].fillna(avg_price_金額,0)





print("\n--- 去除缺失值後 ---")
print(df_clean)



import tkinter as tk
import tkinter.ttk as ttk
root = tk.Tk()
root.geometry("300x600")

data = {
    "訂單編號": ["A01", "A02", "A01", "A03", "A04", "A05"],
    "品名": ["美式咖啡", "拿鐵咖啡", "美式咖啡", "卡布奇諾", None, "焦糖瑪奇朵"],
    "數量": [2, 1, 2, np.nan, 1, 3],
    "金額": [160, 120, 160, 120, 150, np.nan]
}





import tkinter as tk
from tkinter import ttk
import pandas as pd

# ----- sample data (replace with your own) -----
data = {
    "訂單編號": ["A01", "A02", "A01", "A03", "A04", "A05"],
    "品名": ["美式咖啡", "拿鐵咖啡", "美式咖啡", "卡布奇諾", None, "焦糖瑪奇朵"],
    "數量": [2, 1, 2, np.nan, 1, 3],
    "金額": [160, 120, 160, 120, 150, np.nan]
}

df = pd.DataFrame(data)

# ----- GUI -----
root = tk.Tk()
root.title("DataFrame Duplicate Remover")
root.geometry("600x400")

# Label
tk.Label(root, text="DataFrame Preview").grid(row=0, column=0, columnspan=2, pady=5)

# Treeview
tree = ttk.Treeview(root)
tree.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)

# Scrollbars
vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
vsb.grid(row=1, column=2, sticky="ns")
tree.configure(yscrollcommand=vsb.set)

hsb = ttk.Scrollbar(root, orient="horizontal", command=tree.xview)
hsb.grid(row=2, column=0, columnspan=2, sticky="ew")
tree.configure(xscrollcommand=hsb.set)

# Result label
result = tk.Label(root, text="", fg="blue")
result.grid(row=3, column=0, columnspan=2, pady=5)

def load_dataframe(dataframe):
    """Clear Treeview and load a DataFrame into it"""
    tree.delete(*tree.get_children())          # clear old rows
    tree["columns"] = list(dataframe.columns)
    tree["show"] = "headings"

    for col in dataframe.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center")

    for _, row in dataframe.iterrows():
        tree.insert("", "end", values=list(row))

def delete_duplicates():
    global df
    if df.duplicated().any():
        before = len(df)
        df = df.drop_duplicates().reset_index(drop=True)
        after = len(df)
        load_dataframe(df)
        result.config(text=f"Removed {before - after} duplicate row(s)")
    else:
        result.config(text="沒有重複資料")

# Button
delete_button = tk.Button(root, text="刪除重複資料", command=delete_duplicates)
delete_button.grid(row=4, column=0, columnspan=2, pady=10)

# Make the Treeview expand when window is resized
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Initial load
load_dataframe(df)

root.mainloop()




# # pandas+視窗表格
# import tkinter as tk
# from tkinter import ttk
# import pandas as pd

# df = pd.DataFrame({
#     "姓名": ["小明", "小華", "小美"],
#     "年齡": [20, 25, 22],
#     "城市": ["台北", "桃園", "台中"]
# })

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
#     tree.column(col, width=120, anchor="center")

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
