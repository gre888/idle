import pandas as pd

# products = [
#     {"name": "咖啡機", "price": 5000, "rating": 4.8},
#     {"name": "磨豆機", "price": 1200, "rating": 4.2},
#     {"name": "濾紙", "price": 150, "rating": 4.9},
#     {"name": "保溫杯", "price": 800, "rating": 3.5}
# ]

# df1 = pd.DataFrame(products)
# print(df1)
# print()
# print(df1[(df1['rating']>4.5)&(df1['price']<=2000)])
# print("----------------------------")


df = pd.DataFrame({
    "user": [" Alice ", "Bob\n", "  Charlie  "],
    "email": ["ALICE@gmail.com", "bob@Gmail.com", "CHARLIE@outlook.com"]
})
df["user"] = df["user"].str.strip()
print(df["user"])
print()
df["email"] = df["email"].str.lower()
print(df["email"])
print()
print(df)


# s="Bob\n"
# print(s+"是一位醫生")
# print(s.strip()+"是一位醫生")

  # df1=.DataFram({"product":["iPhone","iPad"],"price":["5000","3000"]})

#print(df)
print(df["user"])
print(df["email"])