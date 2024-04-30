cities = {
    'cochabamba': {
        'country': 'bolivia',
        'population': 1200000,
        'fact': 'donde mejor comida hay en bolivia',
        },
    'buenos aires': {
        'country': 'argentina',
        'population': 9000000,
        'fact': 'la ciudad mas europea de sudamerica',
        },
    'nueva york': {
        'country': 'estados unidos',
        'population': 90000000,
        'fact': 'la ciudad mas avanzada del planeta'
    },
    }

for city, information in cities.items():
    print(f"\nSome information about {city.title()} city:")

    for key, value in information.items():
        print(f"\t{key.title()}: {value}")