


score = float(input("Provide a score between 0.0 and 1.0"))

if 0.0 < score < 1.0:
    if score >= .9:
        print("A")
    elif score >= .8:
        print("B")
    elif score >= .7:
        print("C")
    elif score >= .6:
        print("D")
    elif score < .6:
        print("F")
else:
    print("error score outside of range")