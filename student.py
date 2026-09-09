class Student():
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone
    def take_exame(self):
        print(f"{self.name} is taking the exam.")
    
    def do_homework(self):
        print(f"{self.name} is doing homework.")

def test():
  print("test()函數")
