class LibraryManagementSystem:
    def __init__(self, library_name, books=None):
        self.library_name = library_name
        self.books = books if books else []

    def add_book(self, book_title, author, year=None):

        book_info = {'title': book_title, 'author': author}
        if year:
            book_info['year'] = year
        self.books.append(book_info)

    def remove_book(self, book_title):
        
        try:
            for book in self.books:
                if book['title'] == book_title:
                    self.books.remove(book)
                    print(f"{book_title} has been removed from the library.")
                    return
            raise ValueError(f"Book with title {book_title} not found in the library.")
        except ValueError as e:
            print(e)

    def search_book(self, **kwargs):
        
        matches = []
        for book in self.books:
            if all(book.get(key) == value for key, value in kwargs.items()):
                matches.append(book)
        return matches

library = LibraryManagementSystem("My Library")
library.add_book("Harry Potter", "J.K. Rowling", 1997)
library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
library.add_book("To Kill a Mockingbird", "Harper Lee", 1960)

print(library.books)

library.remove_book("Harry Potter")

print(library.books)

search_results = library.search_book(author="Harper Lee")
print(search_results)


def vote_validity(val):
    match val:
        case x if x>=18:
            print("adult")
        case x if x<18:
            print("Not a adult")
        case _:
            print("invalid data")

val= int(input())
vote_validity(val)

