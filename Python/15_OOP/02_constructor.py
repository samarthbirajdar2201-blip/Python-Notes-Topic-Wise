# ------------------------------
# 2. Constructor
# ------------------------------

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self)

obj = Student("Sam", 21)

print(obj.name)
print(obj.age)                                    