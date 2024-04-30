sandwich_orders = ['tuna', 'avocado', 'chicken', 'cesar', 'egg']
finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich")
    sandwich_orders.remove(sandwich)
    finished_sandwiches.append(sandwich)

print(f"Finished sandwiches: {finished_sandwiches}")