from bs4 import BeautifulSoup

html = """
<div class="category">
    <h3>水果</h3>
    <ul>
        <li>蘋果</li><li>香蕉</li>
    </ul>
</div>
<div class="category">
    <h3>蔬菜</h3>
    <ul>
        <li>青江菜</li><li>高麗菜</li>
    </ul>
</div>
"""
soup = BeautifulSoup(html, 'html.parser')
cats = soup.select(".category")

category_map = {}
for c in cats:
    cat_name = c.select_one("h3").text
    
    # 抓取該分類容器下的所有 li
    # 使用列表生成式 (List Comprehensions) 快速提取文字
    items = [li.text for li in c.select("ul li")]
    
    category_map[cat_name] = items

print(category_map)
