print( '''welcome to rock paper scissor game!!\n rules for playing :
\n1.you have to choose your option  
2.computer randomly choose one option
3.rock wins againts scisscor\nscissor wins against paper
paper wins against rock
4.if your option and computer option same then draw
if any other probablity than these above rules you lose''' )

def choice():  
    if our ==1 and comp==1:
        print("our choice:scissor \ncomp choice:scissor")
    elif our==1 and comp==0:
        print("our choice:scissor \ncomp choice:rock")
    elif our==1 and comp==2:
        print("our choice:scissor \ncomp choice:paper")
    elif our==0 and comp==1:
        print("our choice:rock \ncomp choice:scissor")
    elif our==0 and comp==2:
        print("our choice:rock \ncomp choice:paper")
    elif our==0 and comp==0:
        print("our choice:rock \ncomp choice:rock")
    elif our==2 and comp==0:
        print("our choice:paper \ncomp choice:rock")
    elif our==2 and comp==1:
        print("our choice:paper \ncomp choice:scissor")
    elif our==2 and comp==2:
        print("our choice:paper \ncomp choice:paper")
        
        
our =int(input("For rock enter0,For scissor enter 1, For paper enter 2:"))
import random
comp =random.randint(0,2)
if our >2 or comp<0:
    print("enter valid no")
else:
    choice()
    if our==comp:
        print("Draw")
    elif our>0 and comp<2:
            print("You won!!!!")
    elif our==0 and comp==2:
                print("comp won,Better luck next time bro")
    elif our == 1 and  comp==2:
                    print("comp win,Better luck next time bro")
                    
