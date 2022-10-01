#  2. Christmas tree 

# Ask user to enter the height of the tree 
# Then Print the tree: Ex. height == 3 
# The printout would be: 
#   * 
#  *** 
# ***** 
# Note: remember that several symbols can be # printed at once, for example: print ("" * 10 + "*" * 6)

tree_high = int(input("Please enter the 5heigh of the tree "))
star = 1

for i in range (1,tree_high+1):
    print(" "*(tree_high-i)+ "*" * star)
    star +=2 
