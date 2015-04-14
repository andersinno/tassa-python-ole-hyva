# -*- coding: utf-8 -*-

import elain  # <-- elain.py
import elain as elukka  # <-- import with alias
from elain import Cat # <-- import specific name

miuku = elain.Cat(name="Miuku")
miuku.make_noise()
mauku = elukka.Cat(name="Mauku")
print(elain.Cat is elukka.Cat is Cat)
mouku = Cat(name="Mouku")

p = elain.Plant()
print(vars(p))
print(p.tell_me_your_secret())
