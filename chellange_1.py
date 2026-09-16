# Day 1 Challenge: Python Functions & Default ArgumentsTask Description:
# Write a Python function named calculate_salary that calculates the total monthly payout for an employee based on their base salary and an optional performance bonus.
# Requirements:The function must accept two parameters: basic_salary and bonus.
# The bonus parameter must have a default value of 0 (so the function doesn't crash if no bonus is provided).
# If the basic_salary is 0 or a negative number, the function should return the string: "Invalid Salary".
# Otherwise, it should return the total sum of basic_salary and bonus.
# Expected Behavior Examples:calculate_salary(50000, 5000) should return 55000calculate_salary(60000) should return 60000 (since bonus defaults to 0)calculate_salary(-1000) should return "Invalid Salary"
def calculate_salary(basic_salary, bonus=0):
    if basic_salary <=0:
        return "invalid salary"
    else:
        return basic_salary + bonus
        
    
    
