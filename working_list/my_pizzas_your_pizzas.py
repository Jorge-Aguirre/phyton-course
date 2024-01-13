pizzas = ['cuatro quesos', 'mozzarella', 'hawaiana']
friend_pizzas = pizzas[:]

pizzas.append('salame')
friend_pizzas.append('choclo con pollo')

print(f"My favorite pizzas are:")
for my_pizza in pizzas:
    print(f"{my_pizza.title()}")

print(f"\nMy friend's favorite pizzas are:")
for your_pizza in friend_pizzas:
    print(your_pizza.title())