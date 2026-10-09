class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


def make_sound(animal):
    animal.sound()


d1 = Dog()
c1 = Cat()

make_sound(d1)
make_sound(c1)
