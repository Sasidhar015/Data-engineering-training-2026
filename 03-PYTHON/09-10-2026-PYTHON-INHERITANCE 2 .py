class Employee:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Employee:", self.name)


class Manager(Employee):

    def manage_team(self):
        print(self.name, "is managing the team")


m1 = Manager("Muni")

m1.display()
m1.manage_team()






class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def manage(self):
        print("Department:", self.department)


m1 = Manager("Muni", 50000, "IT")

m1.display()
m1.manage()
