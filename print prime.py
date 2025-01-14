n=int(input("enter number to check prime:"))
l=[]
for i in range(0,n,1):
    a=int(input("enter the elements of list"))
    l.append(a)
print(l)
for i in l:
    if n%i==0:
        print(i)
        
    
