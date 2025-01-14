input_num = input("Enter numbers separated by comma: ")
numbers = input_num.split(",")

prime = []

for Num in numbers:
    num = int(Num)
    if num > 1:
        is_prime = True
       
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
       
        if is_prime:
           print(num)



