# ------------------------------
# 3. Instance Method
# ------------------------------

class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Welcome :", self.name)

obj = Student("Sam")

obj.display()      


 