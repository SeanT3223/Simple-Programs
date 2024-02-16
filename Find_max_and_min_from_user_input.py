L = None
S = None 
CL = None
CS = None

x = True
 

while True: 
    num = input("Enter a number:")
    if num == "done":
        break
    try:
        num = float(num)
        if L == None or L < num :
            L = num 
        elif S == None or S > num: 
            S = num 
    except:
        print("Invalid input")

print("Maximum is", L)
print("Minimum is", S)
