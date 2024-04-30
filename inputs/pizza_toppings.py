flag = True
message = f"Please enter the topping that you want add to your pizza: "

while flag:
    topping = input(message)
    if topping == 'quit':
        flag = False
        break
    else:
        print(f"We're adding {topping} to your pizza soon!")