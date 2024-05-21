class Train:

    def __init__(self, name, price, seats):
        self.name = name
        self.seats = seats
        self.price = price

    def getStatus(self):
        print(f"Name of the Train is : {self.name}")
        print(f"The Seats available in the train is : {self.seats}")

    def fareInfo(self):
        print(f"The Price for this Ticket is : {self.price}")

    def bookTicket(self):
        if self.seats > 0:
            print("Your Ticket has been Booked")
            self.seats = self.seats - 1
        else:
            print("Tickets are not available")


omi = Train("Hutatma Express = 14025", 130, 350)
omi.getStatus()
omi.fareInfo()
omi.bookTicket()