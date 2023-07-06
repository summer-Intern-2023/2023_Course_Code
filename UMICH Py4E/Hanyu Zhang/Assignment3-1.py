hrs = input("Enter Hours: ")
per = input("Hourly rate: ")
h = float(hrs)
p = float(per)
if h < 40 :
    print(h * p)
else :
    print(40 * p + 1.5 * p * (h - 40))