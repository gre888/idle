
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/91.0.4472.124 Safari/537.36"
                  
}


url="https://www.thsrc.com.tw/"
response=requests.get(url, headers=headers, verify=False)
print(f"回應狀態碼：{response.status_code}")
print(f"回應內容：{response.text[:200]}")

with open("thsrc.html", "w", encoding="utf-8") as f:
    f.write(response.text)


