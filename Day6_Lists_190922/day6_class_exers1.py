# 1a. Average value

# Write a program that prompts the user to enter numbers (float).

# The program shows the average value of all entered numbers after each entry.
# PS. 1a can do without a list

# 1b. The program shows both the average value of the numbers and ALL the numbers entered

# PS Exit the program  by entering "q"

# 1c The program does not show all the numbers entered but only TOP3 and BOTTOM3 and of course still average.

number_list = []
while True:
    numbers = input("please enter numbers: ")
    if numbers == "q":
        print("Quitting time!")
        break
    number_list.append(float(numbers))
    number_avg = round((sum(number_list) / len(number_list)),2)
    print(f"Average result of {number_list} is {number_avg} ")
#  print("All numbers", number_list)




