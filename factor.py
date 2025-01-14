#factor
a=int(input("enter the number to check the factors:"))
l=[]
for i in range(1,a):
    if a%i==0:
        l.append(i)
print(l)
