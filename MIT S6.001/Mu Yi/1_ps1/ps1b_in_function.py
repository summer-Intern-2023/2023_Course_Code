def part_b(annual_salary, portion_saved, total_cost, semi_annual_raise):
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
	
	    if months % 6 == 0:
	        annual_salary = annual_salary*(1+semi_annual_raise)
	        monthly_salary_saved = annual_salary/12*portion_saved
	
	print('Number of months:', months)
	return months