# write a program that asks for two text inputs s1 and s2 
# you can use better names than s1 and s2

# then checks if all the characters in first string are in second string
# if they are, print All character counts in the second string
# if not, print Not all characters are in the second string
# example
# s1 = "abc"
# s2 = "abracadabra"
# output: a 5, b 2, c 1, d 1, r 2  # so do not print the empty ones

# example two
# s1 = "abc"
# s2 = "def"
# output: Not all characters are in the second string

text1 = input("enter the text ")
text2 = input("enter other text ")



for c in text1:
    letter_count = 0
    # print(c)
    for d in text2:
        # print(d)
        if c == d:
            letter_count+=1
    print(f"{c} in text was {letter_count}")