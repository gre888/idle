from bs4 import BeautifulSoup
import re

# 結合BeautifulSoup與正則表達式來解析HTML內容，例如日期
html = """
<div id="content">
    <h1 class="title">今日熱門商品</h1>
    <ul class="item-list">
        <li class="item hot">iPhone 15</li>
        <li class="item">PS5 Slim</li>
        <li class="item hot">RTX 4090</li>
    </ul>
    <p id="footer">最後更新：2026-04-22</p>
</div>
"""
soup = BeautifulSoup(html, 'html.parser')

# footer = soup.find(id="footer") # 相當於 soup.select_one("#footer")
# print(footer.text)

# match = re.search(r"最後更新：(\d{4}-\d{2}-\d{2})", footer.text)
# if match:
#     print("最後更新日期（使用正則表達式）：", match.group(1))

print("所有商品：")
items = soup.select(".item")
for item in items:
    print(item.text)

print()
print("熱門商品：")    
hot_items = soup.select("li.item.hot")
for hot_item in hot_items:
    print(hot_item.text)