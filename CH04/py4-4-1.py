import re
html_raw="<div>歡迎來到<span class='hightlight'>爬蟲課程</span></div>"
result = re.sub(r"<.*?>","",html_raw) #?問號有0次獲1次有 .*貪婪指損的意思

#提取span標籤內容 ""空字串取代不要的標籤
print(result)


#4-4-2
bad_clean = re.sub(r"<.*?>","",html_raw)

#4-4-3
result=re.sub(r"<.*?>","\n",html_raw)



