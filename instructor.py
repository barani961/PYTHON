class Instructor:
    follower=0
    def __init__(self,name):
        self.name=name#attributes of class

        
    def print_name(self):#methods
        print(self.name)
obj=Instructor("barani")
obj2=Instructor("sanjay")
print(obj.print_name())
print(obj.name)
print(obj2.print_name())
print(obj2.name)
        
