class human:
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
class female(human):
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
        
        
