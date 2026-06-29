# ------------------------------
# 7. Palindrome Using Recursion
# ------------------------------

def palindrome(text):

    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return palindrome(text[1:-1])

word = "madam"

if palindrome(word):
    print("Palindrome")
else:
    print("Not Palindrome")