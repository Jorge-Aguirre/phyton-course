guest_list = ['juan', 'pedro', 'maria']

print(f'Suddenly we have more guest than previsted, we need a big table')

guest_list.insert(0, 'paola')
guest_list.insert(2, 'jorge')
guest_list.append('rodrigo')

message = f"I'd like to invite you to dinner tomorrow."
print(f'Hi {guest_list[0].title()}, {message}')
print(f'Hi {guest_list[1].title()}, {message}')
print(f'Hi {guest_list[2].title()}, {message}')
print(f'Hi {guest_list[3].title()}, {message}')
print(f'Hi {guest_list[4].title()}, {message}')
print(f'Hi {guest_list[5].title()}, {message}')