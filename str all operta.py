#string every op
name="Baranidharan"
print('name=',name)
print("oth index=",name[0])
print("0:5=",name[0:5])# prints 0th index to 4th
print("lower func:",name.lower())
print("upper func:",name.upper())
print("lenght:",len(name))
print("count of letter a:",name.count('a'))
new_name="barani is a good boy and a good person"
print("new name:",new_name)
print("new name of word GOOD count IS:",new_name.count('good'))
print("to find the index of the word or letter(d) in name :",name.find('d'))
print("to replace word in new_name use replace func to replace word 'good':",new_name.replace('good','success'))
print("\nformat to use instead of f string:\n""hello {} ,welcome".format(name,))
print("\n")
print(help(str.lower))
