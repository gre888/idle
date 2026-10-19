from bs4 import BeautifulSoup

html = """
<div id="content">
    <h1 class="title">今日熱門商品</h1>
    <ul class="item-list">
      <div class="item-group">
        <li class="item hot">iPhone 15</li>
        <li class="item">PS5 Slim</li>
        <li class="item hot">RTX 4090</li>
      </div>
    </ul>
    <p id="footer">最後更新：2026-04-22</p>
</div>
"""
soup = BeautifulSoup(html, 'html.parser')

title=soup.select("#content h1.title")
print(f"標題文字：{title[0].text}")


list_items = soup.select("li")
for item in list_items:
    print(f"商品列表項目：{item.text}")
    
    
title=soup.select('#content h1') 
print(f"標題文字：{title[0].text}")


list_items = soup.select("ul.item-list li.item > li")
for li in list_items:
    print(f"商品列表項目：{li.text}")
    



