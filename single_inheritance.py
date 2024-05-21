class Employee:
    company = "Google"

    def showDetails(self):
        print("This is a class Employee")


class Programmer(Employee):
    language = "Python"

    def getLanguage(self):
        print(f"The language is {self.language}")

    def showDetails(self):
        print("This is class Programmer")  # Function Overwritten


e = Employee()
print(e.company)
e.showDetails()

p = Programmer()
p.getLanguage()
p.showDetails()
print(p.company)
