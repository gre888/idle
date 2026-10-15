import requests
url = "https://httpbin.org/post"


payload = {
    "keyword": "Python課程",
    "page": 2
}

response = requests.post(url, data=payload)
if response.status_code == 200:
    json_data = response.json()
    print("伺服器收到資料",json_data["form"])
    print("伺服器收到資料",json_data["json"])   
else:
    print("Failed to send data:", response.status_code)
    
