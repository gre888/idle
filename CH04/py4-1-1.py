import re



text= "我的電話號碼是 0912-345-678, ID是worker_007"

print(re.findall("\d", text))
print(re.findall("\d\d\d", text))


print("-"*50)
print(re.findall("\w","ID: user_1"))



