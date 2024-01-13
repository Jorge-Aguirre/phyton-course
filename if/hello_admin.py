user_names = ['admin', 'jorge', 'luis', 'fidel', 'juan carlos']

for user in user_names:
    if user == 'admin':
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")