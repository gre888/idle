import re

text="分機:526,手機:0912-345-678,員編:ABC12345"

print("分機:", re.findall(r"\d{3}+", text))
print("手機:", re.findall(r"\d{4}-\d{3}-\d{3}", text))
print("員編:", re.findall(r"[A-Z]{3}\d{5}", text))

print("測試", re.findall(r"\d{3,5}+", text))

print("分機", re.findall(r"分機:(\d{3})", text))


text_split=text.split(",")
for segment in text_split:
    print("分機", re.findall(r"分機:(\d{3})", segment))