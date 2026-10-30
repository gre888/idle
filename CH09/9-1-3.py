from lxml import etree

html = """<div>
          <section>
              <article>
                <ul>
                  <li>目標項目</li>
                </ul>
              </article>
          </section>
        </div>
        """
tree = etree.HTML(html)

# 不管中間有多少層，直接找 div 下面的 li
# // 代表中間可以隔著任何標籤
target = tree.xpath("//div//article//li/text( )")
print(f"抓到的文字：{target[0]}")

target = tree.xpath("//div//li/text( )")
print(f"抓到的文字：{target[0]}")