favorite_places = {
    'fidel': ['paris', 'tokio', 'santa cruz'],
    'luis': ['uyuni', 'buenos aires'],
    'juan carlos': ['chapare'],
    'jorge': ['madrid', 'nueva york'],
    }

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")

    for place in places:
        print(f"\t{place.title()}")

