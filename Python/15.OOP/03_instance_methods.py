# ------------------------------
# 3. Instance Method
# ------------------------------

class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name :", self.name)

obj = Student("Sam")

obj.display()