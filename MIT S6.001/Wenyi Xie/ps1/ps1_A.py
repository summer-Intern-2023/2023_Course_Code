annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: ")) * 0.25
current_savings = 0.0
month = 0
r = 0.04
while True:
    invest_month = current_savings * (r / 12)
    current_savings = current_savings + invest_month + (annual_salary/12) * portion_saved
    month = month + 1
    if current_savings > total_cost:
        break
print("Number of months: ", month)