# -*- coding: utf-8 -*-
import datetime


def test():
    s = "string"
    i = 42
    f = 42.4242
    dt = datetime.date(2015, 4, 1)
    l = [s, i, f, dt]
    print(l)
    l[0] = "hei"
    print(l)
    t = (s, i, f, dt)
    print(t)

    d = {
        "kissa": "katten",
        "koira": "hund",
        "hevonen": "häst"
    }

    print(d)
    print(d["hevonen"])

    for key in d:
        print(key)

    numerojoukko = {1, 2, 4, 8, 16}
    print(numerojoukko)
    print(3 in numerojoukko)
    print(4 in numerojoukko)

    if 4 in numerojoukko:
        print("Nelonenhan se siellä möllöttää")

    for name, obj in locals().items():
        print(name)
        print(obj)
        print(type(obj))
        print("=" * 40)


if __name__ == "__main__":
    test()
