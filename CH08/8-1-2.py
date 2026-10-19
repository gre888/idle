# import requests
# from bs4 import BeautifulSoup
# html = """
# <tr>
#     <td class="label">姓名</td>
#     <div>其他</div>
#     <td class="value">張小明</td>
#     <td class="label">職稱</td>
#     <td class="value">工程師</td>
# </tr>
# """

# soup=BeautifulSoup(html, 'html.parser')
# first_td=soup.find("td")
# print(first_td)

# # next_td = first_td.find_next_sibling("td")
# # print(next_td)

# next_td = first_td.find_next_sibling() # 找到第一個 td 的下一個兄弟節點，不指定標籤
# print(next_td)

# print("-----")
# for sibling in first_td.find_next_siblings():
#     print(sibling)
    
# print("-----")
# for i in range(3):
#   next_td = next_td.find_next_sibling()
#   print(next_td)
#   first_td = next_td

# print("-----")
# while next_td:
#     next_td = next_td.find_next_sibling()
#     if next_td is None:
#         break
#     print(next_td)

# print("-----")
# while True:
#     next_td = first_td.find_next_sibling()
#     if not next_td:
#         break
#     print(next_td)
#     first_td = next_td
    
# print("-----")
# all_td=soup.find_all("td")    
# for td in all_td:
#       print(td)

#用 BeautifulSoup 解析  表格範例.html



import requests
from bs4 import BeautifulSoup

def get_table_content(tag_name):
  with open("表格範例.html", "r", encoding="utf-8") as f:
      html_doc= f.read()
      soup = BeautifulSoup(html_doc, "html.parser")
      tag_list = soup.find_all(tag_name)
      result = []
      for tag in tag_list:
        result.append(tag.text)
      return result


list1= get_table_content("th")
list2= get_table_content("td")

print(list1)
print(list2)

#將list1 list2 轉乘dataframe
import pandas as pd
df = pd.DataFrame([list2], columns=list1)
print(df)


# import pandas as pd
# df = df=pd.DataFrame([list2], columns=list1)
# print(df)





    
# ##------------------    
# list1=["header1","header2","header3"]
# list2=["data1","data2","data3"]
# for header,data in zip(list1,list2):
#     print(f"{header}: {data}")

#   
# ###########    