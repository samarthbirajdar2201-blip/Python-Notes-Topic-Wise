# ------------------------------
# 1. Recursion Basics
# ------------------------------

def message(n):

    if n == 0:
        return

    print("Hello")

    message(n - 1)

message(5)