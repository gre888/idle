
import csv


products=[{"ID":"A001","Name":"蘋果","Price":100},{"ID":"A002","Name":"香蕉","Price":200},{"ID":"A003","Name":"西瓜","Price":300}]

# with open("products.csv", mode="a", encoding="utf-8-sig", newline='') as f:
#   writer = csv.DictWriter(f, fieldnames=["ID", "Name", "Price"])
#   writer.writeheader()
#   for item in products:
#     writer.writerow(item)
    
    
for item in products:
  with open("products.csv", mode="a", encoding="utf-8-sig", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["ID", "Name", "Price"])
    writer.writeheader()
    writer.writerow(item)
    
    
    