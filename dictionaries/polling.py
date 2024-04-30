favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

people = ['george', 'sarah', 'luis', 'phil', 'fidel']

for person in people:
    if person in favorite_languages.keys():
        print(f"{person.title()}, thank you for taking the poll.")
    else:
        print(f"{person.title()}, please take our poll!")