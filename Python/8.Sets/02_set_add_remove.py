# ------------------------------
# 2. Add and Remove Elements
# ------------------------------

numbers = {10, 20, 30}

# Add Element

numbers.add(40)
print(numbers)

print()

# Update Multiple Elements

numbers.update([50, 60])
print(numbers)

print()

# Remove Element

numbers.remove(20)
print(numbers)

print()

# Discard Element

numbers.discard(100)   # No Error
print(numbers)

print()

# Pop Element

numbers.pop()
print(numbers)