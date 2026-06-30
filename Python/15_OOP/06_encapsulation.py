# ------------------------------
# 6. Encapsulation
# ------------------------------

# Access Modifiers in Python


# 1. Public Member
# Accessible from anywhere.

class Student:
    def __init__(self):
        self.name = "Sam"

s = Student()
print(s.name)


# 2. Protected Member (_)
# Should be accessed only within the class and its child classes (by convention).

class Student:
    def __init__(self):
        self._name = "Sam"

s = Student()
print(s._name)


# 3. Private Member (__)
# Cannot be accessed directly outside the class.

class Student:
    def __init__(self):
        self.__name = "Sam"

    def show(self):
        print(self.__name)

s = Student()
s.show()


# Example of Encapsulation
class Bank:

    def __init__(self):
        self.__balance = 5000

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("Balance:", self.__balance)

b = Bank()

b.deposit(2000)
b.show_balance()