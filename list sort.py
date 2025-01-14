a=[1,2,49,87,3,5,0]
b=['hi','jp','aok']
b.sort()#it changes the original list  

new_a=sorted(a)
print("new a without changing original list:",new_a)
print("even after sorting we didnt change a:",a)
print(b)
print("after this reversing using in sort method:\n")
a.sort(reverse=True)
print(a)#revere the list

