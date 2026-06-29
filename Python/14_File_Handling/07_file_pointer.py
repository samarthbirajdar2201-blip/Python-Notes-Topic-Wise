# ------------------------------
# 7. File Pointer
# ------------------------------

file = open("Python/14.File_Handling/_sample.txt", "r")

print(file.tell())

print(file.read(5))

print(file.tell())

file.seek(0)

print(file.read())

file.close()