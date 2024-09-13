from . import connection

books = connection.books


def readBooks():

    return books.find({}, {"_id": 0})


def readBookISNB(ISNB):

    book = books.find_one({"book_ISNB": f"{ISNB}"}, {"_id": 0})

    if book is None:
        return False

    return book


def readBooksTitle(book_name):

    iniciais = book_name

    padrao = f"^{iniciais}"

    books_by_title = books.find({"book_name": {"$regex": padrao, "$options": "i"}}, {"_id": 0})

    if books_by_title is None:
        return False

    return books_by_title


def readBooksYear(year):

    books_year = books.find({"year": year}, {"_id": 0})

    if books_year is None:
        return False

    return books_year


def readBooksAuthor(book_author):

    inicias = book_author

    padrao = f"^{inicias}"

    books_author = books.find({"book_author": {"$regex": padrao, "$options": "i"}}, {"_id": 0})

    if books_author is None:
        return False

    return books_author
