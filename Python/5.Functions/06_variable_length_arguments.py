# ------------------------------
# 6. Variable Length Arguments
# ------------------------------

def total(*numbers):
    print(sum(numbers))

total(10, 20)

total(10, 20, 30, 40)