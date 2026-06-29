# ------------------------------
# 8. Method Overriding
# ------------------------------

class Animal:

    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def sound(self):
        print("Dog Barks")

obj = Dog()

obj.sound()