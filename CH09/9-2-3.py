from lxml import etree

html = """
<ul>
    <li id="id_01">項目一</li>
    <li id="id_02">項目二</li>
    <li id="id_03">項目三</li>
</ul>
"""
tree = etree.HTML(html)

# 抓取所有 li 的 id 屬性與文字
ids = tree.xpath("//li/@id")
texts = tree.xpath("//li/text( )")
print("ids",ids)
print("texts",texts)

# 使用 zip 縫合資料
for i, t in zip(ids, texts):
    print(f"編號：{i} | 內容：{t}")


count=tree.xpath("count(//li)")
print("count", count)


exists=tree.xpath("boolean(//li)")
print("exists", exists)
