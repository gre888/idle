from bs4 import BeautifulSoup


html = "<html><body><div><p><b id='target'>標籤文字</b></p></div></body></html>"
soup = BeautifulSoup(html, 'html.parser')
target_tag = soup.find(id='target')
b_tag = soup.find(id='target')
# 使用 .parents 迭代器會從最近的父層一路往上找到 html

soup = BeautifulSoup(html, 'html.parser')
target_tag = soup.find(id='target')
print(target_tag)
for parent in b_tag.parents:
    if parent is not None:
        print(f"上層標籤有：{parent.name}")
        
for parent in target_tag.parents:
    if parent is not None:
        print(f"target_tag 的上層標籤有：{parent.name}")



    