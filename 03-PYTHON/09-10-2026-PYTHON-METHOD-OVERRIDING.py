class Animal:

    def sound(self):
        print("Animal makes sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog = Dog()

dog.sound()






class Employee:

    def __init__(self, name):
        self.name = name

    def work(self):
        print(self.name, "is working")


class Developer(Employee):

    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def work(self):
        print(self.name, "is coding in", self.language)


d = Developer("Muni", "Python")

d.work()









