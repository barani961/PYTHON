#arbitrary arguments
def sum_(*num):#these arguments converted into tuple
    c=0
    for i in (num):
        c+=i
    print(c)
sum_(3,4,5,6)
