##import student
from student import *

###寫法一 import student
# student.test()
# s1=student.Student("Alice", 20, "123-456-7890")
# print(s1.name)  
# print(s1.age)
# print(s1.phone)
# s1.take_exame()
# s1.do_homework()


##寫法二 from student import *
test()
s1=Student("Alice", 20, "123-456-7890")
print(s1.name)  
print(s1.age)
print(s1.phone)
s1.take_exame()
s1.do_homework()
