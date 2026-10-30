import matplotlib.pyplot as plt
import numpy as np
import font

font.setting()

# 模擬數據：美金指數 vs 台幣對美金匯率 (USD/TWD)
np.random.seed(42)
usd_index = np.linspace(95, 106, 30)
twd_rate = 28 + 0.35 * (usd_index - 95) + np.random.normal(0, 0.4, 30)

plt.figure(figsize=(8, 5))
plt.scatter(usd_index, twd_rate, color='#2b5c8f', alpha=0.8, edgecolors='k', s=60)

plt.title('美金指數與台幣對美金匯率關係散佈圖', fontsize=14)
plt.xlabel('美金指數 (USD Index)', fontsize=11)
plt.ylabel('台幣對美金匯率 (USD/TWD)', fontsize=11)
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
