import json
import csv

file="3-1-6.json"
with open(file, "r", encoding="utf-8") as f:
    data = json.load(f)
    print(data)



with open("3-1-6.csv", mode="w", encoding="utf-8-sig",newline="") as f:
  fieldnames=["title","clicks"]
  writer = csv.DictWriter(f, fieldnames=fieldnames)
  writer.writeheader()
  writer.writerows(data)
  
  
  with open("3-1-6.csv", mode="r", encoding="utf-8-sig") as f:
      reader = csv.DictReader(f)
      for row in reader:
          print(row["title"], row["clicks"])
  
  