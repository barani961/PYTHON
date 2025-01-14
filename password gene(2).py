import random
print("Welcome to password generator!!!")
alpha=[chr(i) for i in range(97,123)]+[chr(i) for i in range(65,91)]
num=['1','2','3','4','5','6','7','8','9']
symb=['!','@','$','%','^','&','*','(',')']

al_no=int(input("enter the no of alphabets in your pass:"))
no=int(input("enter the no of numbers in your pass:"))
sym_no=int(input("enter the no of sym in your pass:"))
def passgen(al_no,no,sym_no):
    password=[]
    for i in range(0,al_no):
        a=random.choice(alpha)
        password+=a
    for i in range(0,no):
        b=random.choice(num)
        password+=b
    for i in range(0,sym_no):
        c=random.choice(symb)
        password+=c
    return password
        
a=passgen(al_no,no,sym_no)
print("the generated password for your convinience is:",a)
random.shuffle(a)
print(a)
pas=""
for i in (a):
    pas+=i
print("\nthe shuffled password is :",pas)
    






    



