guest_list = ['juan', 'pedro', 'maria']

replaced_guest = guest_list.pop(1)
print(f'Unafortunately {replaced_guest.title()} cannot join us in the dinner.')

guest_list.insert(1, 'raul')

message = f"I'd like to invite you to dinner tomorrow." 
print(f'Hi {guest_list[0].title()}, {message}')
print(f'Hi {guest_list[1].title()}, {message}')
print(f'Hi {guest_list[2].title()}, {message}')