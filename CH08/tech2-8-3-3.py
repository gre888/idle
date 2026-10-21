from bs4 import BeautifulSoup
html = """
<div class="content">
    <span> 第一段 </span>
    <span> 第二段 </span>
</div>
"""
soup = BeautifulSoup(html, 'html.parser')
content = soup.select_one(".content")

print(content)
print(content.get_text( separator="|",strip=True ))

