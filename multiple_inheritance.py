class Employee:
    company = "Google"


class Freelancer:
    skill = "Data Science"


class Programmer(Employee, Freelancer):    # Employee is Priority one and Freelancer is priority two
    name = "Omi"


p = Programmer()
print(p.company)
print(p.skill)
print(p.name)