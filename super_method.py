class Parent:
    def __init__(self, txt):
        self.message = txt

    def printMessage(self):
        print(self.message)


class Child(Parent):
    def __init__(self, txt):
        super().__init__(txt)


x = Child("This is Example of Super class Method")
x.printMessage()