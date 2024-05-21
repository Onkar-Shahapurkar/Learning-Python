class Calculator:
    def __init__(self, num):
        self.num = num
        print(f"The number is : {self.num}")

    def square(self):
        print(f"The Square of {self.num} is : {self.num ** 2}")

    def squareRoot(self):
        print(f"The Squareroot of {self.num} is : {self.num ** 0.05}")

    def cube(self):
        print(f"The Cube of {self.num} is : {self.num ** 3}")


c = Calculator(9)
c.square()
c.squareRoot()
c.cube()