# User Input
annual_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

# Variable initialization
portion_down_payment = 0.20
current_savings = 0
r = 0.04
months = 0

while current_savings<total_cost*portion_down_payment:
    months +=1
    current_savings+=annual_salary/12*portion_saved+current_savings*r/12

print('Number of months: '+str(months))