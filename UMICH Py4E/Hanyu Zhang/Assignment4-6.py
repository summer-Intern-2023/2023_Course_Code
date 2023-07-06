hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter hourly rate: ")
r = float(rate)

def compute_pay(h, r) :
    if h <= 40 :
        return h * r
    elif h > 40 :
        return 40 * r + 1.5 * r * (h - 40)

p = compute_pay(h, r)
print("Pay", p)