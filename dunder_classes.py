class Dunder_eg:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f"Number is :{self.num}"

    def __len__(self):
        return self.num


d = Dunder_eg(86)
print(d)
print(len(d))