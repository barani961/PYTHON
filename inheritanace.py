class human:
    def __init__(self):
        self.eyes=2
        self.nose=1
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
class female(human):
    def __init__(self):
        super().__init__()
    def like(self):
        print("i like boys")
    def likes(self):
        print("i love makeups")
    def work(self):#method overriding !
        print("i can code")
        super().work()

obj=female()
obj.work()
obj.eat()
obj.likes()
print("no of eyes:",obj.eyes)
print("no of nose:",obj.nose)

        
        
