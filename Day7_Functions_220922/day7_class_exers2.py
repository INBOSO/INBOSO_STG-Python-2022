# 2. Palindrome

# Write the function is_palindrome(text)
# which returns a bool True or False depending on whether the word or sentence is read equally from both sides.
# PS You can start with a one-word solution from the beginning, but the full solution will ignore whitespace and uppercase and lowercase letters.
# is_palindrome ("Alus ari i ra    sula") -> True
# is_palindrome("ABa") -> True
# is_palindrome("nava") -> False
# Python has type hints, which are not mandatory but can be used to help the developer
# type hints are like United Nations letters, they are not mandatory but they are useful


def is_palindrome(text):
    formatted_text = text.lower().replace(" ","")
    # print(f"Formatted text {formatted_text}, reversed {formatted_text[::-1]}")
    return formatted_text == formatted_text[::-1]

print(is_palindrome("Alus ari i ra    sula") )
print(is_palindrome("ABa") )
print(is_palindrome("nava"))







# def is_palindrome (text):
#     result="False"
#     if text.upper().replace(" ", "") == text[::-1].upper().replace(" ", "") : result="True"
#     return result

# print(is_palindrome ("Alus ari i ra    sula") )
# print(is_palindrome("ABa") )
# print(is_palindrome("nava"))