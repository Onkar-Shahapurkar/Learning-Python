class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        index = 0
        str = ""
        for i in self.vec:
            str += f"{i}a{index} + "
            index += 1
        return str[:-2]

    def __add__(self, other):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + other.vec[i])
        return Vector(newList)

    def __mul__(self, other):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * other.vec[i]
        return sum

    def __len__(self):
        return len(self.vec)


v1 = Vector([4, 5])
v2 = Vector([6, 5])

print(v1 + v2)
print(v1 * v2)

print(len(v1))