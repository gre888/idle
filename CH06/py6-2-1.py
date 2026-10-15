import requests
api_url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
response = requests.get(api_url)
if response.status_code == 200:
    json_data = response.json()
    print(json_data["data"]["amount"])
else:
    print("Failed to retrieve data:", response.status_code)