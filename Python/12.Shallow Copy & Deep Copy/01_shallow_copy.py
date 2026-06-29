# ------------------------------
# 1. Shallow Copy
# ------------------------------

import copy 

list1 = [[10, 20], [30, 40]]

list2 = copy.copy(list1)

print("Original :", list1)
print("Copy     :", list2)

print()

# Modify Original List

list1[0][0] = 100

print("Original :", list1)
print("Copy     :", list2)