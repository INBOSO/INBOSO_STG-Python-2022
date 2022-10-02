# # 1. Confusion

# # The user enters a name.

# # You print user name in reverse (should begin with capital letter)
# # then extra text: ",a thorough mess is it not ", then the first name of the user name then "?"

# # Example:

# # Enter: Valdis -> Output: Sidlav, a thorough mess is it not V?

original_name=input("What is Your name? ")
reversed_name=original_name[::-1].capitalize()
print(f"Nice to meet you {reversed_name}")
# print(original_name[-1:].upper.repla)