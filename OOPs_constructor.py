class sample:
    def __init__(self):
        print(f"Constructor Called")


s = sample()


class sample1:
    def __init__(self, name):
        print("Constructor Called", name)


s1 = sample1("Onkar")