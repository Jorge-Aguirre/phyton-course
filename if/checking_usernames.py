current_users = ['JORGE', 'luis', 'FIDEL', 'juan carlos', 'Eddy']
new_users = ['raul', 'eddy', 'jessica', 'fidel', 'jhoselin']

users = []

for user in current_users:
    users.append(user.lower())

for user in new_users:
    if user.lower() in users:
        print(f"That {user} nick is already in use please choose another name")
    else:
        print(f"{user} nick is available")