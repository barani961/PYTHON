#to print sum of n numbers using while loop and for in range (start,end+1,inc/dec)

n=int(input("enter the n value"))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1

print("sum=",sum)
