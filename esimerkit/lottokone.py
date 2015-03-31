import random

names_and_ages = {
    "Taina Testi": 22,
    "Teppo Testi": 31,
    "Teddy Test": 6,
    "Tina Test": 141,
    "Kaapo Koe": -7,
    "Kissa": 2
}

print(sorted(names_and_ages.keys(), key=len))
print(sorted(names_and_ages.values()))


def sort_by_age(item):
    return item[1]

print(sorted(names_and_ages.items(), key=sort_by_age))

names = list(names_and_ages.keys())
random.shuffle(names)

for name in names:
    print("The name '{}' is {} characters long".format(name, len(name)))

print("The winner is " + random.choice(names))

