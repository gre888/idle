import json
import csv



json_data='[{"姓名":"小明","成績":85},{"姓名":"小華","成績":92},{"姓名":"小美","成績":78}]'

data = json.loads(json_data)
print(data)

with open('students.csv', 'w', encoding='utf-8-sig', newline='') as f:
  field_name=['姓名', '成績']
  writer = csv.DictWriter(f, fieldnames=field_name)
  writer.writeheader()
  writer.writerows(data)
  