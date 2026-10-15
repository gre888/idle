import requests

url = "https://httpbin.org/get"

# 字典的值可以是列表 (List)
payload = {
    "category": ["electronics", "books"],
    "on_sale": "true"
}

res = requests.get(url, params=payload)
print(f"回應內容：{res.text}")
print(f"多值請求網址{res.url}")
# 輸出：.../get?category=electronics&category=books&on_sale=true
