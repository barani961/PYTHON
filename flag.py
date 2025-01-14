#15.prime number
i=0
int(input("enter the value of n"))
for i in range (2,(n//2)+1,1):
    if n%i==0:
        f=1
    if f==0:
        print(" prime")

if f==0:
        print("not prime")
