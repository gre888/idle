import requests
import time

# base_url = "https://httpbin.org/get"
base_url = "https://www.bing.com"

# res = requests.get(base_url)
# print(res.text)

for page in range(1, 4):
    params = {'page': page, 'per_page': 10}
    res = requests.get(base_url, params=params)
    print(f"正在抓取第 {page} 頁...")

    time.sleep(1) # 
