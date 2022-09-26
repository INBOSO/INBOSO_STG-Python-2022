# So today's exercise: #
# Write a program that asks for and saves a username
# Ask a question about the user's age, using the username in the question.
# Shows in how many years the user will be 100 years old smile
# BONUS: 
# then you will need two additional lines:
# import datetime # let's talk about imports separately
# currentYear = datetime.datetime.now (). yearLet the program also show the year when the user will be 100 years old.
# It could use a variable with the current year.
# It would be even better to get the current year automatically

import datetime
print (f"Today is ", datetime.datetime.now())

name = input ("What is your name? ")
print (f"Hello {name}")

age_now = int(input ("What is your age? "))
print (f"It's nice age {age_now}")

age_100 = int(100)
age_between = age_100 - age_now
print(f"You will be {age_100} age old in {age_between} years")

current_year = datetime.datetime.now().year
year_when_will_be_100 = int(current_year) + int(age_100)
print(f"And it will happened in {year_when_will_be_100}!")
