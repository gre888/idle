
import urllib.request
import re

# 1. 設定網址：不要使用 Markdown 的 []() 格式
url = "https://zh.wikipedia.org/zh-tw/Python"

# 2. 設定請求標頭
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/58.0.3029.110 Safari/537.3"
    )
}

# 3. 建立 Request 物件
req = urllib.request.Request(url, headers=headers)

# 4. 發送請求並取得 HTML
with urllib.request.urlopen(req, timeout=20) as response:
    html_content = response.read().decode("utf-8")
    print(html_content)

# 5. 將 HTML 儲存成檔案
with open("wikipedia_python.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML 儲存完成！")

# 6. 測試沒有換行的 HTML
html1 = """
<table><tbody><tr></table>
"""

result = re.findall(r"(<table.*?>.*?</table>)", html1)
print(result)

# 7. 測試有換行的 HTML
html2 = """
<table>
<tbody><tr>
</table>
"""

result = re.findall(
    r"(<table.*?>.*?</table>)",
    html2,
    re.DOTALL
)
print(result)
