import re


# content="活動日期有 2024-06-15 和 2024-07-20,聯絡信箱 service@google.com.tw"
# # \.沒有\會變萬用
# print("日期:", re.findall(r"\d{4}[/-]\d{1,2}[/-]\d{1,2}", content))
# print("信箱:", re.findall(r"[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content))




import requests
url="https://www.megabank.com.tw/abroad-page/silicon-valley/zh-tw/contact-us"
res=requests.get(url) 
print(res.text)



#從網頁提取所有信箱
print("信箱:", re.findall(r"[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", res.text))
# 從網頁提取電話
phone1=re.findall(r"\d{4}-\d{3}-\d{3}", res.text)
phone2=re.findall(r"\d{2}-\d{4}-\d{4}", res.text)
print("電話1:", phone1)
print("電話2:", phone2)


phone3=re.findall(r"\d{2,4}-\d{3,4}-\d{3,4}", res.text)
print("電話3:", phone3)

print("信箱:", re.findall(r"[\w._]+@[\w.-]+\.[\w]{2,}", res.text))

words=re.findall(r"[^ ]+", "Hello World!")
print("單字:", words)
words=re.findall(r"[^,]+", "Hello World!")
print("單字:", words)
words=re.findall(r"[^!]+", "Hello World!")
print("單字:", words)
