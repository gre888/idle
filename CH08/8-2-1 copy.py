from bs4 import BeautifulSoup
# html = """
# <div id="content">
#     <h1 class="title">今日熱門商品</h1>
#     <ul class="item-list">
#         <li class="item hot">iPhone 15</li>
#         <li class="item">PS5 Slim</li>
#         <li class="item hot">RTX 4090</li>
#     </ul>
#     <p id="footer">最後更新：2026-04-22</p>
# </div>
# """
# soup = BeautifulSoup(html, 'html.parser')

# footer=soup.find(id="footer")
# print(footer)
# print(footer.text)

# match=re.search(r"\d{4}-\d{2}-\d{2}", footer.text)
# if match:
#     print(match.group(1))


#擷取評論範例的評論內容 評論範例.html
#取得標題
# with open("評論範例.html", "r", encoding="utf-8") as f:
#     html = f.read()
# soup = BeautifulSoup(html, 'html.parser')

# #取得標題
# title = soup.find("h3", class_="comment-item-header-title") #beautifulsoup避免跟CSS衝突
# print(title.text)

# #取得所有評論內容
# comment = soup.find("div", class_="comment-item-subItem comment-item-detail")

# for child in comment.children:
#    if child.name == "p":
#        print(f"評論內容：{child.text}")
# print(f"評論內容：{comment.p.text}")


#取得網站的所有評論內容
# # 取得網站的所有評論內容
# import requests
# url = "https://www.gu-global.com/tw/zh_TW/product-detail.html?productCode=u0000000052759"

# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# # 搜尋 HTML 中是否有評論相關文字
# for text in soup.find_all(string=lambda s: s and "喜歡錐形剪裁" in s):
#     print("找到文字：", text.strip())
#     print("所在標籤：", text.parent.name)
#     print("標籤 class：", text.parent.get("class"))


# # 取得所有評論內容
# comments = soup.find_all("div", class_="comment-item-subItem comment-item-detail")
# for comment in comments:
#     for child in comment.children:
#         if child.name == "p":
#             print(f"評論內容：{child.text}")


# # 取得網站的所有評論內容 Task2.html
with open("Task2.html", "r", encoding="utf-8") as f:
    html = f.read()
soup = BeautifulSoup(html, "html.parser")
div=soup.find("div", class_="product-detail-info-item-body comment-list")

articles=div.find_all("article", class_="comment-item")

for article in articles:
    title=article.find("h3", class_="comment-item-header-title")
    print(title.text)
    # 取得所有評論內容
    comment = article.find("div", class_="comment-item-subItem comment-item-detail")
    print(comment.text)



