l=[3,2,3,8,45]
l2=[3,3,5,42,8,4]
s=set(l)
s1=set(l2)
if s&s1:
    print(s&s1)
else:
       print(" no common element")
