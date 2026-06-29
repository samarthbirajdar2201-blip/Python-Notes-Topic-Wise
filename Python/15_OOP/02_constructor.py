# ------------------------------
# 2. Constructor
# ------------------------------

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = Student("Sam", 21)

print(obj.name)
print(obj.age)