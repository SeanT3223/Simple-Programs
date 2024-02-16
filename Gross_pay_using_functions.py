

def computepay(h, r):
    if h <= 40:
        gross_pay = r * h 
        return gross_pay
    else:
        ot = h - 40 
        gross_pay = (40 * r) + (1.5 * (ot * r))
        return gross_pay


hours = float(input("Enter Hours:"))
rate = float(input("Enter rate per hour:"))

x = computepay(hours, rate)
print("Pay", x)