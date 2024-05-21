class Employee:
    company = "Google"

    def getSalary(self):
        print(f"Salary for Employee working in {self.company} is {self.salary}")


omi = Employee()
omi.salary = 1500000
omi.getSalary()
Employee.getSalary(omi)

# The omi.getSalary() is equivalent to the Employee.getSalary(omi)