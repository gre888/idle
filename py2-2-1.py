import json


raw_json_str = '{"name":"台北天氣","temp":25, "status":"晴天"}'
data = json.loads(raw_json_str)
print(type(data))
for item in data:
    print(data[item])






