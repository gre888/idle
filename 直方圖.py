import matplotlib.pyplot as plt
import numpy as np
import font

font.setting()

# 模擬數據：桃園 10~80 歲上班人口數（單位：十萬人）
# 生成 1,000 筆模擬年齡樣本數據（主要集中於 25~55 歲）
np.random.seed(101)
age_data = np.random.triangular(left=10, mode=38, right=80, size=1000)

plt.figure(figsize=(9, 5))
# 設定 10~80 歲，每 10 歲為一個區間 (Bin)
bins = list(range(10, 81, 10))

# weights 用於將頻率轉換為「以十萬人為單位」
counts, edges, patches = plt.hist(
    age_data, 
    bins=bins, 
    color='#7570b3', 
    edgecolor='white', 
    weights=np.ones(len(age_data)) * 0.12  # 模擬換算權重
)

plt.title('桃園 10 歲 ~ 80 歲上班人口年齡分佈直方圖', fontsize=14)
plt.xlabel('年齡區間 (歲)', fontsize=11)
plt.ylabel('人口數 (十萬人)', fontsize=11)
plt.xticks(bins)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
