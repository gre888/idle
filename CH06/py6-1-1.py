#6-1-1
import http.client

import urllib.request
url="https://zh.wikipedia.org/zh-tw/Python"
# conn = http.client.HTTPSConnection("zh.wikipedia.org")  
# conn.request("GET", "/wiki/Python")
# response = conn.getresponse()
# print("狀態",response.status, "原因", response.reason)
# html_raw = response.read().decode("utf-8")
# print(html_raw)

import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

req =  urllib.request.Request(url, headers=headers)


with urllib.request.urlopen(req) as response:
    html_content = response.read().decode("utf-8")
    # print(html_content)
    
tables= re.findall(r'(<table class="wikitable">.*?</table>)', html_content, re.DOTALL)
print(len(tables))
print(tables)
result=re.sub(r"(.*?>","", tables[0])
print(result.strip().replace('\n\n',''))
    
with open("wikipedia_python.html", "w", encoding="utf-8") as f:
    f.write(html_content)



import re
html1 = """
<table><tbody><tr></table>
"""
result= re.findall(r"(<table.*?>.*?</table>)",html1) #.*? 屬性非貪婪模式 .*?</table>就停下來 但是遇到\n就會停下來找不到
print(result)

html2 = """
<table>
<tbody><tr>
</table>
"""

result= re.findall(r"(<table.*?>.*?</table>)",html2, re.DOTALL) #DOTALL飽含全被和換行 .*? 屬性非貪婪模式 .*?</table>就停下來 但是遇到\n就會停下來找不到
print(result)


