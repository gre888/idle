# 任務：從維基百科的Python頁面中提取表格內容並將其換行顯示
import urllib.request
from bs4 import BeautifulSoup

url = "https://zh.wikipedia.org/zh-tw/Python"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

req = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(req) as response:
    html_content = response.read().decode("utf-8")
##    print(html_content)

soup = BeautifulSoup(html_content, "html.parser")
table = soup.find("table", class_="wikitable")

if table is None:
    print("找不到表格")
else:
    rows = []
    for row in table.find_all("tr"):
        cells = row.find_all(["th", "td"])
        values = [cell.get_text(strip=True) for cell in cells]
        if values:
            rows.append(values)

    if rows:
        column_count = max(len(row) for row in rows)
        widths = [0] * column_count

        for row in rows:
            for index, value in enumerate(row):
                widths[index] = max(widths[index], len(value))

        for row in rows:
            padded = [value.ljust(widths[index]) for index, value in enumerate(row)]
            print(" | ".join(padded))