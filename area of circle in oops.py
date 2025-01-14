class circle:
    pi=3.14
    def __init__(self,r):
        self.r=r
        
    def area(self):
        area=self.pi*self.r**2
        print(area)
obj=circle(10)
obj.area()
circle2=circle(r=30)
circle2.area()
