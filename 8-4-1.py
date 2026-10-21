from bs4 import BeautifulSoup

html = """
<div class="article-list">
    <div class="post">
        <h2 class="title"><a href="/p/1">Python 入門指南</a></h2>
        <span class="meta">作者：艾倫</span>
    </div>
    <div class="post">
        <h2 class="title"><a href="/p/2">爬蟲實戰手冊</a></h2>
        <span class="meta">作者：貝拉</span>
    </div>
</div>
"""
soup = BeautifulSoup(html, 'html.parser')

# 1. 先抓取所有的「文章容器」
posts = soup.select(".post")
all_data = [ ]
for p in posts:
    # 2. 在容器 p 內部進行細部選取 (注意是使用 p.select_one)
    title_tag = p.select_one(".title a")
    author_tag = p.select_one(".meta")
    
    if title_tag and author_tag:
        data = {
            "title": title_tag.text,
            "link": title_tag.get("href"),
            "author": author_tag.text.replace("作者：", "")
        }
        all_data.append(data)

print(all_data)


