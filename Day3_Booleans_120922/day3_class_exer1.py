# #1
a = float(input("What is your temperature "))

text= "possible fever"
if a < 35:
    text= "not too cold"

elif a <= 37:   
    text= "all right"

print(f"Temperature:  {a} : {text}")

#2
temp = float(input("What is your temperature? "))
if temp < 35:
    print("not too cold", temp)
elif temp <= 37:
    print("all right", temp)
else:
    print("possible fever")
#3
normal_temp = 37
cold_temp = 35

temp = float(input("What is your temperature? "))
if temp < cold_temp:
    print("not too cold", temp)
elif temp <= normal_temp:
    print("all right", temp)
else:
    print("possible fever")
# 1. Health check
# Ask user for their temperature.
# If the user enters below 35, then output "not too cold"
# If 35 to 37 (inclusive), output "all right"
# If the temperature  over 37, then output  "possible fever
# remember about type conversion if needed