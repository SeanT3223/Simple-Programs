
#takes in text file and returns non duplicating list of words from each line
fname = input("Enter file name: ")
fh = open(fname)
x = list()
for line in fh:
    words = line.split()
    for word in words:
        if word in x: 
            continue
        else:
            x.append(word)
          
x.sort()
print(x)

    
    
 
