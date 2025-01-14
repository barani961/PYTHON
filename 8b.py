# WAP to remove dup elements
print("LIST:\n")
_list = input("Enter values use commas in b/w elements: ").split(',')
my_list = list({int(item.strip()) for item in _list})
print("List without duplicate elem:", my_list)
print("\nTUPLE:")
user_tuple = input("\nEnter values using commas: ").split(',')
dup_tuple = tuple({int(item.strip()) for item in user_tuple})
print("Tuple without duplicates:", dup_tuple)
print("\nSET:")
user_set = input("\nEnter values using commas: ").split(',')
dup_set = {int(item.strip()) for item in user_set}
print("Set without duplicates:", dup_set)
