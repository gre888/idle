import re


# result = re.findall(r".","this is a sample text with several words.")
# print(result)

# result=re.findall(r"[^at]","this is a sample text with several words.")
# print(result)

# result=re.findall(r'.*',"this is a sample text with several words.")
# print(result)

# result=re.findall(r'(text)',"this is a sample text with several words.") 
# print(result)




###無論用 search 還是 findall 都可以取得身分證資訊

# id_text="我的身分證字號是A123456789"

# result = re.findall(r'([A-Z])([12])\d{8}', id_text)
# print(result)
# print("縣市代號",result[0][0] if result else None) #[]顯找list []找tuple,因為findall回傳list of tuple[('A','1','23456789')]
# print("性別代號",result[0][1] if result else None)
# print("身分證號碼",result[0][2] if result else None)
# print("完整結果","".join(result[0]) if result else None) #"".join 串接result list的index0 內的tuple元素
# print()

# match = re.search(r'([A-Z])([12])\d{8}', id_text)
# if match:
#   print(match.group(1))
#   print(match.group(2))
#   print(match.group(3))
#   print("完整結果", match.group(0))
# else:
#   print("No match found")
  
  
  
# match = re.search(r'(([A-Z])([12])\d{8})', id_text)
# if match:
#   print("完整結果", match.group(1))
#   print(match.group(2))
#   print(match.group(3))
#   print(match.group(4))
#   print("完整結果", match.group(0)) #無論有無小掛號包住全部 =巢狀=群組,group(0)都有用

# else:
#   print("No match found")

#6-1-1
# import http.client  
# url="https://zh.wikipedia.org/wiki/Python"
# conn = http.client.HTTPSConnection("zh.wikipedia.org")  
# conn.request("GET", "/wiki/Python")
# response = conn.getresponse()
# print("狀態",response.status, "原因", response.reason)
# html_raw = response.read().decode("utf-8")
# print(html_raw)

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