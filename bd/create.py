from . import connection

books = connection.books


def addBook(book_name, year, book_author, book_pages, book_ISNB):

    book = {
        "book_name": book_name,
        "year": year,
        "book_author": book_author,
        "book_pages": book_pages,
        "book_ISNB": book_ISNB
    }

    return books.insert_one(book)
