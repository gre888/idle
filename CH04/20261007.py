

# id="A123456789"
# converted_id="10"+id[1:]

# print(converted_id)

# sum=0
# for i in range(11):
#   if i==0 or i ==10:
#     sum=sum+int(converted_id[i])*1
#   else:
#     sum=sum+int(converted_id[i])*(10-i)

# if sum%10==0:
#     print("Valid ID")
# else:
#     print("Invalid ID")
    
    
import requests
def get_api_key():
  # with open(r"C:\Users\User\python_idle_code\idle\CH04\mykey.txt", "r") as file:
  with open("mykey.txt", "r") as file:    
    return file.read().strip()


url="https://api.openweathermap.org/data/2.5/weather?lat=24.935233711550417&lon=121.20054097912568&appid=" + get_api_key()
response=requests.get(url)
data= response.json()
print(data)

print("目前溫度:", round(data["main"]["temp"]-273.15, 1))
print("最低溫度:", round(data["main"]["temp_min"]-273.15, 1))
print("最高溫度:", round(data["main"]["temp_max"]-273.15, 1))
if data["wind"]["deg"] == 0:
    print("風向: 北風")
elif 0 < data["wind"]["deg"] < 90:
    print("風向: 東北風")
elif data["wind"]["deg"] == 90:
    print("風向: 東風")
elif 90 < data["wind"]["deg"] < 180:
    print("風向: 東南風")
elif data["wind"]["deg"] == 180:
    print("風向: 南風")
elif 180 < data["wind"]["deg"] < 270:
    print("風向: 西南風")
elif data["wind"]["deg"] == 270:
    print("風向: 西風")
else:    
    print("風向: 西北風")

