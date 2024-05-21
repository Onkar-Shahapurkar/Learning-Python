class C2D_Vector:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"


class C3D_Vector(C2D_Vector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"


v2d = C2D_Vector(4, 6)
v3d = C3D_Vector(6, 7, 3)

print(v2d)
print(v3d)