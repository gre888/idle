
import json
import csv

json_data = '[{"name": "小明", "score": 85}, {"name": "小華", "score": 92}, {"name": "小美", "score": 78}]'
data = json.loads(json_data)
with open("students.csv", "w", encoding="utf-8-sig", newline="") as f:
#     fieldnames = ["姓名", "成績"]
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     for student in data: #取出字典
#         writer.writerow({
#             "姓名": student["name"],
#             "成績": student["score"]
#         })
# print("students.csv 建立完成")

    fieldnames = ["name", "score"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
print("students.csv 建立完成")


with open("students.csv", "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.reader(f)
    print(reader)  # 這裡會輸出 reader 物件，而不是實際的內容
    for row in reader:
        print(row) #取出dict

print("-"*25+"任務二"+"-"*25)
import csv
def smart_reader(file_path):
    try:
        with open(file_path, "r", encoding="utf-8-sig", newline="") as f:
            reader = csv.reader(f)
            rows = list(reader)
            print("Row count:", len(rows))
            return rows
    except FileNotFoundError:
        print("找不到檔案")
        return []
    except Exception:
        print("檔案讀取失敗")
        return []

file_path="students.csv"
smart_reader(file_path)

