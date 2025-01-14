def has_no_or_special(sentence):
    for word in sentence.split():
        for char in word:
            if char.isnumeric() or not char.isalnum():
                    return True
    return False
input_res=input("enter sentence to check whether sentence have numeric or special char:")
result=has_no_or_special(input_res)
if result:
    print("True,\nspecial char or numeric present in sentence")
else:
    print("False,\nno special char is present in sentence")
