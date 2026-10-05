import re
test_str = "apple,apple, appleee, aple, ae, color, colour"

print(re.findall("ap+", test_str))
print(re.findall("ap+le", test_str))
print(re.findall("ap*le", "ale,aple,appple"))