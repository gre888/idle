import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # 設定字體


# 資料
data = {
    "區域": ["北區", "北區", "中區", "南區", "北區", "中區"],
    "店名": ["台北店", "新北店", "台中店", "高雄店", "台北店", "台中店"],
    "廣告費": [1000, 600, 900, 1200, 1040, 960],
    "營收": [5000, 3000, 4500, 6000, 5200, 4800],
    "客數": [50, 40, 45, 70, 55, 50],
    "消費金額": [3500, 2500, 3200, 4500, 3600, 3300],
}

df = pd.DataFrame(data)


# -------------------------
# Tkinter
# -------------------------

root = tk.Tk()
root.title("銷售分析")
root.geometry("800x600")


# 按鈕區
button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, fill=tk.X)


# 圖表區
chart_frame = tk.Frame(root)
chart_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


# -------------------------
# 顯示圖表的函式
# -------------------------

def bar_chart():

    # 建立 Figure 和 Axes
    fig, ax = plt.subplots(figsize=(7, 4))

    # 把圖畫到 ax
    df.plot(
        x="區域",
        y="營收",
        kind="bar",
        title="各區域營收",
        ax=ax
    )

    ax.set_ylabel("營收")

    # 把 Figure 放進 Tkinter
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill=tk.BOTH,
        expand=True
    )


# -------------------------
# 按鈕
# -------------------------

button = tk.Button(
    button_frame,
    text="長條圖",
    font=("微軟正黑體", 14),
    command=bar_chart
)

button.pack(side=tk.LEFT, padx=10, pady=10)


root.mainloop()



