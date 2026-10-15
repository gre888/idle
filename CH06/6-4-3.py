import requests

def get_infinite_data(offset_limit):
    results = [ ]
    for offset in range(0, offset_limit, 10):
        url = f"https://httpbin.org/get?offset={offset}"
        res = requests.get(url)
        # results.append(res.json( )['args'])
        results.append(res.json( ))        
    return results

data = get_infinite_data(30)
print(data)
print(f"總共抓取了 {len(data)} 組封包資料")
