# ------------------------------
# 10. Global Keyword
# ------------------------------

count = 10

def update():
    global count
    count = 20

update()
print(count)