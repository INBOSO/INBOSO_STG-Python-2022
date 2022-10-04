# 3. Text conversion

# Write a program for text conversion
# Save user input
# Print the entered text without changes
# Exception: if the words in the input are not .... bad, 
# then the output is not ...  bad section must be changed to is good

# Examples:
# The weather is not bad -> The weather is good
# The car is not new -> The car is not new
# This cottage cheese is not so bad -> This cottage cheese is good 

# Hints:
# Find (or index, or even rfind) will probably come in handy, as may an operator. 
# Also slice syntax will be useful.

# Extra: How would you do this task in Latvian language (nav slikts/a -> ir labs/a)?



#My solution

original_text = input("Enter your text here: ")
print(original_text)

old_text = "not bad"
new_text = "good"

# text = ['not', 'bad']
replase_text = original_text.replace(old_text, new_text)

print(replase_text)
