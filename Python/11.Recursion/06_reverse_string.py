# ------------------------------
# 6. Reverse String
# ------------------------------

def reverse(text):

    if len(text) == 0:
        return ""

    return reverse(text[1:]) + text[0]

print(reverse("Python"))