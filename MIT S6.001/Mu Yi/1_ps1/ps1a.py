# 6.0001 Pset 1: Part a
# Name:
# Time Spent:
# Collaborators:

##########################################################################
## Get user input for annual_salary, portion_saved and total_cost below ##
##########################################################################
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(
    input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))


#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.2
down_payment_amount = total_cost * portion_down_payment
r = 0.04
monthly_salary_saved = (annual_salary/12) * portion_saved
mr = r / 12
current_savings = 0.00
months = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ##
###############################################################################################

while current_savings < down_payment_amount:
    monthly_ROI = current_savings * mr
    current_savings = current_savings + monthly_ROI + monthly_salary_saved
    months += 1

print('Number of months:', months)
