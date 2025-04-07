class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def checkout(self):
        if self.available == True:
            self.available = False
            return True
        else:
            return False
        
    def return_book(self):
        self.available = True

    def display_info(self):
        print(f"Book info: \nTitle: {self.title}\nAuthor: {self.author}\n")

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def display_books(self):
        [book.display_info() for book in self.books]
    
    def get_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
    
book1 = Book("Atomic Habits", "James Clear")
book2 = Book("Rich Dad, Poor Dad", "Robert Kiyosaki")
book3 = Book("The Psychology of Money", "Morgan Housel")

books = [book1, book2, book3]

library = Library()
for book in books:
     library.add_book(book)

print("Welcome to the Library!")

while True:
    print("Options")
    print("1 - display available books")
    print("2 - borrow a book")
    print("3 - return a book")
    print("4 - see book details")
    print("5 - donate a book")
    print("6 - search book by title")
    print("7 - exit program")

    action = input("Choose a number from 1-7: ")
    
    if action == "1":
        library.display_books()

    elif action == "2":
        title = input("Enter the book title to borrow: ")
        book = library.get_book_by_title(title)
        if book:
            if book.checkout():
                print("You borrowed the book.")
            else:
                print("Sorry, that book is already borrowed!")
        else:
            print("Book not found.")

    elif action == "3":
        title = input("Enter the book title to return: ")
        book = library.get_book_by_title(title)
        if book:
            book.return_book()
            print("Book returned. Thank you!")
        else:
            print("Book not found.")

    elif action == "4":
        title = input("Enter the book title to view details: ")
        book = library.get_book_by_title(title)
        if book:
            book.display_info()
        else:
            print("Book not found.")

    elif action == "5":
        title = input("Enter the title of the book to donate: ")
        author = input("Enter the author of the book: ")
        new_book = Book(title, author)
        library.add_book(new_book)
        print("Thank you for your donation!")

    elif action == "6":
        title = input("Enter the book title to search: ")
        book = library.get_book_by_title(title)
        if book:
            print("Book found!")
            book.display_info()
        else:
            print("Book not found.")

    elif action == "7":
        print("Bye! Please come again!")
        break

    else:
        print("Invalid choice. Try again.")