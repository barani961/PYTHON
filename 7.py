class A:
    def __init__(self,a):
        self.a=a
class B(A):
    def __init__(self,a,b):
        super().__init__(a)
        self.b=b
class C(B):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c
    def calculate(self):
        return self.a+self.b+self.c
a= int(input("enter a :"))
b= int(input("enter b :"))
c= int(input("enter c :"))
c_obj=C(a,b,c)
print(c_obj.calculate())
        
    
