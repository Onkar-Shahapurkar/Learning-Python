class Animal:
    pass


class pet(Animal):
    pass


class dog(pet):
    @staticmethod
    def bark():
        print("Bow Bow !!!!")


d = dog()
d.bark()