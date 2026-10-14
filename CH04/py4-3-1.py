import re



html_data = "價格:500元,價格:1200元,價格:80元,電話:0912345678"
re_no_group = re.findall(r'價格:\d+元', html_data)
print(re_no_group)

re_with_group = re.findall(r'價格:(\d+)元', html_data) #(\d+) 是捕獲群組，只會返回數字部分
print(re_with_group)

re_with_group = re.findall(r'(\d+)', html_data) #(\d+) 是捕獲群組，只會返回數字部分
print(re_with_group)


data = "蘋果:100, 香蕉:50, 橘子:30"
items = re.findall(r'(\w+):(\d+)', data)
print(items)

