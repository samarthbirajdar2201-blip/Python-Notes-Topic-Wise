# ------------------------------
# 3. Remove Elements
# ------------------------------

student = {
    "Name": "Sam",
    "Age": 21,
    "City": "Pune"
}

# Remove using pop()

student.pop("Age")
print(student)

print()

# Remove last item

student.popitem()
print(student)

print()

# Clear Dictionary

student.clear()
print(student)