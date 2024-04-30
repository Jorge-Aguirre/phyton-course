numbers = {
    'jorge': [7, 9, 11],
    'luis': [10],
    'fidel': [5, 69],
    'juanka': [3, 7, 11],
    'daniel': [8],
    }

for name, numbers in numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    print(f"{numbers}")