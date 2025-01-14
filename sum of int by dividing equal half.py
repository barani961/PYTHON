
def split(n,lis):
    total=0
    for num in lis:
        num=str(num)
        n=len(num)//2
        first=num[:n]
        last=num[n:]
        total+=int(first)+int(last)
    return total
a=int(input().strip())
b=list(map(int,input().strip().split()))

a=split(a,b)
print(a)    
        
