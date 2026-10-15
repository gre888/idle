import requests

url = "https://httpbin.org/headers"
headers = {
    "User-Agent": "Mozilla/5.0",
    "X-Requested-With": "XMLHttpRequest" 
}
res = requests.get(url, headers=headers)
print(res.json( )['headers'])
