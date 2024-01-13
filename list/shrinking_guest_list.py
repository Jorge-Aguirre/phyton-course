guest_list = ['paola','juan', 'jorge', 'pedro', 'maria', 'rodrigo']

print(f'My apologies, we have only two places at the dinner table')

popped_guest = guest_list.pop()
print(f"I'm sorry {popped_guest.title()} we don't have a seat for you at the dinner table")
popped_guest = guest_list.pop()
print(f"I'm sorry {popped_guest.title()} we don't have a seat for you at the dinner table")
popped_guest = guest_list.pop()
print(f"I'm sorry {popped_guest.title()} we don't have a seat for you at the dinner table")
popped_guest = guest_list.pop()
print(f"I'm sorry {popped_guest.title()} we don't have a seat for you at the dinner table")


print(f"{guest_list[0].title()} you still invited please come")
print(f"{guest_list[1].title()} you still invited please come")

del guest_list[0]
del guest_list[0]

print(guest_list)