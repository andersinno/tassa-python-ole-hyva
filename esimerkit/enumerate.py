# -*- coding: utf-8 -*-

nimet = ["Janne", "Matti", "Teppo", "Hylje"]
iat = [666, 1600, 2432, 3]

for i, nimi in enumerate(nimet):
    print(nimi, iat[i])

print("===")

for nimi, ika in zip(nimet, iat):
    print(nimi, ika)

print("===")

abc = [
    (1, 2, 3),
    (4, 5, 6),
    (8, 9, 10)
]
cba = list(zip(*abc))
print(cba)
abc2 = list(zip(*cba))
print(abc2)
print(abc == abc2)
