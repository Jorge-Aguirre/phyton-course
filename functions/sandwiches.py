def make_sandwich(*ingredients):
    print("\nMaking a sandwich with:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwich('pepperoni', 'cheese', 'tomatoes')
make_sandwich('salame', 'onions', 'eggs', 'tocino')