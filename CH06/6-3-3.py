import requests

# 某些網站若不帶 User-Agent 會回傳 403
# url = "https://www.ptt.cc/bbs/index.html"
# url =  'https://zh.wikipedia.org/zh-tw/Wiki'
url = "https://www.bing.com/search?q=python%E7%94%B1%E4%BE%86"
res = requests.get(url)

if res.status_code == 403:
    print("糟了！被伺服器拒絕存取（403），可能需要偽裝 User-Agent。")
else:
    print("請求成功，狀態碼:", res.status_code)
    
    
content = res.text
print(content)
    
    
