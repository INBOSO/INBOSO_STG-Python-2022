# 1. Health check

# Ask user for their temperature.
a = int(input("What is your temperature "));

text= "possible fever";
if a < 35:
    text= "not too cold";

elif a <= 37:   
    text= "all right";

print(f"Temperature:  {a} : {text}")
# If the user enters below 35, then output "not too cold"

# If 35 to 37 (inclusive), output "all right"

# If the temperature  over 37, then output  "possible fever

# remember about type conversion if needed