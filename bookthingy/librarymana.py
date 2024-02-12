class Book:
    def __init__(self, count):
        self.count = count
        self.books_tt=[]
        self.books_au=[]
        self.books_isbn=[]

    def the_book(self):   
        for i in range(self.count):
            book_title=str(input("Title: "))
            book_author=str(input('Author: '))
            book_ISBN=int(input('ISBN: '))
            self.books_tt.append(book_title)
            self.books_au.append(book_author)
            self.books_isbn.append(book_ISBN)

    def display_book(self):
        print('Title: ', self.books_tt, 'Author: ', self.books_au, 'ISBN: ', self.books_isbn)


class Library:
    def __init__(self):
        self.books = Book(0)  # Create an instance of the Book class within the Library class

    def add_book(self, new_book):
        for j in range(new_book):
            book_title=str(input("Title: "))
            book_author=str(input('Author: '))
            book_ISBN=int(input('ISBN: '))
            self.books.books_tt.append(book_title)
            self.books.books_au.append(book_author)
            self.books.books_isbn.append(book_ISBN)

    def remove_book(self):
        book_title = str(input("Title: "))
        try:
            index = self.books.books_tt.index(book_title)
            del self.books.books_tt[index]
            del self.books.books_au[index]
            del self.books.books_isbn[index]
            print('Book removed successfully!')
        except ValueError:
            print('Book not found!')

    def search_books(self):
        name=str(input("Title: "))
        if name in self.books.books_tt:
            names=self.books.books_tt.index(name)
            print('Title: ',self.books.books_tt[names], 'Author: ', self.books.books_au[names], 'ISBN: ', self.books.books_isbn[names])
        else:
            print("There's no such book")

    def display_books(self):
        self.books.display_book()  # Utilize the display_book method of the Book instance in Library

bookss=Book(1)
bookss.the_book()
lib = Library()

# Add books to the library
lib.add_book(2)

# Display books in the library
lib.display_books()
lib.search_books()