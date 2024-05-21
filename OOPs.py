class Sample:
    def func(self):
        print("Hello World")


s = Sample()
s.func()




class Employee:
    company = "Google"


emp1 = Employee()
emp1.company = "Youtube"
print(emp1.company)               # Printing instance variable
print(Employee.company)           # Printing class variable

Employee.company = "Microsoft"    # Changing class variable
print(Employee.company)           # made changes reflecting to class variable