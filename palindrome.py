
a=input("enter the string to check it is a palindrome or not:")
b=''.join(reversed(a))+" "

val=True
for i in range (len(a)):
    if a[i]!=b[i]:
        val=False
if val:
    print("palindrome ")
else:
    print("not")
        
