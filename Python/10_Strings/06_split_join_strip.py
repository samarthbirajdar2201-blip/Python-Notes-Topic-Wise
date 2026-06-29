# ------------------------------
# 6. Split, Join and Strip
# ------------------------------

text = "Python Java C++"

words = text.split()

print(words)

print("-".join(words))

print()

msg = "   Python   "

print(msg.strip())
print(msg.lstrip())
print(msg.rstrip())