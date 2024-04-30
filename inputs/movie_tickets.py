message = "How old are you? "
flag = True

while flag:
    age = input(message)
    if age == 'quit':
        flag = False
        break
    else:
        age = int(age)
        if age < 3:
            price = 0
        elif age < 12:
            price = 10
        else:
            price = 15
    
    print(f"Your are going to pay {price}.")