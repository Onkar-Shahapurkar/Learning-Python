class Employee:
    salary = 5600
    bonus = 400

    @property
    def totalSalary(self):
        return self.salary + self.bonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.bonus = val - self.salary


e = Employee()
print(e.totalSalary)
e.totalSalary = 6200
print(e.salary)
print(e.bonus)
print(e.totalSalary)