from lxml import etree

html = """
<div class="user-card">
    <span class="name">老王</span>
</div>
<div class="user-card">
    <span class="name">小李</span>
</div>
"""
tree = etree.HTML(html)
cards = tree.xpath("//div[@class='user-card']")

for card in cards:
    # 注意這裡的 .// 代表「從當前節點開始找」
    # 若沒加點，會變成從整份文件的開頭找
    name = card.xpath(".//span/text( )")
    print(f"使用者：{name[0]}")
    
    
    
for card in cards:
  # .// 代表從當前節點開始找，避免從整份文件的開頭找
  # 如果沒有加點 會從整份文件的開頭找，可能會找到不相關的節點
  # 第一圈 card是第一個 user-card 節點，第二圈 card是第二個 user-card 節點
  
  
  
    name = card.xpath(".//span/text()") #針對當前的card節點查找span的文字
    print(f"使用者：{name[0]}") #找出所有span當中第一個的文字
  