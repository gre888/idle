from bs4 import BeautifulSoup
html_doc = """
<div class="container">
    <h1 id="title">課程清單</h1>
    <ul class="course-list">
        <li>Python 基礎</li>
        <li>網路爬蟲實戰</li>
        <li>資料分析入門</li>
    </ul>
</div>
"""

#第一步取得網頁資料requests
#建立beautifulsoup物件  背後建立DOM樹狀結構 份類好
#尋找目標標籤 (ul) 節點 也能是多個節點=元素, 全部一起叫元素,飽含標籤頭尾內容,標籤通常指起始標籤


soup = BeautifulSoup(html_doc, 'html.parser')
list_tag = soup.find("ul")
# print(f'ul父節點{list_tag}')
# print(f'ul父節點{list_tag.parent}')
# print(f'ul子節點{child}'
#子節點
print(f'ul父節點{list_tag.children}')
for child in list_tag.children:
    # print(type(child))
  if child.name:
    print(f'ul子節點{child.name},內容{child.text}')

for content in list_tag.contents:
    if content.name:
        print(f'ul子節點{content.name},內容{content.text}')
        
