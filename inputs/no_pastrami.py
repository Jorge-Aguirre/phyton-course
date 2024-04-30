print(f"Deli has run out of pastrami sandwich")
sandwich_orders = [
    'pastrami',
    'tuna',
    'avocado',
    'pastrami',
    'chicken',
    'cesar',
    'egg',
    'pastrami'
    ]
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)