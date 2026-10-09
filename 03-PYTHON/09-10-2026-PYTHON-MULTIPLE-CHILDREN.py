class Employee:

    def display(self):
        print("Employee")


class Developer(Employee):

    def code(self):
        print("Developer is coding")


class Tester(Employee):

    def test(self):
        print("Tester is testing")


d1 = Developer()
t1 = Tester()

d1.display()
d1.code()

t1.display()
t1.test()
