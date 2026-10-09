class Employee:

    def __init__(self):
        print("Employee object created")


e1 = Employee()




class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


e1 = Employee("Muni", 50000)

print(e1.name)
print(e1.salary)





class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


e1 = Employee("Muni", 50000)

e1.display()
