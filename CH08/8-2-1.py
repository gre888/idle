
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

footer=soup.find(id="footer")
print(footer)
print(footer.text)

match=re.search(r"\d{4}-\d{2}-\d{2}", footer.text)
if match:
    print(match.group(1))


items=soup.select("ul.item-list li.item")
for item in items:
    print(item.text)

