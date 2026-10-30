import matplotlib.pyplot as plt
import font

font.setting()

# 範例數據：全球地震規模分級佔比
labels = ['< 3.0', '3.0 - 4.9', '5.0 - 6.9', '>= 7.0']
sizes = [53, 23, 14, 10]
colors = ['#4caf50', '#ffeb3b', '#ff9800', '#f44336']
explode = (0, 0, 0.1, 0.2)  # 突顯佔比較小但關鍵的強震區塊

plt.figure(figsize=(7, 7))
plt.pie(
    sizes, 
    explode=explode, 
    labels=labels, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=140,
    pctdistance=0.75,
    textprops={'fontsize': 10}
)

plt.title('全球地震規模統計佔比 (Magnitude Distribution)', fontsize=14)

plt.tight_layout()
plt.show()
