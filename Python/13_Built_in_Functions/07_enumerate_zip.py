# ------------------------------
# 7. enumerate() and zip()
# ------------------------------

fruits = ["Apple", "Mango", "Banana"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

print()

names = ["Sam", "Rahul", "Amit"]
marks = [90, 80, 85]

for name, mark in zip(names, marks):
    print(name, mark)