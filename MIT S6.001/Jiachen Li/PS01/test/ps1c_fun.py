import math

initial_deposit = float(input("Enter the starting salary:"))

total_cost = 1000000
portion_down_payment = 0.25
semi_annual_raise = 0.07

down_payment_amount = total_cost * portion_down_payment

def check_range(save):
    return save >= (down_payment_amount - 100) and save <= (down_payment_amount + 100)

def boot36m(rate):
    global initial_deposit
    current_savings = initial_deposit
    for i in range(36):
        current_savings *= (1 + rate / 12)
    return current_savings

def bisection_search():
    low, steps, high = 0, 0, 10000
    guess = (high + low) // 2
    
    while True:
        if int(guess / 1000) == 9:
            print("It is not possible to pay the down payment in three years.")
            return
        
        steps += 1
        if check_range(boot36m(guess / 10000)):
            break
        elif boot36m(guess / 10000) < down_payment_amount:
            low = guess
        else:
            high = guess
        guess = (high + low) // 2
    
    print(guess / 10000, steps)

bisection_search()