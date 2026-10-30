from lxml import etree

html = """
<div class="gallery">
    <a href="https://example.com/1">
        <img src="thumb1.jpg" alt="圖片1">
    </a>
    <a href="https://example.com/2">
        <img src="thumb2.jpg" alt="圖片2">
    </a>
</div>
"""
tree = etree.HTML(html)

# 1. 抓取所有連結
links = tree.xpath("//a/@href")
print(f"所有連結：{links}")

# 2. 抓取所有圖片的替代文字 (alt)
alts = tree.xpath("//img/@alt")
print(f"圖片描述：{alts}")
