# ------------------------------
# 5. Traverse Dictionary
# ------------------------------

student = {
    "Name": "Sam",
    "Age": 21,
    "City": "Pune"
}

# Print Keys

for key in student:
    print(key)

print()

# Print Values

for value in student.values():
    print(value)

print()

# Print Key and Value

for key, value in student.items():
    print(key, ":", value)