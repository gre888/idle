students = [
    {"id": "A01", "name": "Alice", "score": 85},
    {"id": "A02", "name": "Bob", "score": 92},
    {"id": "A03", "name": "Charlie", "score": 78}
]

total = 0
for student in students:
    total = total + student["score"]
average = total / len(students)
print("平均分數：", average)

search_name = input("請輸入學生姓名：")
found = False
for student in students:
    if student["name"] == search_name:
        print("學生 ID：", student["id"])
        print("學生分數：", student["score"])
        found = True
        break
if not found:
    print("查無此人")