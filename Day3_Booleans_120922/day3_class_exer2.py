
# #1
# m_salary_amount = int(input("What is your monthly salary amount? "))
# years_worked = float(input("How long are you with company? (in years) "))
# bonus = m_salary_amount * 0.15 * (years_worked-2)

# if years_worked >= 2:
#     print (f"Your bonus 15% from {m_salary_amount} is: {bonus}")
# else:
#     print ("No bonus (0)")

#2
years_worked = float(input("How long are you with company? (in years) "))

if years_worked > 2:
    m_salary_amount = float(input("What is your monthly salary amount? "))
    bonus_rate = 0.15
    bonus_amount = round(m_salary_amount * bonus_rate * (years_worked-2),2)
    print (f"Your bonus 15% from {m_salary_amount} is: {bonus_amount}")

else:
    print ("No bonus (0)")

# 2. Xmas Bonus

# The company has promised a Christmas bonus in the amount of 15% of the monthly salary for EVERY year of 
# service over 2 years.
# Task. Ask the user for the amount of the monthly salary and the number of years worked.
# Calculate the bonus.
# Example1: 5 years of experience, 1000 Euro salary, the bonus will be 450 Euro.
# Example2: 1.5 years of experience, 1500 Euro salary, no bonus(0)

