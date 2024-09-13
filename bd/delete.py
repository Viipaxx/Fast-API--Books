# from . import connection
from bd import connection

books = connection.books

def deleteBook(book_ISNB):

    book_delete = books.find_one_and_delete({"book_ISNB": book_ISNB})

    if book_delete is None:
        return False

    return True
