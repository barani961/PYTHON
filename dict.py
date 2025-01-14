phone={
'barnai':230761,
'arjun':230987,
}
print(type(phone))
print(phone['arjun'])
print(phone.keys())
phone['sanjay']=230785
print(phone)
print(phone.values())
print(phone.items())
print(len(phone))
del phone['arjun']
print(phone)
