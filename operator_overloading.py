class overload:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __mul__(self, other):
        return self.num * other.num

    def __str__(self):
        return "Object Printed"


n1 = overload(10)
n2 = overload(10)

sum = n1 + n2
mul = n1 * n2

print(sum)
print(mul)
print(n1)