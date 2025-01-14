#prime or not prime
start=int(input("enter the start number:"))
end=int(input("enter the end of range:"))
prime=[]
non_prime=[]
for num in range(start,end+1):
    is_prime=1
    for i in range(2,(num//2)+1):
        if num%i==0:
            is_prime=0
            break;

    if is_prime and num>1:
        prime.append(num)
    else:
        non_prime.append(num)
print("prime numbers are:",prime)
print("non prime numbers are:",non_prime)
