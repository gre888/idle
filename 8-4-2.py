from bs4 import BeautifulSoup

html = """
<div class="shop">
    <div class="product">
        <div class="name">無線耳機</div>
        <div class="price">1990</div>
        <div class="tag">新品</div>
    </div>
    <div class="product">
        <div class="name">智慧手錶</div>
        <div class="price">4500</div>
        <!-- 這個商品沒有 tag 標籤 -->
    </div>
</div>
"""
soup = BeautifulSoup(html, 'html.parser')
products = soup.select(".product")

result = [ ]
for item in products:
    name = item.select_one(".name").text
    price = item.select_one(".price").text
    
    # 判斷 tag 是否存在，避免 AttributeError
    tag_element = item.select_one(".tag")
    tag_text = tag_element.text if tag_element else "無標籤"
    
    result.append({
        "name": name, 
        "price": price, 
        "tag": tag_text
    })

print(result)
