# # 2. Cubes

# The user enters the beginning (integer) and end number.
# The output is the entered numbers and their cubes
# For example: inputs 2 and 5 (two inputs)
# Output
# 2 cubed: 8
# 3 cubed: 27
# 4 cubed: 64
# 5 cubed: 125

# All cubes: [8,27,64,125]

# PS could theoretically do without a list, but with a list it will be more convenient

start_num = int(input("please enter start number "))
stop_num = int(input("please enter the end number "))
num_range = range(start_num,stop_num+1)
num_list = list(num_range)

print(num_list)

also_squared= [num**2 for num in num_list]
print(also_squared)
# for num in my_list:


