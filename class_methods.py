class employee:
    salary = 100
    company = "Google"

    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal

    def changeCompany(self, company):
        self.company = company


e = employee()
print(f"This is Salary of object attribute {e.salary}")
print(f"This is Company of object attribute {e.company}")
print(f"This is Salary of class attribute {employee.salary}")
print(f"This is Company of class attribute {employee.company}")

e.changeSalary(1000000)
e.changeCompany("Youtube")

print(f"\n\nThis is Salary of object attribute after method execution {e.salary}")
print(f"This is Company of object attribute after method execution {e.company}")
print(f"This is Salary of class attribute after method execution {employee.salary}")
print(f"This is Company of class attribute after method execution {employee.company}")
