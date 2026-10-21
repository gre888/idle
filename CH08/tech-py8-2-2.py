# from bs4 import BeautifulSoup

# html = """
# <div id="content">
#     <h1 class="title">今日熱門商品</h1>
#     <ul class="item-list">
#         <div>
#             <li class="item hot">iPhone 15</li>
#             <li class="item">PS5 Slim</li>
#             <li class="item hot">RTX 4090</li>
#         </div>
#     </ul>
#     <p id="footer">最後更新：2026-04-22</p>
# </div>
# """
# soup = BeautifulSoup(html, 'html.parser')

# # 解析方式1
# title = soup.select('h1')
# print("主標題：", title[0].text)

# list_items = soup.select('li')
# for item in list_items:
#     print(item.text)

# print()
# # 解析方式2
# title = soup.select('#content h1')
# print("主標題：", title[0].text)

# list_items = soup.select('ul.item-list > li')
# for item in list_items:
#     print(item.text)

# 無法找到任何li，因為ul.item-list的直接子元素不是li，而是div
# list_items = soup.select('ul.item-list > li')
# for item in list_items:
#     print(item.text)
    

from bs4 import BeautifulSoup    
html = """
<div id="content">
    <h1 class="title">今日熱門商品</h1>
    <ul class="item-list">
        <div>
            <li class="item hot">iPhone 15</li>
            <li class="item">PS5 Slim</li>
            <li class="item hot">RTX 4090</li>
        </div>
    </ul>
    <p id="footer">最後更新：2026-04-22</p>
</div>
"""

soup = BeautifulSoup(html, 'html.parser')
# tag_all_li=soup.select('ul.item-list li')
# print(tag_all_li)

# list_all_li=soup.find("ul")
# print(list(list_all_li.children))

tag_li=soup.select_one('ul.item-list li')
print(tag_li.find_next_sibling())


# list_tag=soup.find("ul")
# print(list(list_tag.children))
