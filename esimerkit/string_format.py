# -*- coding: utf-8 -*-

luku = 42
nimi = "Janne"

print("%s:n onnenluku on %s" % (nimi, luku))
print("%s:n onnenluku on %.8f" % (nimi, luku))
print("%(nimi)s:n onnenluku on %(luku).8f" % {"nimi": nimi, "luku": luku})
print("{0}:n onnenluku on {1}".format(nimi, luku))
print("{0}:n onnenluku on {1}".format(luku, nimi))
print("{nimi}:n onnenluku on {luku}".format(nimi=nimi, luku=luku))
