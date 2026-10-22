import requests
import time

# 設定要觀測的關鍵字清單
monitoring_list = ["台股行情", "半導體產業", "永續發展"]

for kw in monitoring_list:
    print(f"🔍 正在初始化【{kw}】的新聞抓取任務...")
    # 這裡先模擬發送請求，下一節會加入實質爬取邏輯
    time.sleep(1) # 模擬網路延遲
    print(f"✅ {kw} 任務準備就緒。")
