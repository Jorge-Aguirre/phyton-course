tyson = {
    'kind': 'dog',
    'age': 3,
    'owner': 'jorge',
    }

panda = {
    'kind': 'dog',
    'age': 5,
    'owner': 'eddy',
}

mishi = {
    'kind': 'cat',
    'age': 4,
    'owner': 'jorge',
    }

pets = [tyson, mishi, panda]

for pet in pets:
    print(f"{pet['kind']}")
    print(f"{pet['owner']}")
    print(f"{pet['age']}")