buffet = ('picania', 'lasagna', 'baby beef', 'tomahawk', 'pique')

print(f"The Yorchie's menu are:")
for food in buffet:
    print(f"- {food.title()}")

buffet = ('milanesa', 'chairo', 'asado en olla', 'silpancho', 'charke')

print(f"Yorchie's menu has changed:")
for food in buffet:
    print(f"- {food.title()}")