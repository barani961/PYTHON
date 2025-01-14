def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a%b
    
a=int(input("enter the num 1:"))
b=int(input("enter the num 1:"))
op=input("enter a operation[*,+,%,-]:")
if op == '+':
    value=add(a,b)
    print("additon of",a ,"and", b,"=",value)
elif op == '-':
    value=sub(a,b)
    print("subraction of",a ,"and", b,"=",value)
elif op == '*':
    value=mul(a,b)
    print("multiplication of",a ,"and", b,"=",value)
elif op == '%':
    value=div(a,b)
    print("modulo of",a ,"and", b,"=",value)
    
        
    
    
