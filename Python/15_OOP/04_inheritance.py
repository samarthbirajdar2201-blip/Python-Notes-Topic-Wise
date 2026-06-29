# ------------------------------
# 5. Polymorphism
# ------------------------------

class Bird:

    def sound(self):
        print("Bird Chirps")

class Dog:

    def sound(self):
        print("Dog Barks")

animals = [Bird(), Dog()]

for animal in animals:
    animal.sound()