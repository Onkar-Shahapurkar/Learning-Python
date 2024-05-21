class Employee:
    salary = 5600
    bonus = 400

    @property
    def totalSalary(self):
        return self.salary + self.bonus


e = Employee()
print(e.totalSalary)