try:
	from bs4 import BeautifulSoup
except ImportError as exc:
	raise SystemExit("請先安裝 beautifulsoup4：pip install beautifulsoup4") from exc


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

html1 = """
<table>
  <tr><th>姓名</th><th>分數</th></tr>
  <tr><td>小明</td><td>95</td></tr>
</table>
"""

def show_table_data(html_text):
	soup = BeautifulSoup(html_text, "html.parser")
	table = soup.find("table")

	if table is None:
		print("No table found")
		return

	for row in table.find_all("tr"):
		cells = row.find_all(["th", "td"])
		values = [cell.get_text(strip=True) for cell in cells]
		if values:
			print(values)

show_table_data(html1)

html2 = """
<table>
	<tr><th>商品</th><th>價格</th></tr>
	<tr><td>蘋果</td><td>30</td></tr>
</table>
"""

show_table_data(html2)