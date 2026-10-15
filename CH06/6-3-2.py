import requests

code = input("請輸入狀態碼: ")
url = f"https://httpbin.org/status/{code}"

try:
    res = requests.get(url)
    res.raise_for_status( ) 
    print("請求成功，狀態碼:", res.status_code)
except requests.exceptions.HTTPError as err:
    print(f"連線出錯了：{err}")
