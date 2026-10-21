from bs4 import BeautifulSoup

html = """
<div class="info">
    <p id="p1">僅有純文字</p>
    <p id="p2">文字中有 <span>子標籤</span></p>
</div>
"""
soup = BeautifulSoup(html, 'html.parser')


p=soup.select("div.info > p")
print(p)
for e in p:
    print(e.text)
    
    
    
p1=soup.select_one("#p1")
print(p1.text)

#唯一可省略的部分是 div.info > ，因為 id 已經是唯一的了
p1=soup.select_one("div.info > p#p1")
print(p1.text)


p2=soup.select_one("#p2")
print(p2.text)
print(p2.string)

p2=soup.find("p", id="p2")
text=p2.find_all(string=True, recursive=True)
print(text)
print(text[0])
print(text[1])