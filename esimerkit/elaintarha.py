# -*- coding: utf-8 -*-

from elain import Cat, LivingThing

cats = []
for n in range(10):
    cats.append(Cat("Cat {}".format(n)))

for cat in cats:
    cat.make_noise()
