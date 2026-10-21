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







# html_with_links = """
# <div class="menu">
#     <a href="/news">新聞</a>
#     <a href="https://google.com" target="_blank">外部連結</a>
#     <a href="/about">關於我們</a>
# </div>
# """
# soup = BeautifulSoup(html_with_links, 'html.parser')


#find 與 select_one 的差異  
tag_li=soup.find('li', class_='item hot')
print(tag_li)


tag_li=soup.select_one('ul.item-list > li')
print(tag_li)

#如果find找不到符合條件的元素，會傳回None
#如果select_one找不到符合條件的元素，也會傳回None
target_tag=soup.find('li', class_='non-existent')
print(target_tag)

target_tag=soup.select_one('li.non-existent')
print(target_tag)

target_tag=soup.find('li', class_='item hot')
print(target_tag)

target_tag=soup.select_one('li.non-existent-class')
print(target_tag)


