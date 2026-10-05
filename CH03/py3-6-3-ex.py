import matplotlib.pyplot as plt
import pandas as pd


plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
# 模擬連鎖店銷售明細
data = {
    "區域": ["北區", "北區", "中區", "南區", "北區", "中區"],
    "店名": ["台北店", "新北店", "台中店", "高雄店", "台北店", "台中店"],
    "廣告費":[1000, 600, 900, 1200, 1040, 960], 
    "營收": [5000, 3000, 4500, 6000, 5200, 4800],
    "客數": [50, 40, 45, 70, 55, 50],
    "消費金額":[3500, 2500, 3200, 4500, 3600, 3300], 
}

df = pd.DataFrame(data)

# 任務：計算每個「區域」的「營收總和」與「平均每客單價」
summary = df.groupby("區域").agg({
    "營收": ["sum", "mean", "max", "min"],
    "客數": ["sum", "mean"]
})

print("--- 區域營收摘要 ---")
print(summary)

summary.to_csv("daily_report.csv", encoding="utf-8-sig")
summary.to_excel("daily_report.xlsx", sheet_name="4月銷售")






# 長條圖
def bar_chart():
  df.plot(
      x="區域",
      y="營收",
      kind="bar",
      title="各區域營收"
  )

  plt.ylabel("營收")
  plt.show()


# 圓餅圖
def pie_chart():
  df.groupby("區域")["營收"].sum().plot(
      kind="pie",
      autopct="%1.1f%%",
      title="各區域營收占比"
  )

  plt.ylabel("")
  plt.show()

#散佈圖 
def scatter_plot():
  df.plot(
      x="廣告費",
      y="營收",
      kind="scatter",
      title="廣告費與營收關係"
  )

  plt.show()


# 直方圖
def histogram_plot():
  df["消費金額"].plot(
      kind="hist",
      bins=10,
      title="客戶消費金額分布"
  )

  plt.xlabel("消費金額")
  plt.show()

  print("完成")
  
#折線圖
def line_chart():
  df.groupby("區域")["營收"].sum().plot(
      kind="line",
      title="各區域營收趨勢"
  )

  plt.ylabel("營收")
  plt.show() 


import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
# tk.Label(root, text="身高(cm)", font=("微軟正黑體", 16)).grid(row=0, column=0, padx = (10, 0), pady=(10,0), sticky="W")
# tk.Label(root, text="體重(kg)", font=("微軟正黑體", 16)).grid(row=1, column=0, padx = (10, 0), pady=(10,0), sticky="W")
# result = tk.Label(root, text="結果", font=("微軟正黑體", 16), width= 25)
# result.grid(row=3, column=0, columnspan=2, padx = (10, 0), pady=(10,0))
# entry1 = tk.Entry(root, font=("微軟正黑體", 16))
# entry2 = tk.Entry(root, font=("微軟正黑體", 16))
# entry1.grid(row=0, column=1, padx = (10, 0), pady=(10,0), sticky="W")
# entry2.grid(row=1, column=1, padx = (10, 0), pady=(10,0), sticky="W")
button1 = tk.Button(root, text="長條圖", font=("微軟正黑體", 16), width= 25, command=bar_chart)
button1.pack(pady=(10,0))
button2 = tk.Button(root, text="圓餅圖", font=("微軟正黑體", 16), width= 25, command=pie_chart)
button2.pack(pady=(10,0))
button3 = tk.Button(root, text="散佈圖", font=("微軟正黑體", 16), width= 25, command=scatter_plot)
button3.pack(pady=(10,0))
button4 = tk.Button(root, text="直方圖", font=("微軟正黑體", 16), width= 25, command=histogram_plot)
button4.pack(pady=(10,0))
button5 = tk.Button(root, text="折線圖", font=("微軟正黑體", 16), width= 25, command=line_chart)
button5.pack(pady=(10,0))
root.mainloop()
