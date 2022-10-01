# # 1. FizzBuzz 

# Print a string 1,2,3,4, Fizz, 6, Buzz, 8, ..... 34, 
# FizzBuzz, 36, .... to 97, Buzz, 99, Fizz 

# So if number divided by 5 then Fizz If divided by 7 then Buzz,
# If divided by 5 AND 7 then FizzBuzz otherwise the same number

#  Note: such a task became popular as the first task to ask to determine 
#  whether a person knows about programming at all smile

# fizzbuzz_start = int(input("Enter a number for FizzBuzz starts? "))
# fizzbuzz_ends = int(input("What will be the end of the FizzBuzz? "))
# fizz = int(input("Enter number for Fizz "))
# buzz = int((input("Enter the number for Buzz ")))

# for fizzbuzz in range(fizzbuzz_start,fizzbuzz_ends):
#     print("devide " + (fizzbuzz % fizz))
#     if fizzbuzz % fizz == 0 and fizzbuzz % buzz == 0:
#         print("fizzbuzz")
#         continue
#     elif fizzbuzz % fizz == 0:
#         print("fizz")
#         continue
#     elif fizzbuzz % buzz == 0:
#         print("buzz")
#         continue
#     print(fizzbuzz)


    
for fizzbuzz in range(1,10):
    print(fizzbuzz , " devide ", (fizzbuzz % 5))