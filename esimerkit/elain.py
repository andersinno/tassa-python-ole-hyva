import random


class NoisyThing(object):
    def make_noise(self):
        raise NotImplementedError("Not implemented")


class LivingThing(object):
    def live(self):
        raise NotImplementedError("Not implemented")


class Plant(LivingThing):
    pass


class Animal(NoisyThing, LivingThing):
    noise = "*blep*"

    def __init__(self, name):
        self.name = name

    def make_noise(self):
        print("{} says {}".format(self.name, self.noise))

    def __str__(self):
        return "{class_name} named {name}".format(
            class_name=self.__class__.__name__,
            name=self.name
        )

    @classmethod
    def count(cls):
        return ("There approximately {count} {name}s in the world, and they all say {noise}".format(
            count=random.randint(1, 5634635),
            name=cls,
            noise=cls.noise
        ))


class Cat(Animal):
    noise = "miau, miau. miau. miau."


class SomewhatSpecialCat(Cat):
    noise = "something"

    def make_noise(self):
        print("{} goes VUH :D".format(self.name))


def test():
    animal = Animal("Janne")
    animal.make_noise()
    cat = Cat("Misse")
    cat.make_noise()
    cat2 = SomewhatSpecialCat("Tiikeri")
    cat2.make_noise()
    print(Cat.count())
    print(SomewhatSpecialCat.count())
