def laske(alffa, beetta, kissa=8):
    return alffa * beetta / kissa

def keskiarvo(*luvut):
    return sum(luvut) / len(luvut)

def teekoo_ikkuna(alffa, **kwargs):
    return "i am window with {} things.".format(len(kwargs))

if 0:
    print(laske(10, 20, 30))
    print(laske(10, beetta=16))
    print(laske(alffa=3, beetta=8))
    argumentit = {"alffa": 8, "beetta": 99}
    print(laske(**argumentit))
    argumentit = {"alffa": 8}
    print(laske(beetta=10, kissa=91, **argumentit))

    asiat = (1, 2, 3)
    print(laske(*asiat))

#print(keskiarvo(1, 6, 3, 67, -42, 3.141))

print(teekoo_ikkuna(beetta=343, alffa=100, tutturuu=100))
