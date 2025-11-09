monthly_income = int(input("Enter your monthly income: "))
monthly_expense = int(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expense
annual_interest = 0.05

projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * annual_interest))

print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")

