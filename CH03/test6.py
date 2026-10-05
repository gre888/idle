student = [
  {"id": "A01", "name": "Alice", "score": 85},
  {"id": "A02", "name": "Bob", "score": 92},
  {"id": "A03", "name": "Charlie", "score": 78}
]
#算出平均分數
total_score = 0 #加法運算中，任何數加上 0 都不會改變其值，所以可以用 0 作為初始值
for score in student:
    total_score += score["score"]
average_score = total_score / len(student)
print("平均分數:", average_score)

name = input("請輸入學生姓名: ")
found = False #False表示尚未找到學生,預設為尚未找到
for s in student:
    if s["name"] == name:
        ID = s["id"]
        score = s["score"]
        found = True
        print(f"ID：{ID}\n分數：{score}")
        break
else:
  print("查無此人")