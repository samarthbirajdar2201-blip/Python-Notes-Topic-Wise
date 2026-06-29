# ------------------------------
# 8. String Programs
# ------------------------------

# Palindrome

text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

print()

# Iterate String

for ch in text:
    print(ch)

print()

# String Formatting

name = "Sam"
age = 21

print(f"My name is {name} and I am {age} years old.")