 # 1. What's the frequency?
# Write a function: get_char_count(text) that receives a string and returns a dictionary with the number of single letter counts.
# get_char_count("hubba bubba") -> {'h': 1, 'u': 2, 'b': 5, 'a': 2, ' ': 1} 
# # dictionary sequence doesn't matter and the whole alphabet doesn't have to be included
#  There may also be a solution with Counter from standard Python library but this is definitely not necessary, although it is very elegant smile

#1
def get_char_count(text):
    
    return {x: text.count(x) for x in text}

print (get_char_count("hubba bubba"))


#2
def get_char_count(text):
    counted = {}
    for c in text: # just a single loop
        if c in counted:
            counted[c] += 1 # this is constant time operation
        else:
            counted[c] = 1 # this is constant time operation
    return counted

print(get_char_count("hubba bubba"))
