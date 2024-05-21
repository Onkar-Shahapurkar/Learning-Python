class person:
    def per(self):
        print("This is Person class")


class Employee(person):
    def emp(self):
        print("This is Employee Class")


class programmer(Employee):
    def prog(self):
        print("This is Programmer class")


p = person()
p.per()

e = Employee()
e.per()
e.emp()

pr = programmer()
pr.per()
pr.emp()
pr.prog()