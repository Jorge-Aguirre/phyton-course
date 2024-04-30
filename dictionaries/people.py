fidel = {
    'first_name': 'fidel',
    'last_name': 'barcaya',
    'age': 34,
    'city': 'cochabamba',
    }

luis = {
    'first_name': 'luis',
    'last_name': 'choque',
    'age': 32,
    'city': 'oruro',
    }
juanka = {
    'first_name': 'juan carlos',
    'last_name': 'ojeda',
    'age': 35,
    'city': 'buenos aires',
    }

people = [fidel, luis, juanka]

for person in people:
    print(person['first_name'].title())
    print(person['last_name'].title())
    print(person['age'])
    print(person['city'].title())