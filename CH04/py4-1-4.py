import re



text= "我的電話號碼是 0912-345-678, ID是worker_007"


print(re.findall("\w\w\w\w\w\w_\d\d\d", text))








