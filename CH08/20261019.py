import requests
from bs4 import BeautifulSoup

url = "http://example.com"
response = requests.get(url)
html_doc = response.text
print(html_doc)

soup = BeautifulSoup(html_doc, 'html.parser')
list_tag = soup.find("ul")
if list_tag is None:
    print("找不到 ul 標籤")
else:
    for child in list_tag.children:
        if child.name:
            print(f'ul子節點{child.name},內容{child.text}')