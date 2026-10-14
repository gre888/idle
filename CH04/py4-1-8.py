


import re

phone_text="門牌 123號, 電話 0912345678"

print(re.findall("\d+", phone_text))

text='\w'
pattern=r"\w"
print(re.findall(pattern, text))
print(re.findall(pattern, text)[0])

print()
pattern=r"\\\w"
print(re.findall(pattern, text))
print(re.findall(pattern, text)[0])


