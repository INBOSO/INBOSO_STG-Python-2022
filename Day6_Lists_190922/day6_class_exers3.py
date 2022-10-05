# 3. Reversed words

# The user enters a sentence.

# We output all the words of the sentence in a reverse form. 
# - not the whole text reversed!!

# Example

# Alus kauss mans -> Sula ssuak snam
# notice how each word was reversed separately

# PS Split and join operations could be useful here.


sentence = input("Please enter the sentence ")
word_list = sentence.split()
print(word_list)
reversed_list = list(reversed(word_list))
print(reversed_list)
new_sentence = " ".join(reversed_list)
print(new_sentence)
