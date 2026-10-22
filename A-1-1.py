
import urllib.parse
import requests
from lxml import html
import time


def generate_search_url(base_url, keyword):
    # 將中文字轉換為 URL 編碼
    encoded_keyword = urllib.parse.quote(keyword)
    return f"{base_url}/search?p={encoded_keyword}"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/91.0.4472.124 Safari/537.36"
}

# 實測
yahoo_base = "https://tw.news.yahoo.com"
my_keyword = "颱風"

url = generate_search_url(yahoo_base, my_keyword)
print(f"生成的網址：{url}")

time.sleep(10)

response = requests.get(url, headers=headers, timeout=15)
print(f"回應狀態碼：{response.status_code}")
print(f"回應內容：{response.text[:200]}")

# 使用 XPath 解析 HTML
tree = html.fromstring(response.text)

# 列出網頁中所有 h1、h2、h3 標籤
titles = tree.xpath("//h1 | //h2 | //h3")

print("\n網頁標題：")
for title in titles[:10]:
    text = "".join(title.xpath(".//text()")).strip()
    if text:
        print(text)

# 抓取所有具有 href 的連結
links = tree.xpath("//a[@href]")

print(f"\n找到的連結數量：{len(links)}")
print("前五個連結：")

for link in links[:5]:
    text = "".join(link.xpath(".//text()")).strip()
    href = link.get("href")

    if text and href:
        print(f"{text} - {href}")
