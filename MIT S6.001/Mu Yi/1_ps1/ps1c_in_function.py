def part_c(initial_deposit):
    #########################################################################
    portion_down_payment = 0.25
    total_cost = 750000

    down_payment_amount = total_cost * portion_down_payment

    ###############################################################################################
    ## Determine how many months it would take to get the down payment for your dream home below ##
    ###############################################################################################

    def check_in_range(m):
        return m >= down_payment_amount-100 and m <= down_payment_amount+100

    def increment_36m(r):
        global initial_deposit
        current_savings = initial_deposit
        for i in range(36):
            current_savings *= (1 + r/12)

        return current_savings

    def bisection_search():
        global initial_deposit
        low = 0
        high = 10000
        steps = 0
        guess = (high + low) // 2
        while True:
            steps += 1
            if check_in_range(increment_36m(guess/10000)):
                break
            elif increment_36m(guess/10000) < down_payment_amount:
                low = guess
            else:
                high = guess
            guess = (high + low) // 2

        print(guess/10000, steps)

    bisection_search()
    return r, steps
