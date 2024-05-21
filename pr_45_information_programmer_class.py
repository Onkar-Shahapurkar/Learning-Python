class programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The Name of Programmer is :{self.name}")
        print(f"The Product of Programmer is :{self.product}")
        print(f"The Company of Programmer is :{self.company}")


omi = programmer("Onkar", "Capgemini's AI")
omi.getInfo()
print("\n")
trupti = programmer("Trupti", "Capgemin's Chatbot")
trupti.getInfo()
