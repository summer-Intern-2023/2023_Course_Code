# User Input
initial_deposit = float(input("Enter the initial deposit: "))

# Variable initialization
year = 3
lowest = 0
highest = 1

if 159900 <= initial_deposit:
    r = 0.0
    print("Best savings rate: 0.0")
    print("Steps in bisection search: 0")
if (initial_deposit*(1+1/12)**36) < 159900:
    r = None
    print("Best savings rate: "+str(r))
    print("Steps in bisection search: 0")
count = 0
while True:
    r = (lowest+highest)/2
    if (initial_deposit*((1+r/12)**36)) < 159900:
        lowest = r
    if (initial_deposit*((1+r/12)**36)) > 160100:
        highest = r
    if 159900 <= (initial_deposit*((1+r/12)**36)) < 160100:
        print('Best savings rate: '+str(r))
        break
    count += 1

print("Steps in bisection search: ", count)
