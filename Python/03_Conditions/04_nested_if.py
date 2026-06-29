# ------------------------------
# 04. Nested If
# ------------------------------

age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to Vote")
    else:
        print("Not a Citizen")
else:
    print("Not Eligible")