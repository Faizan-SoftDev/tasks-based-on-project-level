"""Create a function called salary_estimator(tax_rate). 
Inside it, define and return a nested function called estimate(basic_salary).
The nested function should calculate the salary after deducting the tax.
Requirements:The outer function salary_estimator must accept one parameter: tax_rate (a float representing percentage, e.g., 0.10 for 10% tax).
The outer function must return the inner function itself (not the result of the inner function).
The inner function estimate must accept basic_salary.If basic_salary is 0 or negative, return "Invalid Salary".
Otherwise, the inner function should calculate and return the salary after tax deduction using the formula: basic_salary * (1 - tax_rate)."""
def salary_estimate(tax_rate):
    def estimate(basic_salary):
        if basic_salary <= 0:
            return "Invalid Salary"
        else:
            return(basic_salary* (1 - tax_rate))
    return estimate