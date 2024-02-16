
#Simply computes a gross pay based on hours and hourly rate with over time considered


hours = float(input("Enter Hours:"))
pay = float(input("Enter Pay Rate:"))

if hours < 40:
    gross_pay = hours*pay
else: 
    hours_over = hours - 40
    gross_pay = (40 * pay) + (1.5 * pay * hours_over)
print(gross_pay)
