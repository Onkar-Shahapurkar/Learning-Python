class Library:
    def __init__(self, books):
        self.books = books

    def displaylist(self):
        print("Books available in the Library are :")
        for index, book in enumerate(self.books):
            print(f"{index+1}. {book}")

    def requestbook(self, book):
        if book in self.books:
            print(f"You have Requested the book titled as {book}. Handle the book properly and keep it safe")
            self.books.remove(book)
            return True
        else:
            print("This book has been issued to someone else or is unavailable at the moment. Please wait till it is available")
            return False

    def returnbook(self, book):
        self.books.append(book)
        print(f"You have Returned the book titled as {book}. Thankyou !!!!")



class Student:
    def requestbook(self):
        self.book = input("Enter Book that you want to issue :")
        return self.book

    def returnbook(self):
        self.book = input("Enter the Book name to return :")
        return self.book


library = Library(["Algorithms", "Data Structure", "Python Beginners Guide", "Artificial Intelligence", "Machine Learning"])
student = Student()

while True:
    wlcm = '''\n ===== Welcome to Omi's Library =====
        1. List the available books
        2. Request a book
        3. Return a Book
        4. Exit.'''
    print(wlcm)

    a = int(input("Enter your choice :"))
    print()
    if a == 1:
        library.displaylist()
    elif a == 2:
        library.requestbook(student.requestbook())
    elif a == 3:
        library.returnbook(student.returnbook())
    elif a == 4:
        print("Thankyou for choosing Omi's Library. Wish you a great day !!")
        exit()
    else:
        print("Invalid Choice !!!!!")