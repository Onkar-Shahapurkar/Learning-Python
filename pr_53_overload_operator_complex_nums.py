class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginery = i

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginery + other.imaginery)

    def __mul__(self, other):
        # (ac-bd) + (ad+bc)
        mulReal = self.real * other.real - self.imaginery * other.imaginery
        mulImg =  self.real * other.imaginery + self.imaginery * other.real
        return Complex(mulReal, mulImg)

    def __str__(self):
        return f"{self.real} + {self.imaginery}i"


c1 = Complex(3, 2)
c2 = Complex(1, 7)
print(c1 + c2)
print(c1 * c2)