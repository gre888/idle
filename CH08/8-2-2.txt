from bs4 import BeautifulSoup

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

# 1. 用 ID 選取 (#)
footer = soup.select_one("#footer")
print(f"頁尾文字：{footer.text}")

# 2. 用 Class 選取 (.)
items = soup.select(".item")
print(f"商品數量：{len(items)}")
# 3. 組合選取 (同時具備 item 和 hot 兩個 class 的 li)
hot_items = soup.select("li.item.hot")
for hi in hot_items:
    print(f"熱門商品：{hi.text}")


