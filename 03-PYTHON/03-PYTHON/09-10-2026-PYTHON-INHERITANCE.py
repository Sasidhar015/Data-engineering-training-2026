class Employee:

    def __init__(self, name):
        self.name = name


class Manager(Employee):

    def __init__(self, name, department):
        super().__init__(name)
        self.department = department


m1 = Manager("Muni", "IT")

print(m1.name)
print(m1.department)
