class Book:
    def __init__(self, book_name, book_code, book_price, book_year, book_author):
        self.book_name = book_name
        self.book_code = book_code
        self.book_price = book_price
        self.book_year = book_year
        self.book_author = book_author
    
    def __str__(self):
        return f'{self.book_name} {self.book_code} {self.book_price} {self.book_year} {self.book_author}'

    def __repr__(self):
        return f'{self.book_name} {self.book_code} {self.book_price} {self.book_year} {self.book_author}'

    def __lt__(self, other):
        return self.book_name > other.book_name


books = [
    Book('AA', 121, 12.34, 2022, 'BC'),
    Book('AB', 124, 34.22, 2021, 'BB'),
    Book('AC', 125, 20, 2022, 'BC'),
    Book('AD', 120, 7.43, 2021, 'AC'),
]

def sort_name():
    print(sorted(books))

def author(other):
    for book in books:
        if book.book_name == other:
            print(book)

def search_book(other):
    for book in books:
        if book.book_code == other:
            print(book.book_year)
            return
    print('Book was not found')

sort_name()
author('A2')
search_book(120)
search_book(110)