#user_names = ['admin', 'jorge', 'luis', 'fidel', 'juan carlos']
user_names = []

if user_names:
    for user in user_names:
        if user == 'admin':
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")