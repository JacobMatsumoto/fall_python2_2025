"""Create the Book Class:
Define a class named Book.
Inside the class, create an __init__ method with three parameters: title, author, and pages.
Initialize these parameters as attributes of the class.
Add Methods to the Book Class:
Create a method display_details that prints the title, author, and pages of the book.
Create a method is_long_book that returns True if the book has more than 100 pages, otherwise returns False.
Create Instances of the Book Class:
Create three instances of the Book class with different book details.
Assign these instances to variables: book1, book2, and book3.
Print Book Details and Length Status:
Use the display_details method to print the details of each book.
Use the is_long_book method to print whether each book is long or not."""

class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages
    
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_pages(self):
        return self.__pages
    
    def set_title(self, value):
        self.__title = value

    def set_author(self, value):
        self.__author = value

    def set_pages(self, value):
        self.__pages = value

    def print_details(self):  # prints the info
        print(f"{self.__title}, {self.__author}, {
              self.__pages},")
        
    def is_book_long(self):
        is_book_long = True
        if self.__pages > 100:
            is_book_long = True
        elif self.__pages < 100:
            is_book_long = False
        
        if is_book_long == True:
            print(f"{self.__title} is a long book")
        elif is_book_long == False:
            print(f"{self.__title} is not a long book")


def main():
    book1 = Book("One Fish Two Fish Red Fish Blue Fish", "Dr. Seuss", 10)
    book2 = Book("Dune", "Frank Herbert", 412)
    book3 = Book("The Hobbit", "J.R.R. Tolkien", 320)
     
    book1.print_details()
    book2.print_details()
    book3.print_details()

    book1.is_book_long()
    book2.is_book_long()
    book3.is_book_long()


main()