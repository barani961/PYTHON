class barani:
    followers=0
    def __init__(self,name,sec):
        self.name=name
        self.sec=sec
        print(self.name)
    def print_info(self):
        print("printing the function print_info:")
        print("name:",self.name)
        print("section",self.sec)
    def update_fees(self,fee):
        print("printing the update")
        print(f" for the student {self.name} ,the fee for this academic year is {fee}")
       
        
        
obj=barani('barani','B')
obj2=barani('sanjay','C')
print("\n")
obj.print_info()
print("\n")
obj.update_fees(50000)
print("\n")
obj2.update_fees(20000)
5


