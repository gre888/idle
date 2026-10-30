import matplotlib.pyplot as plt
import font

font.setting()

# 範例數據：台股高價股（千金股）
stocks = ['信驊', '世芯-KY', '力旺', '緯穎', '祥碩', '旭隼', '川湖', '弘塑', '台積電', '聯發科']
prices = [3200, 2850, 2400, 2250, 1950, 1780, 1420, 1250, 980, 950]

plt.figure(figsize=(10, 6))
bars = plt.bar(stocks, prices, color='#d95f02', width=0.6)

# 在長條上方標示具體股價
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 30, f'{yval:,}', ha='center', va='bottom', fontsize=9)

plt.title('台股股價前十高股票排行', fontsize=14)
plt.xlabel('股票名稱', fontsize=11)
plt.ylabel('股價 (NTD)', fontsize=11)
plt.ylim(0, 3600)
plt.xticks(rotation=30)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
