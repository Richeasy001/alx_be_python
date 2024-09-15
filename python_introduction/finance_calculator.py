income = int(input("Enter your monthly income: "))
exp = int(input("Enter your total monthly expenses: "))
monthly_savings = income - exp
Savings = (monthly_savings * 12 + (monthly_savings * 12 * 0.05))
print (f"Your monthly savings are ${monthly_savings}.")
print (f"Projected savings after one year, with interest, is: ${Savings}.")