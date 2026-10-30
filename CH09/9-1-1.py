from lxml import etree
html_str = """
<html>
    <body>
        <div class="content">
            <h1 id="title">XPath 學習</h1>
            <p>第一段文字</p>
            <p>第二段文字</p>
        </div>
    </body>
</html>
"""

# 將字串轉換為 HTML 元素物件
content = etree.HTML(html_str)

# 1. 使用絕對路徑抓取 h1
title_abs = content.xpath("/html/body/div/h1")
print(f"絕對路徑結果：{title_abs[0].text}")


# 2. 使用相對路徑抓取 h1
title_rel = content.xpath("//h1")
print(f"相對路徑結果：{title_rel[0].text}")

print(title_abs[0])