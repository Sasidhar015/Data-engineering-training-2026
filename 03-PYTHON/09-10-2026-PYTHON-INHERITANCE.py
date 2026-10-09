class Employee:

    def display(self):
        print("Employee")


class Manager(Employee):
    pass


m1 = Manager()
m1.display()




class Employee:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


class Manager(Employee):
    pass


m1 = Manager("Muni")

m1.display()
