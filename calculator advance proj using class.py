class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(f"addition of{a} and {b}:", self.a+self.b)
    def sub(self):
       print( f"subraction of{a} and {b}:" ,self.a-self.b)
    def mul(self):
        print (f"multiplication of{a} and {b}:", self.a*self.b)
    def div(self):
        print (f"division of{a} and {b}:",self.a//self.b)
    def power(self):
        print( f"power of{a} and {b}:" ,self.a**self.b)
switch=input("calculator on/off:")
while switch=='on':
    
    a=int(input("enter a number :"))
    b=int(input("enter a number :"))
    op=input("enter a operator[+,-,*,/,**]:")
    obj=calculator(a,b)
    if op=='-':
        obj.sub()
    elif op=='+':
        obj.add()
    elif op=='*':
        obj.mul()
    elif op=='**':
        obj.power()
    elif op=='//':
        obj.div()
    else :
        print("invalid operator")

