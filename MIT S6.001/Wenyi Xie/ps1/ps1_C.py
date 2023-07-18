semi_annual_raise = 0.07
total_cost = 1000000 * 0.25
r = 0.04
month = 0

def test(portion_saved, current_savings, annual_salary):
    global month, r, total_cost,semi_annual_raise
    while True: 
        invest_month = current_savings * (r / 12)
        current_savings = current_savings + invest_month + (annual_salary/12) * portion_saved
        month = month + 1
        if month % 6 == 0:
            annual_salary = annual_salary + annual_salary * semi_annual_raise
        if current_savings > total_cost:
            break
    return current_savings


annual_salary = float(input("Enter your starting salary: "))

current_savings = 0.0
rate_min = 0
rate_max = 10000
re = (10000 / 2) - 1
mid = 0.0
Steps = 0
while True:
    if Steps > re:
        print("It is not possible to pay the down payment in three years.")
        break
    month = 0
    mid = (rate_min + rate_max)//2
    portion_saved = mid * 0.0001
    res = test(portion_saved, current_savings, annual_salary)
    Steps = Steps + 1
    if month == 36 and res < 250100:
        break
    elif month > 36:
        rate_min = mid
    else:
        rate_max = mid

if Steps < re:
    print("Best savings rate: ", round(portion_saved, 4))
    print("Steps in bisection search: ", Steps)