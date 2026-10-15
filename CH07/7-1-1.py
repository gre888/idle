import requests

url = "https://httpbin.org/get"
# 準備參數字典
payload = {
    "keyword": "python 爬蟲",
    "page": 5,
    "sort": "desc"
}

# 使用 params 參數
res = requests.get(url, params=payload)

print(f"最終請求的網址：{res.url}")
# 輸出會自動變成：https://httpbin.org/get?keyword=python+%E7%88%AC%E8%9F%B2&page=5&sort=desc
