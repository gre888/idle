import matplotlib.pyplot as plt
import font

font.setting()

# 1. 準備數據（10年數據：2015 - 2024）
years = list(range(2015, 2025))
# 假設的淨利潤數據（單位：百萬元）
net_profit = [12.5, 15.0, 14.2, 18.8, 22.4, 20.1, 28.5, 35.0, 42.1, 50.3]

# 2. 建立圖表與設定大小
plt.figure(figsize=(10, 6))

# 3. 繪製折線圖
plt.plot(
    years, 
    net_profit, 
    color='#1f77b4',       # 線條顏色（質感藍）
    marker='o',            # 資料點形狀（圓點）
    linewidth=2.5,         # 線條寬度
    markersize=6,          # 數據點大小
    label='Net Profit'     # 圖例標籤
)

# 4. 設定圖表標題與軸標籤
plt.title('Company 10-Year Profit Growth (2015-2024)', fontsize=16, pad=15, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Net Profit ($ Millions)', fontsize=12)

# 5. 美化圖表細節
plt.xticks(years, rotation=45)        # 顯示所有年份並稍微旋轉
plt.grid(True, linestyle='--', alpha=0.5)  # 添加虛線背景網格
plt.ylim(0, 60)                        # 設定 Y 軸範圍留出適當頂部空間

# 6. 在每個點上方標示具體數值
for x, y in zip(years, net_profit):
    plt.text(x, y + 1.2, f'${y}', ha='center', va='bottom', fontsize=9)

# 7. 顯示圖例與調整版面
plt.legend(loc='upper left')
plt.tight_layout()

# 8. 顯示圖表
plt.show()
