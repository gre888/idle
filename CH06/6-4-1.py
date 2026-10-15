import requests

api_url = "https://fakestoreapi.com/products/category/electronics?limit=20"

response = requests.get(api_url)
products = response.json( ) 
for p in products:
    print(f"商品：{p['title']} | 價格：{p['price']}")
