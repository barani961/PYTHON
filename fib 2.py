terms=int(input("enter the no of terms"))
fib=[0,1]
while len(fib)<terms:
    c=fib[-1]+fib[-2]
    fib.append(c)
print(c)
